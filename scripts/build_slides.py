"""Build the editable MOE presentation from versioned JSON content."""
from __future__ import annotations
import json
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
C = {'bg':'101B2D','panel':'192A40','ink':'F5F7FB','muted':'ACBBD0','accent':'35DFC1','line':'34465F','soft':'23384F'}
# Calibri ships with common office suites, or is replaced there by a metric-compatible font, so the
# layout does not depend on a typeface the presenting machine may lack.
FONT = 'Calibri'

def color(name):
    return RGBColor.from_string(C.get(name, name))

def box(slide, x,y,w,h, fill='panel', line=None, radius=False):
    shape=slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid(); shape.fill.fore_color.rgb=color(fill)
    if line is None: shape.line.fill.background()
    else: shape.line.color.rgb=color(line)
    if radius:
        try: shape.adjustments[0]=0.12
        except (IndexError, AttributeError): pass
    return shape

def text(slide, value, x,y,w,h, size=20, bold=False, ink='ink', align=None, anchor=None):
    shape=slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf=shape.text_frame; tf.clear(); tf.word_wrap=True
    tf.margin_left=tf.margin_right=tf.margin_top=tf.margin_bottom=0
    if anchor is not None:tf.vertical_anchor=anchor
    for i,line in enumerate(value.split('\n')):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.text=line; p.font.name=FONT; p.font.size=Pt(size); p.font.bold=bold; p.font.color.rgb=color(ink)
        p.space_before=Pt(0); p.space_after=Pt(0)
        if align is not None:p.alignment=align
    return shape

def rule(slide,x1,y1,x2,y2,ink='line',width=1):
    sh=slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    sh.line.color.rgb=color(ink);sh.line.width=Pt(width)
    return sh

def arrow(slide,x,y,w=.25,h=.22,rotation=0):
    sh=slide.shapes.add_shape(MSO_SHAPE.CHEVRON,Inches(x),Inches(y),Inches(w),Inches(h))
    sh.fill.solid();sh.fill.fore_color.rgb=color('accent');sh.line.fill.background();sh.rotation=rotation;return sh

def header(slide,s,n):
    slide.background.fill.solid();slide.background.fill.fore_color.rgb=color('bg')
    text(slide,'MOE',.65,.27,1,.3,16,True,'accent')
    text(slide,s.get('eyebrow',''),1.55,.32,10.8,.25,10.5,True,'muted')
    rule(slide,.65,7.03,12.68,7.03)
    text(slide,'MAKER-ORCHESTRATED ENGINEERING',.65,7.14,6,.2,8.5,True,'muted')
    text(slide,f'0.3.0 WORKING DRAFT   /   {n:02d}',10.05,7.12,2.65,.25,9,False,'muted')
    if s['layout'] not in ('cover','closing'):
        text(slide,s['title'],.65,1.0,12,1.52,36,True)

def card(slide,x,y,w,h,title,body,title_size=21):
    box(slide,x,y,w,h,radius=True)
    box(slide,x+.2,y+.24,.28,.04,'accent')
    text(slide,title,x+.2,y+.45,w-.4,.76,title_size,True)
    text(slide,body,x+.2,y+1.27,w-.4,h-1.38,17,False,'muted')

