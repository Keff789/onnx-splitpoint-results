"""Render new paper figures from small derived tables; PDF/SVG deterministic."""
import argparse,json,sys
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

MODELS=['mobilenet_v3_large','regnet_x_1_6gf','resnet50','yolo11l','yolo26m','yolo26s','yolov7_paper']
LABEL=dict(zip(MODELS,['MobileNetV3-L','RegNetX-1.6GF','ResNet-50','YOLO11l','YOLO26m','YOLO26s','YOLOv7']))
SETUPS=['H8','H10','DeepX'];COLORS={'H8':'#1f77b4','H10':'#d97900','DeepX':'#2c8c51'}
MARKERS={'H8':'o','H10':'s','DeepX':'^'}
def order(r):return MODELS.index(r['model_id']),SETUPS.index(r['setup_id'])
def label(r):return LABEL[r['model_id']]+' / '+r['setup_id']
def main():
    p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True);a=p.parse_args()
    sys.path.insert(0,str(a.source_root/'scripts'))
    from extract_inputs import csvread,csvwrite,write
    O=a.output_root;T=O/'tables';F=O/'figures';P=O/'previews'
    for d in [F,P]:d.mkdir(exist_ok=True,parents=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8,'axes.titlesize':9,'axes.labelsize':8,'legend.fontsize':7,'xtick.labelsize':7,'ytick.labelsize':7,'axes.grid':True,'grid.alpha':.2,'grid.linewidth':.5,'axes.axisbelow':True,'savefig.bbox':'tight','pdf.fonttype':42,'ps.fonttype':42,'svg.fonttype':'none','svg.hashsalt':'thesis20-deep-20261004'})
    registry=[]
    def save(fig,name,rows,caption,role='main'):
        csvwrite(T/(name+'_source.csv'),rows)
        for suffix in ['pdf','svg']:
            metadata={'Creator':'THESIS20 offline analysis','CreationDate':None,'ModDate':None} if suffix=='pdf' else {'Date':None}
            fig.savefig(F/(name+'.'+suffix),metadata=metadata)
        fig.savefig(P/(name+'.png'),dpi=160);plt.close(fig)
        registry.append(dict(figure=name,role=role,pdf='figures/'+name+'.pdf',svg='figures/'+name+'.svg',source_csv='tables/'+name+'_source.csv',caption=caption))
    coverage=sorted(csvread(T/'coverage_matrix.csv'),key=order)
    fig,ax=plt.subplots(figsize=(7.2,5.5),layout='constrained')
    values=np.array([[r['generic_measured']/r['generic_required'],(r['native_base_split']+r['native_added_split'])/20,r['quality_loss']/r['quality_total'],r['energy_cases']/22] for r in coverage])
    ax.imshow(values,cmap='Blues',vmin=0,vmax=1,aspect='auto');ax.grid(False)
    for i,r in enumerate(coverage):
        texts=[f"{r['generic_measured']}/{r['generic_required']}",f"{r['native_base_split']} + {r['native_added_split']}",f"{r['quality_loss']}/{r['quality_total']}",f"{r['energy_cases']} / {r['energy_repeats']}"]
        for j,v in enumerate(texts):ax.text(j,i,v,ha='center',va='center',color='white' if values[i,j]>.65 else 'black',fontsize=8)
    ax.set_yticks(range(len(coverage)),[label(r) for r in coverage]);ax.set_xticks(range(4),['Historical Generic\nmeasured / required','Completed pairs\nbase + added','Quality loss\nloss / all','Native FS energy\ncases / repeats']);ax.xaxis.tick_top();ax.set_title('Observed coverage by model and setup',pad=38)
    save(fig,'fig01_coverage_matrix',coverage,'Coverage across 21 model/setup groups. Historical Generic: 527/588 observations (37 build failures and 24 policy exclusions); completed-task pairs: 192 base + 12 post-planned additions; quality: 39/560 accuracy-loss observations; Native full-system energy: 246 cases and 738 repeats, including 42 unique Full baselines. Counts are not common denominators across columns. Native unsupported cases (228) are terminal capability exclusions, listed separately. Cell shading is a visual count guide, not a common success probability. No uncertainty bars or performance baseline apply.')
    pairs=csvread(T/'energy_split_full.csv')
    fig,axs=plt.subplots(1,2,figsize=(7.2,3.2),layout='constrained')
    for ax,kind,title in zip(axs,['vendor_full','trt_full'],['Vendor Full','TensorRT Full']):
        rr=[r for r in pairs if r['baseline_kind']==kind]
        # The historical name may be tensorrt_full; use exact stored category.
        if not rr and kind=='trt_full':rr=[r for r in pairs if r['baseline_kind']!='vendor_full']
        for r in rr:
            color=COLORS[r['setup_id']];good=r['both_reference_close'];marker='x' if not r['semantic_comparable'] else MARKERS[r['setup_id']]
            ax.scatter(r['energy_window_rate_ratio'],r['energy_ratio'],s=15,marker=marker,c=color if good or marker=='x' else 'none',edgecolors=color if marker!='x' else None,alpha=.72)
        ax.axhline(1,color='black',lw=.7,ls='--');ax.axvline(1,color='black',lw=.7,ls='--');ax.set_xscale('log');ax.set_yscale('log');ax.set_title(title+f' (n={len(rr)} pairs)');ax.set_xlabel('Energy-window throughput: Split / Full')
        ax.text(.03,.03,'Faster and lower J/task:\n'+str(sum(r['energy_window_rate_ratio']>1 and r['energy_ratio']<1 for r in rr))+'/'+str(len(rr)),transform=ax.transAxes,fontsize=7)
    axs[0].set_ylabel('Full-system J/task: Split / Full')
    fig.legend(handles=[Line2D([],[],marker=MARKERS[s],color=COLORS[s],ls='',label=s) for s in SETUPS],loc='upper center',bbox_to_anchor=(.55,1.07),ncol=3,frameon=False)
    save(fig,'fig02_split_full_benefit',pairs,'All 408 descriptive Split/Full comparisons (204 per baseline family), derived from 204 split cases and 42 reused Full baselines; pairs are dependent. Ratios use means of three per-replicate E/N and N/T values from the same active energy windows; primary energy is calibrated full-system, without idle subtraction. Dashed lines denote equality. Hollow symbols retain accuracy loss in either endpoint; crosses mark 16 unsupported semantic comparisons (all Vendor Full). The other 392 have local semantic evidence. No range bars are drawn here; all nine repetition combinations are provided in the supplement tables. TRT Full references share a declared historical attestor-source gap. No causal or deployment claim is inferred.')
    ranks=sorted([r for r in csvread(T/'rank_groups.csv') if r['cohort']=='augmented' and r['tier']=='technical'],key=order)
    reps={(r['model_id'],r['setup_id']):r for r in csvread(T/'rank_repeat_sensitivity.csv') if r['cohort']=='augmented' and r['tier']=='technical'}
    fig,axs=plt.subplots(1,2,figsize=(7.2,6),gridspec_kw={'width_ratios':[1,1.15]},layout='constrained')
    source=[]
    for i,r in enumerate(ranks):
        x=reps[(r['model_id'],r['setup_id'])];c=COLORS[r['setup_id']];source.append(dict(r,repeat_L_R_min=x['L_R_min'],repeat_L_R_max=x['L_R_max'],repeat_rho_min=x['rho_min'],repeat_rho_max=x['rho_max'],repeat_top1_hits=x['top1_hits']))
        axs[0].plot([x['rho_min'],x['rho_max']],[i,i],color=c,alpha=.45,lw=2);axs[0].scatter(r['rho'],i,color=c,marker=MARKERS[r['setup_id']],s=22)
        axs[1].plot([100*x['L_R_min'],100*x['L_R_max']],[i,i],color=c,alpha=.45,lw=2);axs[1].scatter(100*r['L_R'],i,color=c,marker=MARKERS[r['setup_id']],s=22)
        axs[1].text(77,i,f"{x['top1_hits']}/9",fontsize=7,va='center')
    axs[0].set_yticks(range(21),[label(r)+f"  n={r['n']}" for r in ranks]);axs[1].set_yticks(range(21),['']*21)
    axs[0].set_xlim(-1.05,1.05);axs[1].set_xlim(-2,90);axs[0].set_xlabel('Spearman ρ');axs[1].set_xlabel('Throughput loss L_R (%)');axs[0].set_title('(a) Rank transfer');axs[1].set_title('(b) Generic-Top1 loss; hit count / 9')
    for ax in axs:ax.invert_yaxis();ax.axvline(0,color='gray',lw=.7)
    save(fig,'fig03_selection_and_stability',source,'Generic-to-Native selection in all 21 exact model/setup/precision/endpoint groups (204 augmented technical pairs; n=17, 19 or 20 for classification and n=3 for YOLO). Symbols use three-repeat median throughput; horizontal segments show min/max over nine Generic/Native repetition combinations, not confidence intervals or independent studies. L_R=1−R_selected/R_best; L_C uses a different denominator and is tabulated separately. Right labels count exact Top1 hits across the nine combinations. All accuracy-loss cases are retained; quality-transfer and reference-close sensitivities are in rank_groups.csv. The baseline is the best observed Native candidate within the same group.')
    cases=csvread(T/'rank_cases.csv');yolo=[r for r in cases if r['model_id'].startswith('yolo')]
    fig,axs=plt.subplots(4,3,figsize=(7.2,7.5),layout='constrained')
    for mi,m in enumerate(MODELS[3:]):
        for si,s in enumerate(SETUPS):
            ax=axs[mi,si];rr=sorted([r for r in yolo if r['model_id']==m and r['setup_id']==s],key=lambda r:r['case_id'])
            for i,r in enumerate(rr):
                for offset,prefix,marker,color in [(-.12,'generic','o','#777777'),(.12,'native','s',COLORS[s])]:
                    val=r[prefix+'_completed_task_fps'];lo=r[prefix+'_min'];hi=r[prefix+'_max'];ax.errorbar(i+offset,val,yerr=[[val-lo],[hi-val]],fmt=marker,color=color,mfc='none' if r[prefix+'_task_quality_status']=='accuracy_loss' else color,ms=3,capsize=2,lw=.8)
            ax.set_title(LABEL[m]+' / '+s);ax.set_xticks(range(3),[r['case_id']+(' *' if r['observation_origin']=='augmentation' else '') for r in rr]);ax.set_ylim(0,1.1*max(max(r['native_max'],r['generic_max']) for r in rr))
            if si==0:ax.set_ylabel('Completed tasks/s')
    fig.legend(handles=[Line2D([],[],marker='o',color='#777777',ls='',label='Generic'),Line2D([],[],marker='s',color='black',ls='',label='Native')],loc='upper center',bbox_to_anchor=(.5,1.04),ncol=2,frameon=False)
    save(fig,'fig04_yolo_fixed_candidates',yolo,'All 36 YOLO completed-task pairs in 12 groups, with exactly three measured boundaries per group. Circles/squares show Generic/Native median throughput; bars are min/max of three 1000-task repetitions (not confidence intervals). Asterisks mark the 12 post-planned additions; the 12 short predecessor runs are excluded. Boundary labels are categorical, not a common graph-depth axis; no interpolation is drawn. Both runners use the existing task-completion pairing evidence, with uncontrolled runtime conditions. Hollow symbols retain accuracy losses; quality-transfer exclusions and filtered groups with fewer than three candidates are retained in the supplement. No Full baseline appears.')
    pareto=[r for r in csvread(T/'energy_pareto.csv') if r['view']=='augmented' and r['filter']=='technical']
    close_front={(r['model_id'],r['setup_id'],r['case_id']) for r in csvread(T/'energy_pareto.csv') if r['view']=='augmented' and r['filter']=='reference_close_transfer' and r['pareto']}
    def draw_energy(ax,m,s,annotate=False):
        rr=[r for r in pareto if r['model_id']==m and r['setup_id']==s];src=[]
        for r in rr:
            x,y=r['energy_fps'],r['j_per_task'];ax.errorbar(x,y,xerr=[[x-r['energy_fps_min']],[r['energy_fps_max']-x]],yerr=[[y-r['j_per_task_min']],[r['j_per_task_max']-y]],fmt='none',ecolor=COLORS[s],alpha=.35,lw=.5)
            ax.scatter(x,y,s=30 if r['pareto'] else 12,marker='^' if r['cohort']=='augmentation' else 'o',facecolors='none' if r['accuracy_class']=='accuracy_loss' else COLORS[s],edgecolors='black' if (m,s,r['case_id']) in close_front else COLORS[s],linewidths=.9)
            if annotate and r['pareto']:ax.annotate(r['case_id'],(x,y),xytext=(-5,7),ha='right',textcoords='offset points',fontsize=7)
            src.append(dict(r,plot_role='split',reference_close_frontier=(m,s,r['case_id']) in close_front))
        for kind,marker in [('vendor_full','D'),('trt_full','X')]:
            matches=[r for r in pairs if r['model_id']==m and r['setup_id']==s and (r['baseline_kind']=='vendor_full')==(kind=='vendor_full')]
            r=matches[0]
            ax.scatter(r['baseline_energy_fps'],r['baseline_j_per_task'],marker=marker,edgecolors='black',s=38,facecolors='none' if r['baseline_accuracy_class']=='accuracy_loss' else 'black')
            src.append(dict(model_id=m,setup_id=s,case_id='full',plot_role=kind,energy_fps=r['baseline_energy_fps'],j_per_task=r['baseline_j_per_task'],semantic_comparable=all(x['semantic_comparable'] for x in matches),baseline_uid=r['baseline_uid'],baseline_accuracy_class=r['baseline_accuracy_class']))
        ax.set_title(LABEL[m]+' / '+s);ax.set_xlabel('Tasks/s in energy window');ax.set_ylabel('Full-system J/task');return src
    fig,axs=plt.subplots(1,3,figsize=(7.2,2.9),layout='constrained');source=[]
    for ax,(m,s) in zip(axs,[('resnet50','DeepX'),('regnet_x_1_6gf','H10'),('mobilenet_v3_large','DeepX')]):source+=draw_energy(ax,m,s,True)
    save(fig,'fig05_energy_choices',source,'Three contrasting exact energy strata: ResNet-50/DeepX (stable throughput/energy tradeoff), RegNet/H10 (same winner), and MobileNet/DeepX (small energy difference with unstable winner). All split candidates are shown; large circles denote the technical split Pareto frontier and black outlines its reference-close-transfer counterpart. Full references (diamond: Vendor; X: TRT) are contextual, not inserted into the split frontier; all comparisons in these three panels have local semantic evidence. Values are means of three per-replicate E/N and N/T ratios; bars are observed min/max, not CIs. Fulls are plotted once per panel. Calibrated full-system energy has no idle subtraction. The TRT attestor-source gap remains. Panel case counts, identities and precision/calibration contracts are in the source CSV; no cross-panel dominance is implied.')
    graph=csvread(T/'graph_completed_cases.csv');rg=[r for r in graph if r['model_id']=='regnet_x_1_6gf' and r['setup_id']=='H10']
    fig,axs=plt.subplots(1,2,figsize=(7.2,3),layout='constrained')
    for r in rg:
        x=100*r['stored_flops_left_ratio'];axs[0].scatter(x,r['generic_completed_task_fps'],marker='o',color='#777777',s=17);axs[0].scatter(x,r['native_completed_task_fps'],marker='s',color=COLORS['H10'],s=17)
        axs[1].scatter(r['generic_completed_task_fps'],r['native_completed_task_fps'],color=COLORS['H10'],s=17)
        if r['case_id'] in ['b052','b123']:
            axs[1].annotate(r['case_id'],(r['generic_completed_task_fps'],r['native_completed_task_fps']),xytext=(3,4),textcoords='offset points',fontsize=7)
    axs[0].set_xlabel('Stored analytical stage-1 FLOPs share (%)');axs[0].set_ylabel('Completed tasks/s');axs[1].set_xlabel('Generic completed tasks/s');axs[1].set_ylabel('Native completed tasks/s');axs[0].set_title('(a) Opposite associations with graph placement');axs[1].set_title('(b) Within-group rank reversal')
    axs[0].legend(handles=[Line2D([],[],marker='o',color='#777777',ls='',label='Generic'),Line2D([],[],marker='s',color=COLORS['H10'],ls='',label='Native')],frameon=False)
    save(fig,'fig06_regnet_counterexample',rg,'RegNetX-1.6GF/H10, all 20 original reference-close completed-task candidates. Points are three-repeat medians (ranges are tabulated and selection sensitivity appears in Fig. 3); no smoothing, regression fit or confidence bands. The x-axis of panel (a) uses the saved analytical FLOPs share, not measured stage time or normalized boundary IDs. Generic/Native rank reversal is descriptive; materialized two-worker Generic and asynchronous Native paths, plus uncontrolled thread/thermal conditions are alternative explanations, not isolated causes. Panel (b) compares identical candidate identities. Full baselines and post-planned additions are absent; numerical results do not establish a universal manufacturer property.')
    # Supplements retain all quality losses, raw-proxy groups and energy strata.
    quality=csvread(T/'quality_losses.csv');fig,axs=plt.subplots(1,2,figsize=(7.2,6),layout='constrained')
    for ax,metric,title in zip(axs,['Top1','COCO_AP_50_95'],['Top-1 accuracy','COCO AP50:95']):
        rr=[r for r in quality if r['metric']==metric]
        for i,r in enumerate(rr):
            ax.plot([r['delta_ci_low_pp'],r['delta_ci_high_pp']],[i,i],color=COLORS[r['setup_id']],lw=1);ax.scatter(r['delta_pp'],i,color=COLORS[r['setup_id']],marker='o' if r['uncertainty']=='supported' else 'x',s=18)
        ax.set_yticks(range(len(rr)),[LABEL[r['model_id']].replace('MobileNetV3-L','MobileNet')+' '+r['setup_id']+(' Full' if r['variant']=='vendor_full' else ' '+r['case_id']) for r in rr],fontsize=6.5);ax.invert_yaxis();ax.set_title(title+f' (n={len(rr)})');ax.set_xlabel('Candidate − ONNX reference (pp)');ax.axvline(0,color='gray',lw=.7)
    save(fig,'supp01_quality_losses',quality,'All 39 retained accuracy-loss observations: 22 Top-1 and 17 AP50:95, shown in separate panels; 30 are splits and 9 are Vendor Full companions. Full labels identify the execution variant even when the stored case_id names a companion boundary. Points are original N=5000 estimates; bars are the original paired-bootstrap B=1000 95% intervals for absolute metric differences, with no bootstrap rerun. Crosses mark seven losses whose original relative-loss intervals cross the frozen 5% reporting threshold; circles mark 32 supported losses. Classification/detection metrics are not pooled. The original 0.01 absolute task margin (one percentage point) is retained separately from the relative reporting rule. All other 521 reference-close observations are in quality_effects.csv. All 39 losses are original-base observations.','supplement')
    proxies=[r for r in csvread(T/'rank_proxy_comparison.csv') if r['tier']=='technical' and r['n_common']>=3];proxies.sort(key=order)
    fig,axs=plt.subplots(1,2,figsize=(7.2,4),layout='constrained')
    for i,r in enumerate(proxies):
        for ax,left,right,scale in [(axs[0],'raw_rho','completion_rho',1),(axs[1],'raw_L_R','completion_L_R',100)]:
            ax.plot([scale*r[left],scale*r[right]],[i,i],color=COLORS[r['setup_id']],lw=1);ax.scatter(scale*r[left],i,marker='o',facecolors='none',edgecolors=COLORS[r['setup_id']],s=26);ax.scatter(scale*r[right],i,marker='s',color=COLORS[r['setup_id']],s=20)
    for ax in axs:ax.set_yticks(range(len(proxies)),[label(r)+f" n={r['n_common']}" for r in proxies]);ax.invert_yaxis()
    axs[0].set_xlabel('Spearman ρ');axs[1].set_xlabel('Native throughput loss L_R (%)');axs[0].set_title('Open: historical raw; filled: completion');axs[1].set_title('Same original candidates in each comparison')
    save(fig,'supp02_proxy_change',proxies,'Historical raw-output proxy versus Generic task-completion proxy on exactly the same original candidate identities in each group. All technical groups with n≥3 appear; groups below three remain tabulated. Open circles: raw; filled squares: completion; Native reference uses the same three-repeat medians. No error bars are implied. No short augmentation predecessors enter the raw cohort. Changes in ranking and throughput regret are not causally attributable solely to postprocessing because acquisition date, runtime, thread and thermal conditions are uncontrolled.','supplement')
    fig,axs=plt.subplots(7,3,figsize=(7.2,13),layout='constrained');source=[]
    for mi,m in enumerate(MODELS):
        for si,s in enumerate(SETUPS):source+=draw_energy(axs[mi,si],m,s)
    save(fig,'supp03_all_energy_groups',source,'All 21 exact energy strata, using the same encoding and aggregation as Fig. 5: all 204 split cases plus 42 unique contextual Fulls, three valid energy repeats per case. Min/max bars are not confidence intervals. Fulls do not enter the split Pareto frontier. Vendor Full semantic limits affect all four DeepX detection models and additionally YOLO11l/YOLO26s on H8 and H10; see all 16 comparisons in energy_semantic_limits.csv and per-reference source rows. These references remain descriptive context and are not declared semantically interchangeable. Technical and reference-close-transfer frontiers are distinguished. Hollow split markers and hollow Full diamonds retain accuracy losses (9 of 21 Vendor Fulls); filled Full markers are reference_close. No cross-model/setup dominance is inferred.','supplement')
    write(O/'figure_index.json',registry)
    (O/'CAPTIONS.md').write_text('# English paper captions\n\n'+'\n\n'.join('## '+r['figure']+' ('+r['role']+')\n\n'+r['caption'] for r in registry)+'\n')
    print(json.dumps({'main_figures':sum(r['role']=='main' for r in registry),'supplements':sum(r['role']=='supplement' for r in registry)}))
if __name__=='__main__':main()
