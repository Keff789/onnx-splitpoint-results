#!/usr/bin/env python3
"""Generate browsable figure/table indexes without modifying or copying evidence.

No plotting, waveform access, third-party modules, network, Git writes or auto-install.
"""
from pathlib import Path
import argparse, csv, html, json, os, re
from collections import defaultdict
from urllib.parse import quote
from layout import E, TIM, PARMA, THEMES, topic_for, TIM_LABELS

IMAGE = {'.png','.svg','.jpg','.jpeg','.webp'}
FIG = IMAGE | {'.pdf','.eps'}
TAB = {'.csv','.tsv','.tex','.md','.ods','.xlsx','.xls'}


def link(page, target):
    return quote(os.path.relpath(target, page.parent).replace(os.sep,'/'), safe='/._-')


def write(page, text):
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(text.rstrip()+'\n', encoding='utf-8')


def table_header(path):
    if path.suffix.lower() not in ('.csv','.tsv'):
        return ''
    try:
        with path.open(encoding='utf-8-sig', newline='') as stream:
            names = next(csv.reader(stream, delimiter='\t' if path.suffix=='.tsv' else ','), [])
        return ', '.join(names[:8]) + (' …' if len(names)>8 else '')
    except (OSError,UnicodeError,csv.Error):
        return ''


def collect(repo):
    energy=repo/E
    records=[]
    # Do not catalogue texmf logos, private origins, metadata or old manuscript source sections.
    roots=[(repo/PARMA,'PARMA v0.15.1','paper-parma'),(repo/TIM,'TIM v0.3','paper-tim')]
    for topic in THEMES:
        root=energy/'evidence'/topic/'sources'
        if root.exists():
            for package in sorted(root.iterdir()):
                if package.is_dir(): roots.append((package,'Originale Evidence / Zusatzprüfung',topic+'--'+package.name))
    archive=energy/'archive/original-exports'
    if archive.exists():
        for package in sorted(archive.iterdir()):
            if package.is_dir(): roots.append((package,'Archiv: ursprüngliche Darstellungen','archive--'+package.name))
    unknown=[]
    for root,status,collection in roots:
        if not root.is_dir(): continue
        for p in sorted(root.rglob('*')):
            if not p.is_file() or p.is_symlink(): continue
            rel=p.relative_to(root).as_posix(); parts=rel.lower().split('/')
            if any(x in parts for x in ('texmf','metadata','provenance','.venv','records')): continue
            ext=p.suffix.lower(); kind=None
            if ext in FIG and (any(x in parts for x in ('figures','plots','previews','pictures')) or collection.startswith('archive--')):
                kind='figures'
            elif ext in TAB and (ext in ('.csv','.tsv','.ods','.xlsx','.xls') or any(x in parts for x in ('tables','generated'))):
                if ext=='.tex' and not (p.name.startswith('table') or 'tables' in parts): continue
                if ext=='.md' and 'tables' not in parts: continue
                kind='tables'
            if kind is None: continue
            topic=topic_for(p.as_posix())
            records.append({'topic':topic,'kind':kind,'status':status,'collection':collection,
                'path':p.relative_to(repo).as_posix(),'bytes':p.stat().st_size,'format':ext[1:],
                'label':TIM_LABELS.get(p.stem,p.stem.replace('_',' ')) if collection=='paper-tim' else p.stem.replace('_',' '),'header':table_header(p) if kind=='tables' else ''})
    # Table I is inline, not a generated table file; catalogue it explicitly.
    inline=repo/TIM/'sections/instrumentation.tex'
    if inline.is_file():
        records.append({'topic':'measurement-comparison','kind':'tables','status':'TIM v0.3',
            'collection':'paper-tim','path':inline.relative_to(repo).as_posix(),'bytes':inline.stat().st_size,
            'format':'tex','label':'Tab. I — Rollen der experimentellen Kohorten (inline)',
            'header':'Manuskripttabelle direkt im Instrumentierungsabschnitt'})
    for row in records:
        if row['collection']=='paper-tim':
            name=Path(row['path']).stem
            if (row['kind']=='figures' and name in TIM_LABELS) or name in ('jetson_reference','direct_repeatability','controlled','instrumentation'):
                row['usage']='Hauptabbildung / Haupttabelle'
            elif '/generated/' in row['path']:
                row['usage']='Vollständige Ergebnis- / Plotinputs'
            else:row['usage']='Zusatzdatei; nicht automatisch im Haupttext'
        elif row['collection']=='paper-parma':row['usage']='PARMA-Paket; Umfang siehe Quellenzuordnung'
        elif row['collection'].startswith('archive--'):row['usage']='Ursprüngliche Darstellung; nicht automatisch aktueller Befund'
        else:row['usage']='Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung'
    return records


