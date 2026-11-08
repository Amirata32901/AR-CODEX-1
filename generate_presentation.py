from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

prs=Presentation()
prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
BG=RGBColor(12,10,22); PANEL=RGBColor(29,24,47); PURPLE=RGBColor(151,103,255)
YELLOW=RGBColor(255,213,74); WHITE=RGBColor(248,245,255); MUTED=RGBColor(190,182,209); DARK=RGBColor(20,16,33)
blank=prs.slide_layouts[6]
def bg(s):
    s.background.fill.solid(); s.background.fill.fore_color.rgb=BG
def sh(s,x,y,w,h,c,line=None,oval=False):
    z=s.shapes.add_shape(MSO_SHAPE.OVAL if oval else MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    z.fill.solid(); z.fill.fore_color.rgb=c
    if line: z.line.color.rgb=line
    else: z.line.fill.background()
def tx(s,t,x,y,w,h,sz=20,c=WHITE,b=False,a=PP_ALIGN.RIGHT):
    z=s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    f=z.text_frame; f.clear(); f.word_wrap=True; f.vertical_anchor=MSO_ANCHOR.MIDDLE
    f.margin_left=Inches(.07); f.margin_right=Inches(.07)
    p=f.paragraphs[0]; p.text=t; p.alignment=a; p.font.name="Arial"; p.font.size=Pt(sz); p.font.bold=b; p.font.color.rgb=c
    p._p.get_or_add_pPr().set('rtl','1')
def slide(k,t,sub):
    s=prs.slides.add_slide(blank); bg(s); sh(s,-.6,-.8,2.5,2.5,PANEL,oval=True); sh(s,12,6,2,2,PANEL,oval=True)
    tx(s,k,9.4,.28,3.3,.35,11,YELLOW,True); tx(s,t,1,.72,11.3,.8,30,WHITE,True)
    tx(s,sub,1,1.55,11.3,.5,15,MUTED); sh(s,10.8,2.2,.9,.05,PURPLE)
    tx(s,f"AMIRATA  •  {len(prs.slides):02d}",.45,7.08,3,.2,8,MUTED,False,PP_ALIGN.LEFT)
    return s
s=prs.slides.add_slide(blank); bg(s); sh(s,9.6,-1.2,4.7,4.7,PANEL,oval=True); sh(s,-1.1,5.6,3,3,PANEL,oval=True); sh(s,10.8,4.9,1.1,1.1,PURPLE,oval=True)
tx(s,"یک معرفی کوتاه",8.7,.8,3.5,.5,15,YELLOW,True); tx(s,"سلام، من",5.9,1.7,5.7,.8,34,WHITE,True); tx(s,"امیرعطا هستم",3,2.45,8.7,1.1,48,PURPLE,True)
tx(s,"علاقه‌مند به فناوری، طراحی و ساختن ایده‌های تازه",1.6,3.8,10,.7,19,MUTED,False,PP_ALIGN.CENTER)
sh(s,4.6,5.2,4.1,.65,YELLOW); tx(s,"خلاقیت  |  یادگیری  |  ساختن",4.7,5.25,3.9,.5,14,DARK,True,PP_ALIGN.CENTER); tx(s,"AMIRATA  •  2026",.5,7.05,3,.2,9,MUTED,False,PP_ALIGN.LEFT)
s=slide("01  /  درباره من","همیشه یک ایده تازه دارم","من از یاد گرفتن و تبدیل ایده‌ها به پروژه‌های واقعی لذت می‌برم.")
tx(s,"من امیرعطا هستم؛ به دنیای فناوری و طراحی دیجیتال علاقه دارم. دوست دارم چیزهای جدید را امتحان کنم، مهارت‌هایم را توسعه بدهم و با هر پروژه تجربه بیشتری به دست بیاورم.",1.2,2.55,10.8,1.5,22)
for i,(t,d) in enumerate([("کنجکاوی","پرسیدن و کشف کردن"),("خلاقیت","ساختن راه‌حل‌های تازه"),("پیشرفت","یادگیری با تمرین")]):
    x=1.1+i*3.8; sh(s,x,4.65,3.25,1.15,PANEL,PURPLE if i==1 else None); tx(s,t,x+.15,4.75,2.95,.4,18,YELLOW,True,PP_ALIGN.CENTER); tx(s,d,x+.15,5.18,2.95,.4,12,MUTED,False,PP_ALIGN.CENTER)
s=slide("02  /  علاقه‌مندی‌ها","دنیای مورد علاقه من","چند حوزه که دوست دارم در آن‌ها تجربه کسب کنم.")
for i,(t,d) in enumerate([("طراحی وب","ساخت وب‌سایت‌های جذاب و کاربردی"),("برنامه‌نویسی","حل مسئله و ساخت ابزارهای کوچک"),("بازی‌سازی","طراحی محیط و تجربه‌های تعاملی"),("مدل‌سازی سه‌بعدی","ساخت اشیا و صحنه‌های دیجیتال")]):
    col=i%2; row=i//2; x=1.1+col*5.7; y=2.65+row*1.65; sh(s,x,y,5.1,1.25,PANEL); tx(s,f"0{i+1}",x+4.45,y+.12,.45,.35,12,YELLOW,True,PP_ALIGN.CENTER); tx(s,t,x+.25,y+.12,4,.4,18,WHITE,True); tx(s,d,x+.25,y+.58,4.5,.42,12,MUTED)
s=slide("03  /  پروژه‌ها","چیزهایی که ساخته‌ام","هر پروژه فرصتی برای یادگیری و بهتر شدن است.")
for i,(t,d) in enumerate([("Golden Mug","تجربه طراحی و توسعه فروشگاه اینترنتی ماگ و فلاسک."),("بازی‌سازی با Godot","ساخت محیط‌های بازی و تمرین کار با صحنه‌ها و دوربین."),("مدل‌سازی با Blender","ساخت و آماده‌سازی مدل‌های سه‌بعدی برای پروژه‌های دیجیتال.")]):
    x=1+i*3.85; sh(s,x,2.8,3.35,2.35,PANEL,PURPLE if i==0 else None); tx(s,f"PROJECT 0{i+1}",x+.2,3.02,2.95,.3,10,YELLOW,True,PP_ALIGN.LEFT); tx(s,t,x+.2,3.45,2.95,.5,18,WHITE,True); tx(s,d,x+.2,4.05,2.95,.85,12,MUTED)
s=slide("04  /  ابزارها","ابزارهایی که با آن‌ها کار می‌کنم","در حال تمرین و یادگیری این ابزارها و فناوری‌ها هستم.")
for i,t in enumerate(["Python","HTML","CSS","JavaScript","Blender","Godot","طراحی رابط کاربری","مدل‌سازی سه‌بعدی"]):
    col=i%4; row=i//4; x=1+col*2.9; y=2.9+row*1.25; sh(s,x,y,2.45,.72,PANEL,PURPLE if i in (0,4) else None); tx(s,t,x+.1,y+.08,2.25,.52,15,YELLOW if i in (0,4) else WHITE,True,PP_ALIGN.CENTER)
s=slide("05  /  روش کار","چطور پیش می‌روم؟","از یک ایده کوچک تا یک خروجی قابل نمایش.")
for i,(n,t,d) in enumerate([("۱","ایده‌پردازی","انتخاب موضوع و مشخص کردن هدف"),("۲","یادگیری","پیدا کردن روش‌ها و ابزارهای مناسب"),("۳","ساخت و آزمایش","پیاده‌سازی، بررسی و اصلاح"),("۴","بهبود","گرفتن بازخورد و بهتر کردن نتیجه")]):
    x=.9+i*3.1; sh(s,x+.78,2.8,.72,.72,PURPLE if i%2==0 else YELLOW,oval=True); tx(s,n,x+.85,2.88,.58,.52,17,WHITE if i%2==0 else DARK,True,PP_ALIGN.CENTER); tx(s,t,x,3.75,2.3,.45,16,WHITE,True,PP_ALIGN.CENTER); tx(s,d,x,4.25,2.3,.8,11,MUTED,False,PP_ALIGN.CENTER)
s=slide("06  /  هدف‌ها","مسیر من ادامه دارد","هنوز چیزهای زیادی برای یاد گرفتن و ساختن وجود دارد.")
tx(s,"می‌خواهم پروژه‌های خلاقانه‌تر و کامل‌تری بسازم، در برنامه‌نویسی و طراحی تجربه بیشتری کسب کنم و ایده‌هایم را به محصولاتی تبدیل کنم که دیگران هم بتوانند از آن‌ها استفاده کنند.",1.25,2.6,10.7,1.5,22)
sh(s,3.5,4.7,6.3,.8,PANEL,PURPLE); tx(s,"هر پروژه، یک قدم رو به جلوست.",3.7,4.82,5.9,.55,18,YELLOW,True,PP_ALIGN.CENTER)
s=prs.slides.add_slide(blank); bg(s); sh(s,9.8,-1.3,4.5,4.5,PANEL,oval=True); sh(s,-1,5.6,3,3,PANEL,oval=True)
tx(s,"ممنون از توجه شما",2,1.6,9.3,1,38,WHITE,True,PP_ALIGN.CENTER); tx(s,"این تازه شروع ماجراست.",2,2.75,9.3,.8,27,PURPLE,True,PP_ALIGN.CENTER); tx(s,"امیرعطا  |  خلاقیت، یادگیری و ساختن",2,3.9,9.3,.55,17,MUTED,False,PP_ALIGN.CENTER); sh(s,5.2,5.15,2.9,.13,YELLOW)
prs.core_properties.title="معرفی امیرعطا"; prs.core_properties.subject="ارائه معرفی شخصی"; prs.core_properties.author="Amirata"
prs.save("Amirata_Introduction.pptx")
