#!/usr/bin/env python3
"""Generate methods, evidence-linked findings and portable manuscript assets."""
import csv
import json
from pathlib import Path
import zipfile

def read(p):
    return json.loads(p.read_text())

def tex(value):
    replacements = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$',
                    '#': r'\#', '_': r'\_\allowbreak{}', '/': r'/\allowbreak{}', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}'}
    return ''.join(replacements.get(c, c) for c in str(value))

def render(output):
    out = Path(output)
    s = read(out/'summary.json')
    data = read(out/'PAPER_DATASET.json')
    ng = s['native_generic']
    fc = s['fastest_full_comparison']
    ec = s['lowest_full_energy_comparison']
    opt = s['optima']
    top = read(out/'tables/table3_top2_native.json')
    best = max(top, key=lambda r: r['speedup'])
    n_single = sum(r['performance_observations']==1 for r in data)
    mismatches = [r for r in data if r.get('quality_cached_loss_disagrees')]
    methods = f'''# Methods: Refresh16 paper analysis

The analysis uses the canonical `refresh16_20261013` selection, projected from `CURRENT.json` and its existing manifest. It contains {s['cases']} deployment identities ({s['native']} Native and {s['generic']} Generic), including {s['full_coverage']['configurations']} host-specific Full configurations. Refresh16 replaces performance and energy for {s['refresh16_cases']} exact Native identities with three independently executed performance repeats and three energy repeats each. The other {s['unchanged_cases']} rows and all original quality selections and flags are preserved. No measurement, model build or dataset evaluation is performed by this offline tool.

## Selection and coverage

The primary view includes every available measured numeric observation. Accuracy-loss classes, a 5% loss threshold, a single historical repeat, screening/diagnostic status, old claim flags and missing administrative hashes do not veto a row. Included means used in this descriptive deployment comparison; it does not establish equality of executed work. Performance-only questions use observed FPS independently of energy; energy questions require observed energy, and joint questions use the intersection. The measured coverage is {s['performance_coverage']}/{s['cases']} FPS, {s['energy_coverage']}/{s['cases']} energy and {s['quality_numeric_coverage']}/{s['cases']} numeric dataset-quality values.

Source selection follows completed canonical observations, never highest FPS or filesystem modification time. The explicit per-metric fallback accepts a latest completed older observation only when a newer matching metric is absent or invalid, retaining exact host, model, cut, runtime, input and endpoint identity. No such fallback is needed for the current complete FPS/energy matrix. Source generations and actual field locations are listed in `METRIC_SOURCES.csv` and `MEASUREMENT_GENERATIONS.csv`; re-assignment of existing quality is not counted as a new evaluation.

## Metrics and uncertainty

Throughput is images/s (FPS), preserving the median of the recorded independent repeats. Historical single observations remain labelled n=1 ({n_single} current identities), without an invented confidence interval. The primary energy is calibrated host-inclusive energy per completed image: for repeat r, e_r=E_r/N_r, then mean(e_r). The compact display is 1000*mean(e_r) mJ/image. N_r is completed images, never detected boxes. Total joules, actual command-window duration, average power, image count and each repeat remain in the accompanying tables. Existing host/idle-corrected comparison energy is a separately labelled sensitivity; no new correction is estimated.

The descriptive repeat range and sample coefficient of variation remain visible. Existing three-repeat t intervals describe the energy mean, not the FPS median, and do not establish between-implementation significance. Mean(N/E), 1/mean(E/N) and sum(N)/sum(E) are separately named and generally differ. Neither J/FPS nor a compound throughput/energy score is used. Small differences are observations, not significance claims.

## Comparisons and weighting

All ratios are computed from unrounded inputs. Native/Generic pairs match model, host and cut. All split rows are compared to both measured Full alternatives on the same host, with winners and nonwinners retained. Table 2 reports TRT ranges across the three host aggregates; these ranges are not repeat confidence intervals. Host values and arithmetic means are separately available. Table 3 selects the two Native configurations with the largest FPS ratio to the fastest observed Full on the same host for each model. Stable ascending UID breaks ties. Energy never changes this FPS ranking. Energy gain G_n=e_full/e_split uses exactly the same Full identity as that row's speedup; values greater than one indicate lower split energy. The independently lowest-energy Full is kept separately.

Point-pooled summaries are separate from equal-model summaries. The latter first take the point median within each model/setup, then average setups within each model, then average those model values. Classifiers with many cuts therefore receive no extra model weight. Fastest and lowest-energy splits are selected within each model/setup/runner. Shared optima are one configuration; groups with a single candidate are distinguished from multiple-candidate groups. All optimum and Top-2 selections are retrospective, with no prediction or causal interpretation.

## Dataset quality and source inconsistencies

Top-1 accuracy and COCO mAP@[.50:.95] are distinct metrics. Numerical metrics, reference values, sample counts and existing bootstrap intervals are copied from the selected completed quality evidence. Output parity/PASS is not dataset accuracy. Relative loss (reference-candidate)/reference and percentage-point differences 100*(candidate-reference) are separately named. Vendor-Full and split quality are shown even when Hailo Full quality is substantially below the model reference.

For {len(mismatches)} Native DeepX classifier rows, the selected quality summary's numerical result differs from the cached relative loss in Current. The newer summary numbers are exposed as `quality_value` and `quality_numeric_relative_loss`; the original `quality_relative_loss`, quality class and gates remain unchanged. Both values and their exact sources are published, rather than substituting an older, more favorable result or silently repairing Current. This is a projection of existing reports, not a new quality evaluation. The prior 17 administrative receipt-version gaps and unresolved historical Full-producer source version remain provenance limits.

## Executed work and remaining interpretation limits

All 36 Native detector split configurations record `fast_oracle_outside_timing`, whereas the 36 corresponding Generic detector splits record `decoded_nms`. The refreshed YOLO26s Native path explicitly records `native_three_stage_fast_oracle_outside_timing`: its correctness oracle runs outside the timed loop. For the refreshed YOLO26s Full paths, H8/H10 Vendor Full records `frozen_host_tail` with dense outputs and host decoding/NMS. TRT Full records integrated accelerator execution plus frozen normalization, including prepared-input H2D, engine execution, D2H synchronization, filtering, class-aware NMS and inverse letterbox. The per-configuration completion modes and execution notes retain the other models' recorded boundaries. These actual implementation differences remain in the data and captions even where a comparison-endpoint declaration matches. A missing or different administrative hash alone establishes neither equal nor different work and does not remove an observation. The deployment ratios therefore do not isolate the causal effect of graph splitting at equal executed work.

Other recorded completion modes, prepared-input geometry and work boundaries are retained per identity. Missing contract hashes alone are not evidence of different executed work; unknown entries remain unknown. The exact old clock profiles for Refresh16 cases 11-13 remain undocumented; the handoff reports 96 current before/after snapshots without profile mismatch. Contextual comparisons are retained. Strict historical claim/provenance and reference-close views are optional sensitivities, never the hidden main selection. Broad plots show raw throughput, host-inclusive energy and quality. Any descriptive Pareto table explicitly names its two objectives and recorded work cohort; it is not an equal-quality or universal endpoint-equivalence claim.
'''
    (out/'METHODS.md').write_text(methods)
    claims = [
        {'claim':'Full numeric deployment coverage', 'metric_denominator':f"{s['performance_coverage']}/{s['cases']} FPS; {s['energy_coverage']}/{s['cases']} energy; {s['quality_numeric_coverage']}/{s['cases']} quality; {s['full_coverage']['configurations']} Full configurations", 'selection':'Broad canonical Refresh16', 'evidence':'PAPER_DATASET.csv; tables/full_configurations.csv; figures/01_full_throughput.pdf; figures/02_full_energy.pdf', 'limitation':'Coverage does not prove identical timed work or quality.'},
        {'claim':'Native is faster than Generic at many, but not all, paired points', 'metric_denominator':f"{ng['faster']}/{ng['n_performance']}; pooled median FPS ratio {ng['fps_ratio_median']:.6f}", 'selection':'All matching model/setup/cut pairs with FPS', 'evidence':'tables/native_generic_pairs.csv; tables/native_generic_groups.csv', 'limitation':'Point-pooled distribution; cut multiplicity differs among models.'},
        {'claim':'Native often uses less energy than Generic', 'metric_denominator':f"{ng['energy_lower']}/{ng['n_energy']}; pooled median energy ratio {ng['energy_ratio_median']:.6f}; both better {ng['both_better']}/{ng['n_joint']}", 'selection':'Raw host-inclusive energy pairs; joint intersection for both-better', 'evidence':'tables/native_generic_pairs.csv', 'limitation':'Mean per-repeat E/N; workload, runner and quality differences remain.'},
        {'claim':'Some Native splits beat the fastest observed same-host Full', 'metric_denominator':f"{fc['faster']}/{fc['splits']}", 'selection':'Every Native split versus fastest Full of same model/host', 'evidence':'tables/baseline_selection.csv; tables/table3_top2_native.csv', 'limitation':'Retrospective deployment comparison, not equal-work causality.'},
        {'claim':'Some Native splits use less energy than the independently lowest-energy Full', 'metric_denominator':f"{ec['lower']}/{ec['splits']}", 'selection':'Every Native split versus minimum raw energy Full of same model/host', 'evidence':'tables/baseline_selection.csv', 'limitation':'This separate baseline is not substituted into Table 3 G_n.'},
        {'claim':'Largest observed Native split/fastest-Full speedup', 'metric_denominator':f"{best['speedup']:.6f}x; {best['model']} {best['setup']}/{best['case']}; same-Full G_n={best['energy_gain_same_full']:.6f}", 'selection':f"{fc['splits']} Native split candidates; Top-2 per model", 'evidence':'tables/table3_top2_native.csv', 'limitation':'Maximum selected after observing measurements; no held-out prediction claim.'},
        {'claim':'Throughput and energy optima can differ', 'metric_denominator':f"{opt['multi_candidate_conflicts']}/{opt['multi_candidate_groups']} Native groups with multiple candidates; {opt['single_candidate_groups']} single-candidate groups", 'selection':'Within model/setup, raw energy versus FPS', 'evidence':'tables/model_setup_optima.csv', 'limitation':'A shared optimum is one point, not two independent observations.'},
        {'claim':'Negative quality observations remain in the main dataset', 'metric_denominator':f"{s['quality_loss'].get('native',0)} Native and {s['quality_loss'].get('generic',0)} Generic original accuracy_loss flags", 'selection':'No 5% or quality veto', 'evidence':'PAPER_DATASET.csv; tables/quality_comparison.csv', 'limitation':'Top-1 and mAP differ; original classes are preserved, not reevaluated.'},
        {'claim':'Selected quality report and cached Current loss can disagree', 'metric_denominator':f"{len(mismatches)}/{s['cases']} identities", 'selection':'Numerical selected report versus preserved cached scalar', 'evidence':'PAPER_DATASET.csv; METRIC_SOURCES.csv', 'limitation':'No silent repair or favorable historical replacement; both values retained.'},
        {'claim':'Refresh selection preserves other observations', 'metric_denominator':f"{s['refresh16_cases']} refreshed; {s['unchanged_cases']} unchanged; {s['cases']} original quality selections/gates retained", 'selection':'Exact Refresh16 UID list against prior frozen cases', 'evidence':'../validation/independent_check.py; ../inputs/refresh16_provenance.json', 'limitation':'No new quality evaluation; acquisition failures remain in the canonical archive.'}
    ]
    with (out/'CLAIM_EVIDENCE.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,list(claims[0]),lineterminator='\n');w.writeheader();w.writerows(claims)
    md=['# Claim-to-evidence table','', '| Claim | Exact metric / denominator | Selection | Evidence | Limitation |', '|---|---|---|---|---|']
    md.extend('| '+' | '.join(r.values())+' |' for r in claims)
    (out/'CLAIM_EVIDENCE.md').write_text('\n'.join(md)+'\n')
    lt=[r'% Requires booktabs, longtable and array.',r'\begin{longtable}{@{}>{\raggedright\arraybackslash}p{.18\linewidth}>{\raggedright\arraybackslash}p{.19\linewidth}>{\raggedright\arraybackslash}p{.17\linewidth}>{\raggedright\arraybackslash}p{.19\linewidth}>{\raggedright\arraybackslash}p{.17\linewidth}@{}}',r'\toprule',r'Claim & Metric / denominator & Selection & Evidence & Limitation \\ \midrule \endhead']
    lt.extend(' & '.join(tex(v) for v in r.values())+r' \\' for r in claims)
    lt.extend([r'\bottomrule',r'\end{longtable}'])
    (out/'CLAIM_EVIDENCE.tex').write_text('\n'.join(lt)+'\n')
    findings = f'''# Findings from the broad Refresh16 selection

This report is generated from the same selected rows as Tables 2/3 and all figures. {s['cases']} identities provide {s['performance_coverage']} FPS and {s['energy_coverage']} energy observations, including all {s['full_coverage']['configurations']} Full deployments. Numeric dataset quality covers {s['quality_numeric_coverage']} identities. No measurement or quality evaluation was started by this analysis.

Native exceeds Generic throughput in {ng['faster']}/{ng['n_performance']} paired points and uses less raw energy in {ng['energy_lower']}/{ng['n_energy']}; {ng['both_better']}/{ng['n_joint']} improve both. The point-pooled median Native/Generic ratios are {ng['fps_ratio_median']:.4f} for throughput and {ng['energy_ratio_median']:.4f} for energy. Separate equal-model results in `tables/equal_model_summary.json` avoid weighting models by their number of cuts.

Against the fastest Full on the same host, {fc['faster']}/{fc['splits']} Native splits are faster. Against the separately selected minimum-energy Full, {ec['lower']}/{ec['splits']} use less energy. The largest observed speedup is {best['speedup']:.3f}x for {best['model']} {best['setup']}/{best['case']}; its energy gain against that exact same Full is {best['energy_gain_same_full']:.3f}. Table 3 reports the Top-2 for every model, selected from unrounded FPS ratios without energy filtering. These are retrospective results.

The fastest and minimum-energy Native split differ in {opt['multi_candidate_conflicts']}/{opt['multi_candidate_groups']} groups with more than one candidate. Shared optima and the candidate counts are shown explicitly. A small ratio above one is described as a small observed advantage; the analysis does not infer statistical significance from it.

Quality is a separate result axis. The original {s['quality_loss'].get('native',0)} Native and {s['quality_loss'].get('generic',0)} Generic accuracy-loss flags remain visible. Vendor Full quality, model reference quality and every available split score appear in the quality figures. {len(mismatches)} cached Current losses differ from the numerical selected quality reports; both are retained. The Full and split figures display actual deployments with their quality and timed-work differences, including the YOLO26s fast-oracle versus host-tail distinction described in `METHODS.md`.

See [Table 2](tables/table2_full.md), [Table 3](tables/table3_top2_native.md), [methods](METHODS.md), [claim evidence](CLAIM_EVIDENCE.md), [figure captions](CAPTIONS.md), and [all machine-readable findings](summary.json). Missing values, if any, are enumerated by UID in `summary.json`. Historical source-version and clock-profile limitations remain; these do not trigger a new measurement campaign.
'''
    (out/'FINDINGS.md').write_text(findings)
    # Source paragraphs are supplied separately from any private manuscript.
    paragraph = ('We report the broad measured deployment selection, retaining quality-loss, single-repeat and screening observations with their original flags. '
                 'Throughput is the recorded cohort median in images/s. Energy is calibrated host-inclusive energy per completed image, averaged as the mean of per-repeat E/N and displayed in mJ/image. '
                 'Dataset Top-1 accuracy or COCO mAP is reused from the selected existing evidence and shown separately. '
                 'Table 3 ranks Native splits retrospectively against the fastest measured Full on the same host and uses that exact Full for both speedup and energy gain. '
                 'Source generations and numerical quality/cache discrepancies are recorded per metric. '
                 'Native detector splits record a correctness oracle outside timing, whereas Generic detector splits record decoded NMS; refreshed YOLO26s Full paths include their recorded host-tail or integrated normalization work. These ratios compare observed deployments and do not isolate a causal effect of splitting at identical work.')
    (out/'METHODS_PARAGRAPH.tex').write_text(tex(paragraph)+'\n')
    index=read(out/'figures/INDEX.json')
    assets=out/'assets';assets.mkdir(exist_ok=True)
    for name, selected in [('MLSys', [r for r in index if r['main_paper']]), ('Dissertation', index)]:
        contents={}
        for f in ['tables/table2_full.tex','tables/table3_top2_native.tex','CLAIM_EVIDENCE.tex','CLAIM_EVIDENCE.md','CLAIM_EVIDENCE.csv','METHODS.md','METHODS_PARAGRAPH.tex','CAPTIONS.md']:
            contents[f]=(out/f).read_bytes()
        for p in sorted((out/'tables').glob('*')):
            if p.suffix in ['.tex', '.md']:
                contents['tables/'+p.name] = p.read_bytes()
        for r in selected:
            for ext in ['pdf','svg','png']:
                f='figures/'+r['name']+'.'+ext
                contents[f]=(out/f).read_bytes()
        # Every package can be unpacked and compiled independently as a preview.
        driver=[r'\documentclass[a4paper]{article}',r'\usepackage[margin=16mm]{geometry}',r'\usepackage{booktabs,siunitx,graphicx,longtable}',r'\usepackage[T1]{fontenc}',r'\begin{document}',r'\section*{Refresh16 manuscript assets: '+name+'}',r'\input{METHODS_PARAGRAPH.tex}',r'\begin{table}[ht]\centering\resizebox{\textwidth}{!}{\input{tables/table2_full.tex}}\caption{Full deployments. TRT ranges span host aggregates, not confidence intervals.}\end{table}',r'\begin{table}[ht]\centering\resizebox{\textwidth}{!}{\input{tables/table3_top2_native.tex}}\caption{Retrospective Native Top-2 per model. Energy gain uses the same Full as speedup.}\end{table}',r'\clearpage']
        for r in selected:
            driver.extend([r'\begin{figure}[p]\centering',r'\includegraphics[width=\textwidth,height=.72\textheight,keepaspectratio]{figures/'+r['name']+'.pdf}',r'\caption{'+tex(r['caption'])+'}',r'\end{figure}\clearpage'])
        driver.extend([r'\small\input{CLAIM_EVIDENCE.tex}',r'\end{document}'])
        contents['preview.tex']=('\n'.join(driver)+'\n').encode()
        contents['README.txt']=(f'{name} assets from paper_after_refresh16_20261013.\nUnpack and compile preview.tex with pdflatex; booktabs, siunitx, graphicx and longtable are required.\nThis is an asset preview, not a submitted or overwritten manuscript.\nRead METHODS.md and CLAIM_EVIDENCE.md before final manuscript integration.\n').encode()
        with zipfile.ZipFile(assets/(name+'_assets.zip'),'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
            for path, payload in sorted(contents.items()):
                zi=zipfile.ZipInfo(path,(2026,10,14,0,0,0));zi.compress_type=zipfile.ZIP_DEFLATED;zi.external_attr=0o100644<<16
                z.writestr(zi,payload,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    (assets/'README.md').write_text('# Manuscript asset packages\n\n[MLSys](MLSys_assets.zip) contains the compact main-paper figure selection; [Dissertation](Dissertation_assets.zip) contains all model views. Both include standalone LaTeX Tables 2/3, figures in PDF/SVG/PNG, captions, methods and the claim-to-evidence table. Unpack and compile `preview.tex`. Private manuscripts are not part of these packages.\n')

if __name__ == '__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True)
    render(p.parse_args().output)