def generate(repo):
    repo=Path(repo).resolve(); energy=repo/E
    records=collect(repo); created=[]
    def emit(p,text): write(p,text);created.append(p.relative_to(repo).as_posix())
    index=energy/'CATALOG.csv'
    with index.open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['topic','kind','status','collection','label','format','bytes','path','header','usage'])
        writer.writeheader();writer.writerows(records)
    created.append(index.relative_to(repo).as_posix())
    for topic,(title,description) in THEMES.items():
        topic_root=energy/'evidence'/topic
        for kind,heading in [('figures','Abbildungen'),('tables','Tabellen und Tabellendaten')]:
            here=topic_root/kind/'README.md'
            selected=[r for r in records if r['topic']==topic and r['kind']==kind and not r['collection'].startswith('archive--')]
            by=defaultdict(list)
            for row in selected:by[row['collection']].append(row)
            overview=f'# {heading} — {title}\n\n[Themenübersicht](../README.md) · [Gesamtkatalog](../../../CATALOG.md)\n\n'
            overview+='Die Dateien bleiben an ihrer eindeutigen Quelle. Dieser Ordner bietet anklickbare Katalogseiten statt weiterer PDF-/CSV-Kopien.\n\n'
            overview+='Aktuelle Manuskriptansichten stehen zuerst. Originalexporte sind separat bezeichnet; ein jüngeres Dateidatum macht sie nicht automatisch zur Papergrundlage.\n\n'
            for collection in sorted(by,key=lambda c:(0 if c=='paper-tim' else 1 if c=='paper-parma' else 2,c)):
                rows=by[collection];page=here.parent/(collection+'.md')
                overview+=f'- [{rows[0]["status"]} — {collection}]({page.name}) ({len(rows)} Dateien)\n'
                text=f'# {heading}: {collection}\n\n[Zurück](README.md)\n\n**Einordnung:** {rows[0]["status"]}.\n\n'
                if collection=='paper-tim':
                    text+=f'[Vollständige Zuordnung zu den TIM-Abbildungs-/Tabellennummern]({link(page,repo/TIM/"SOURCE_MAPPING.md")}).\n\n'
                elif collection=='paper-parma':
                    text+=f'[PARMA-Quellenzuordnung]({link(page,repo/PARMA/"SOURCE_MAPPING.md")}).\n\n'
                if kind=='figures':
                    grouped=defaultdict(list)
                    for r in rows:
                        grouped[str(Path(r['path']).with_suffix(''))].append(r)
                    for key,variants in grouped.items():
                        first=variants[0];text+='## '+first['label']+'\n\n'+first['usage']+'\n\n'
                        text+=' · '.join('['+r['format'].upper()+']('+link(page,repo/r['path'])+')' for r in variants)+'\n\n'
                        preview=next((r for ext in ('.png','.svg','.jpg','.jpeg','.webp') for r in variants if '.'+r['format']==ext),None)
                        if preview:
                            text+=f'<details><summary>Vorschau öffnen</summary>\n\n![{first["label"]}]({link(page,repo/preview["path"])})\n\n</details>\n\n'
                        text+='Quelle: `'+first['path'].rsplit('/',1)[0]+'`\n\n'
                else:
                    text+='| Datei | Format | Einordnung | Verfügbare Spalten (Auszug) |\n|---|---|---|---|\n'
                    for r in rows:
                        label=r['label'].replace('|','\\|');header=r['header'].replace('|','\\|')
                        text+=f'| [{label}]({link(page,repo/r["path"])}) | {r["format"].upper()} | {r["usage"]} | {header} |\n'
                    text+='\nCSV-Dateien können vollständige Run-/Paarwerte oder Plotinputs enthalten; sie sind nicht automatisch zusätzliche Tabellen im Manuskript.\n'
                emit(page,text)
            if not by:overview+='Noch keine passende Datei in diesem Bestand. Es werden keine fehlenden Ergebnisse erzeugt.\n'
            emit(here,overview)
        top=topic_root/'README.md'
        text=f'# {title}\n\n{description}\n\n'
        text+='| Einstieg | Inhalt |\n|---|---|\n| [Abbildungen](figures/README.md) | Formate, Vorschauen und eindeutige Quellen |\n| [Tabellen](tables/README.md) | Tabellenquellen, numerische Ausgaben und volle Paarwerte |\n| [Unveränderte Quellenpakete](sources/README.md) | Zugehörige Methoden und Provenienz |\n\n'
        text+='Die Katalogseiten verändern keine Messwerte. PDF, PNG und SVG derselben Abbildung werden gemeinsam angezeigt.\n'
        emit(top,text)
    # Archive gets a separate catalogue, never promoted as current paper evidence.
    archpage=energy/'archive/original-exports/README.md'
    text='# Ursprüngliche Abbildungs- und Tabellenexporte\n\n[Gesamtkatalog](../../CATALOG.md)\n\nDiese Bestände bleiben vollständig erhalten. Ihre Platzierung im Archiv bedeutet nicht, dass alle darin enthaltenen Ergebnisse fachlich ungültig sind. Für aktuelle Paperaussagen ist die Quellenzuordnung des jeweiligen Manuskripts maßgeblich.\n\n'
    for r in records:
        if r['collection'].startswith('archive--'):
            text+=f'- [{r["label"]} ({r["format"]})]({link(archpage,repo/r["path"])})\n'
    emit(archpage,text)
    catalog=energy/'CATALOG.md'
    text='# Abbildungen und Tabellen — Gesamtübersicht\n\n[Projektstart](README.md) · [Maschinenlesbarer Gesamtkatalog](CATALOG.csv)\n\n'
    text+='## Aktuelle Paper\n\n[PARMA v0.15.1](papers/parma-v0.15.1/manuscript/paper.pdf) · [TIM v0.3](papers/tim-v0.3/main.pdf) · [TIM-Quellenzuordnung mit Abbildungsnummern](papers/tim-v0.3/SOURCE_MAPPING.md)\n\n'
    text+='## Nach Fragestellung\n\n| Thema | Abbildungen | Tabellen und Daten |\n|---|---|---|\n'
    for topic,(title,_) in THEMES.items():
        nf=sum(r['topic']==topic and r['kind']=='figures' and not r['collection'].startswith('archive--') for r in records)
        nt=sum(r['topic']==topic and r['kind']=='tables' and not r['collection'].startswith('archive--') for r in records)
        text+=f'| [{title}](evidence/{topic}/README.md) | [{nf} Dateien](evidence/{topic}/figures/README.md) | [{nt} Dateien](evidence/{topic}/tables/README.md) |\n'
    text+='\nDie Zahlen zählen Dateien/Formate, nicht unabhängige Messungen oder nummerierte Manuskriptobjekte. Paneldateien können eine gemeinsame Abbildungsnummer besitzen.\n\n'
    text+='[Ältere Originalexporte](archive/original-exports/README.md) stehen getrennt. Fehlende Vorschaubilder werden nicht erfunden; das vorhandene PDF bleibt anklickbar.\n'
    emit(catalog,text)
    return records,created

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    args=parser.parse_args()
    rows,files=generate(args.repo)
    print(f'Katalog: {len(rows)} vorhandene Bild-/Tabellendateien, {len(files)} Indexdateien. Keine Daten verändert.')