def build():
    content=json.loads((ROOT/'presentations/slides.json').read_text(encoding='utf-8'))
    prs=Presentation();prs.slide_width=Inches(13.333333);prs.slide_height=Inches(7.5)
    prs.core_properties.title='Maker-Orchestrated Engineering | MOE 0.3.0'
    prs.core_properties.subject='Vendor-neutral engineering framework for human-agent collaboration'
    prs.core_properties.author='MOE Project'
    prs.core_properties.keywords='MOE, maker-orchestrated engineering, working draft'
    for n,s in enumerate(content,1):
        sl=prs.slides.add_slide(prs.slide_layouts[6]);header(sl,s,n);kind=s['layout']
        if kind in ('cover','closing'):
            for x,y,w in [(9.9,1.3,2.6),(10.4,1.8,1.6),(10.9,2.3,.6)]:
                sh=sl.shapes.add_shape(MSO_SHAPE.OVAL,Inches(x),Inches(y),Inches(w),Inches(w));sh.fill.background();sh.line.color.rgb=color('accent');sh.line.width=Pt(1.5)
            text(sl,s['title'],.78,1.65,9.6,3.4,49 if kind=='cover' else 46,True)
            text(sl,s['subtitle'],.82,5.27,11.6,.85,23,False,'muted')
            text(sl,s['tag'],.82,6.47,11.8,.3,12,True,'accent')
        elif kind in ('statement','definition'):
            text(sl,s['subtitle'],.69,2.82,11.9,.9,21,False,'muted')
            items=s['cards'];w=(12.03-.24*(len(items)-1))/len(items)
            for i,item in enumerate(items):card(sl,.65+i*(w+.24),4.15,w,2.35,item['title'],item['body'])
        elif kind=='split':
            for x,key in [(.65,'left'),(6.8,'right')]:
                box(sl,x,2.95,5.87,3.67,radius=True)
                text(sl,s[key+'_title'],x+.3,3.24,5.2,.5,23,True,'accent')
                for i,item in enumerate(s[key]):
                    box(sl,x+.32,4.02+i*.51,.06,.06,'accent')
                    text(sl,item,x+.56,3.92+i*.51,4.95,.43,18)
        elif kind=='principles':
            for i,(num,title,body) in enumerate(s['items']):
                col=i%2;row=i//2;x=.65+col*6.18;y=2.49+row*1.04
                text(sl,num,x,y,.52,.45,22,True,'accent')
                text(sl,title,x+.7,y,5.3,.42,21,True)
                text(sl,body,x+.7,y+.46,5.3,.37,16,False,'muted')
        elif kind=='layers':
            for i,(title,body) in enumerate(s['layers']):
                y=2.63+i*.72;box(sl,.65,y,12.03,.59,'panel');box(sl,.65,y,.05,.59,'accent')
                text(sl,title,.88,y+.13,3.05,.35,17,True)
                text(sl,body,4.07,y+.13,8.28,.35,16,False,'muted')
        elif kind=='loop':
            for i,(title,body) in enumerate(s['steps']):
                row=0 if i<3 else 1;col=i if i<3 else 5-i;x=.65+col*4.1;y=2.83+row*1.51
                box(sl,x,y,3.82,1.25,radius=True)
                text(sl,f'{i+1:02d}',x+.2,y+.18,.55,.38,18,True,'accent')
                text(sl,title,x+.84,y+.16,2.75,.42,22,True)
                text(sl,body,x+.22,y+.73,3.4,.4,16,False,'muted')
                if i in (0,1):arrow(sl,x+3.88,y+.48,.15,.22)
                if i in (3,4):arrow(sl,x-.22,y+.48,.15,.22,180)
            # Close the loop: Orchestrate down to Prove, and Learn back up to Define.
            arrow(sl,10.685,4.1,.15,.22,90);arrow(sl,2.485,4.1,.15,.22,270)
            text(sl,s['subtitle'],.7,6.25,12,.48,18,False,'muted')
        elif kind=='contracts':
            for i,(title,body) in enumerate(s['items']):
                y=2.66+i*.61
                text(sl,f'{i+1:02d}',.7,y,.5,.4,17,True,'accent')
                text(sl,title,1.43,y,3.45,.4,19,True)
                text(sl,body,5.1,y,7.4,.43,18,False,'muted')
                rule(sl,1.4,y+.47,12.5,y+.47)
            text(sl,s['subtitle'],.7,6.22,12,.43,18,True,'accent')
        elif kind=='roles':
            for i,(title,body) in enumerate(s['items']):
                x=.65+(i%3)*4.1;y=2.88+(i//3)*1.74;box(sl,x,y,3.82,1.5,radius=True)
                text(sl,title,x+.22,y+.2,3.38,.4,21,True,'accent')
                text(sl,body,x+.22,y+.78,3.38,.53,17,False,'muted')
        elif kind=='architecture':
            text(sl,s['subtitle'],.7,2.55,12,.8,20,False,'muted')
            for i,title in enumerate(s['nodes']):
                x=.65+i*3.07;box(sl,x,3.75,2.81,1.3,radius=True)
                text(sl,title,x+.23,3.75,2.35,1.3,21,True,anchor=MSO_ANCHOR.MIDDLE)
                if i<3:arrow(sl,x+2.85,4.27,.17,.25)
            box(sl,.65,5.7,12.03,.69,'soft')
            text(sl,s['bottom'],.87,5.91,11.6,.38,16,False,'muted')
        elif kind=='evidence':
            for i,(title,body) in enumerate(s['items']):
                y=2.75+i*.68;text(sl,f'{i+1:02d}',.7,y,.5,.42,18,True,'accent')
                text(sl,title,1.5,y,2.1,.42,21,True);text(sl,body,3.6,y,9,.48,18,False,'muted')
            text(sl,s['subtitle'],.7,6.13,12,.55,19,True,'accent')
        elif kind=='autonomy':
            for i,(level,title,body) in enumerate(s['rows']):
                y=2.77+i*.73;box(sl,.65,y,12.03,.6,'panel')
                text(sl,level,.88,y+.12,.7,.35,18,True,'accent')
                text(sl,title,1.8,y+.12,3.0,.35,18,True)
                text(sl,body,5.0,y+.12,7.4,.38,17,False,'muted')
            text(sl,s['subtitle'],.7,6.17,12,.48,18,False,'muted')
        elif kind=='profiles':
            for i,item in enumerate(s['cards']):
                x=.65+(i%2)*6.14;y=2.72+(i//2)*1.83;box(sl,x,y,5.89,1.63,radius=True)
                text(sl,item['title'],x+.23,y+.23,5.4,.41,21,True,'accent')
                text(sl,item['body'],x+.23,y+.86,5.4,.58,17,False,'muted')
        elif kind=='example':
            for i,(title,body) in enumerate(s['steps']):
                y=2.7+i*.62;text(sl,title,.75,y,2.0,.4,20,True,'accent');text(sl,body,2.9,y,9.65,.48,18)
            text(sl,s['subtitle'],.75,6.3,11.9,.43,16,False,'muted')
        elif kind=='pilot':
            for i,(title,body) in enumerate(s['steps']):
                x=.65+i*2.44;box(sl,x,3.05,2.25,2.58,radius=True)
                text(sl,f'{i+1:02d}',x+.2,3.27,1,.43,23,True,'accent')
                text(sl,title,x+.2,3.96,1.88,.42,21,True)
                text(sl,body,x+.2,4.59,1.88,.86,16,False,'muted')
            text(sl,s['subtitle'],.7,6.18,12,.48,19,False,'muted')
        elif kind=='metrics':
            for i,item in enumerate(s['cards']):
                x=.65+(i%3)*4.1;y=2.96+(i//3)*1.68;box(sl,x,y,3.82,1.46,radius=True)
                text(sl,item['title'],x+.22,y+.19,3.37,.4,21,True,'accent')
                text(sl,item['body'],x+.22,y+.78,3.37,.54,16.5,False,'muted')
        elif kind=='conformance':
            for i,item in enumerate(s['cards']):card(sl,.65+i*4.1,3.05,3.82,2.6,item['title'],item['body'],19)
            text(sl,s['subtitle'],.7,6.15,12,.6,18,False,'muted')
        elif kind=='roadmap':
            for i,(title,body) in enumerate(s['steps']):
                y=2.81+i*.71;text(sl,title,.75,y,2.2,.45,21,True,'accent');text(sl,body,3.0,y,9.5,.51,19,False,'muted')
            text(sl,s['subtitle'],.75,6.17,11.9,.55,17,False,'muted')
        elif kind=='sources':
            for i,(num,title,url) in enumerate(s['sources']):
                y=2.32+i*.57;text(sl,num,.75,y,.4,.4,17,True,'accent');text(sl,title,1.35,y,7.25,.4,17,True);text(sl,url,8.75,y,3.85,.46,13.5,False,'muted')
            text(sl,s['subtitle'],.75,6.33,11.9,.42,15,False,'muted')
        else: raise ValueError(f'Unknown layout {kind}')
        sl.notes_slide.notes_text_frame.text=s['notes']
    OUT.mkdir(exist_ok=True)
    path=OUT/'MOE_Framework_v0.3.pptx';prs.save(path);print(path)
    notes='# MOE presentation: speaker notes\n\nMOE 0.3.0 working draft.\n'
    for i,item in enumerate(content,1):
        title=item['title'].replace('\n',' ')
        notes+=f'\n## {i:02d}. {title}\n\n'+item['notes']+'\n'
    (OUT/'MOE_Speaker_Notes.md').write_text(notes,encoding='utf-8')

if __name__=='__main__':build()
