from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.xmlchemy import OxmlElement

OUT = "KAR_KHANE_KAGHAZSAZI_12_SLIDES_ANIMATED.pptx"
prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
C = {
 "navy": RGBColor(18,37,54), "navy2": RGBColor(29,57,75),
 "teal": RGBColor(27,153,139), "mint": RGBColor(204,239,229),
 "coral": RGBColor(235,111,92), "cream": RGBColor(248,246,239),
 "paper": RGBColor(255,253,247), "ink": RGBColor(34,48,58),
 "muted": RGBColor(100,117,126), "white": RGBColor(255,255,255),
 "pale": RGBColor(230,239,238), "green": RGBColor(83,155,117),
 "orange": RGBColor(227,151,78)
}
FONT = "Tahoma"

def rtl(p):
    p._p.get_or_add_pPr().set("rtl", "1")

def text(slide, value, x,y,w,h, size=17, color=None, bold=False, align=PP_ALIGN.RIGHT):
    box=slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf=box.text_frame; tf.clear(); tf.word_wrap=True
    tf.margin_left=tf.margin_right=Inches(.10)
    tf.margin_top=tf.margin_bottom=Inches(.06)
    tf.vertical_anchor=MSO_ANCHOR.MIDDLE
    for i,line in enumerate(str(value).split("\n")):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.alignment=align; rtl(p); p.space_after=Pt(4)
        r=p.add_run(); r.text=line
        r.font.name=FONT; r.font.size=Pt(size); r.font.bold=bold
        r.font.color.rgb=color or C["ink"]
    return box

def shape(slide,x,y,w,h,fill,round=True):
    typ=MSO_SHAPE.ROUNDED_RECTANGLE if round else MSO_SHAPE.RECTANGLE
    a=slide.shapes.add_shape(typ, Inches(x), Inches(y), Inches(w), Inches(h))
    a.fill.solid(); a.fill.fore_color.rgb=fill; a.line.fill.background()
    if round:
        try: a.adjustments[0]=.12
        except Exception: pass
    return a

def card(slide,x,y,w,h,title,body,accent,num):
    shape(slide,x,y,w,h,C["paper"])
    shape(slide,x+w-.13,y+.18,.07,h-.36,accent,False)
    text(slide,str(num),x+w-.75,y+.19,.43,.43,12,C["white"],True,PP_ALIGN.CENTER)
    text(slide,title,x+.2,y+.18,w-1.1,.48,18,C["navy"],True)
    text(slide,body,x+.22,y+.75,w-.48,h-.88,15,C["ink"])

def footer(slide,n):
    text(slide,"علوم ششم | کارخانهٔ کاغذسازی",.5,7.08,5,.22,9,C["muted"],False,PP_ALIGN.LEFT)
    a=slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(12.35), Inches(6.98), Inches(.42), Inches(.42))
    a.fill.solid(); a.fill.fore_color.rgb=C["teal"]; a.line.fill.background()
    text(slide,f"{n:02d}",12.35,6.98,.42,.42,10,C["white"],True,PP_ALIGN.CENTER)

def transition(slide):
    t=OxmlElement("p:transition"); t.set("spd","med")
    t.append(OxmlElement("p:fade")); slide._element.insert(1,t)

def newslide(n,section,title,subtitle=""):
    s=prs.slides.add_slide(prs.slide_layouts[6])
    s.background.fill.solid(); s.background.fill.fore_color.rgb=C["cream"]
    shape(s,0,0,13.333,.17,C["teal"],False)
    text(s,section,9.1,.42,3.7,.3,10,C["teal"],True)
    text(s,title,.65,.78,12,.65,27,C["navy"],True)
    if subtitle: text(s,subtitle,.7,1.43,11.9,.42,13,C["muted"])
    footer(s,n); transition(s)
    return s

# 1 — Cover
s=prs.slides.add_slide(prs.slide_layouts[6])
s.background.fill.solid(); s.background.fill.fore_color.rgb=C["navy"]
shape(s,0,0,13.333,.16,C["teal"],False)
shape(s,.8,1.05,3.05,4.8,C["navy2"])
shape(s,1.18,1.42,3.05,4.8,C["teal"])
shape(s,1.55,1.78,3.05,4.8,C["cream"])
text(s,"کاغذ",1.85,3.0,2.45,.7,28,C["navy"],True,PP_ALIGN.CENTER)
text(s,"از مادهٔ خام\nتا محصول نهایی",1.85,3.75,2.45,1.0,16,C["teal"],True,PP_ALIGN.CENTER)
text(s,"علوم تجربی پایهٔ ششم",5.1,1.4,7,.45,16,C["mint"],True)
text(s,"کارخانهٔ\nکاغذسازی",5.05,2.0,7.2,1.7,37,C["white"],True)
shape(s,5.1,4.05,1.2,.08,C["coral"],False)
text(s,"نگاهی به آهن، فلزها، اسیدها و بازیافت کاغذ",5.05,4.4,7.2,.65,17,C["mint"])
text(s,"بر اساس صفحات ۱۸ تا ۲۴ کتاب علوم ششم",5.05,6.25,7.2,.35,11,C["mint"])
transition(s)

# 2
s=newslide(2,"شروع درس","چرا کاغذ را در کارخانه تولید می‌کنیم؟","با افزایش جمعیت، مصرف سالانهٔ کاغذ در جهان بیشتر شده است.")
card(s,.75,2.15,5.75,3.6,"نیاز به تولید زیاد","برای پاسخ‌گویی به مصرف گسترده، باید میلیون‌ها تُن کاغذ در سال تولید شود.",C["teal"],1)
card(s,6.8,2.15,5.75,3.6,"روش صنعتی","روش‌های سنتی و دستی برای تولید این مقدار کافی نیستند؛ کارخانه‌ها تولید را در مقیاس بزرگ انجام می‌دهند.",C["coral"],2)
text(s,"پرسش آغازین: چه مواد و دستگاه‌هایی در کارخانهٔ کاغذسازی به کار می‌روند؟",1,6.1,11.3,.55,15,C["navy"],True,PP_ALIGN.CENTER)

# 3
s=newslide(3,"آهن در کارخانه","چرا آهن در کارخانهٔ کاغذسازی مهم است؟","فلز آهن در ساخت بخش‌های مختلف کارخانه کاربرد گسترده‌ای دارد.")
card(s,.75,2.15,3.85,3.7,"غلتک‌های بزرگ","برای صاف‌کردن خمیر و تبدیل آن به ورقه‌های نازک کاغذ.",C["teal"],1)
card(s,4.75,2.15,3.85,3.7,"مخزن‌های آهنی","برای نگهداری و آماده‌سازی خمیر کاغذ.",C["coral"],2)
card(s,8.75,2.15,3.85,3.7,"دستگاه‌های دیگر","مانند چوب‌خردکن، سرند و دیگ‌های خمیرسازی.",C["green"],3)
text(s,"آهن به دلیل استحکام و کاربردهای فراوان، در ساخت تجهیزات صنعتی استفاده می‌شود.",1,6.15,11.3,.45,14,C["navy"],True,PP_ALIGN.CENTER)

# 4
s=newslide(4,"ویژگی‌های آهن","آهن چه ویژگی‌هایی دارد؟","در کتاب، به چند ویژگی مهم آهن اشاره شده است.")
card(s,.75,2.15,5.75,3.65,"زنگ‌زدن","آهن در شرایط مناسب و در تماس با رطوبت و هوا می‌تواند زنگ بزند.",C["coral"],1)
card(s,6.8,2.15,5.75,3.65,"گداخته‌شدن","آهن در دمای بالا گداخته می‌شود و می‌توان آن را شکل داد.",C["teal"],2)
text(s,"فکر کنید: چرا برای خشک‌کردن خمیر کاغذ از غلتک‌های بزرگ آهنی استفاده می‌کنند؟",1,6.1,11.3,.55,15,C["navy"],True,PP_ALIGN.CENTER)

# 5
s=newslide(5,"آزمایش و مشاهده","سبک یا سنگین؟ سخت یا نرم؟","با مقایسهٔ آهن با چوب و پلاستیک می‌توان بعضی ویژگی‌ها را شناخت.")
card(s,.75,2.1,3.85,3.75,"مقایسهٔ وزن","قطعه‌هایی با شکل و اندازهٔ یکسان را روی دو کفهٔ ترازو مقایسه کنید.",C["teal"],1)
card(s,4.75,2.1,3.85,3.75,"مقایسهٔ سختی","با واردکردن ضربهٔ یکسان، میزان تغییر شکل مواد را بررسی کنید.",C["coral"],2)
card(s,8.75,2.1,3.85,3.75,"مقایسهٔ خراش","میزان مقاومت چوب، پلاستیک و آهن در برابر خراش را مقایسه کنید.",C["green"],3)
text(s,"نتیجه‌گیری را از مشاهده‌ها بنویسید؛ نه فقط از حدس اولیه.",1,6.15,11.3,.4,14,C["navy"],True,PP_ALIGN.CENTER)

# 6
s=newslide(6,"فلزها","آهن تنها فلز نیست!","در کتاب، فلزهای دیگری هم معرفی شده‌اند.")
card(s,.85,2.1,5.65,1.55,"آلومینیم","فلزی سبک و پرکاربرد.",C["teal"],1)
card(s,6.8,2.1,5.65,1.55,"مس","رسانای خوب جریان برق.",C["coral"],2)
card(s,.85,3.95,5.65,1.55,"طلا","فلزی ارزشمند و قابل شکل‌دهی.",C["orange"],3)
card(s,6.8,3.95,5.65,1.55,"سرب","سمی است؛ از تماس طولانی‌مدت با آن پرهیز می‌کنیم.",C["green"],4)
text(s,"این فلزها جامدند و جریان برق و گرما را هدایت می‌کنند.",1,6.25,11.3,.4,15,C["navy"],True,PP_ALIGN.CENTER)

# 7
s=newslide(7,"کاربرد فلزها","چرا برای هر وسیله از فلز متفاوتی استفاده می‌شود؟","انتخاب فلز به ویژگی‌های آن و کاربرد وسیله بستگی دارد.")
card(s,.75,2.15,3.85,3.65,"رسانایی","فلزهایی مانند مس برای انتقال جریان برق مناسب‌اند.",C["teal"],1)
card(s,4.75,2.15,3.85,3.65,"سبکی","آلومینیم در وسایلی به کار می‌رود که وزن کمتر اهمیت دارد.",C["coral"],2)
card(s,8.75,2.15,3.85,3.65,"استحکام","آهن برای ساخت بسیاری از دستگاه‌ها و سازه‌های مقاوم کاربرد دارد.",C["green"],3)
text(s,"پرسش: برای ساخت سیم برق، قابلمه و بدنهٔ خودرو چه ویژگی‌هایی مهم است؟",1,6.1,11.3,.55,15,C["navy"],True,PP_ALIGN.CENTER)

# 8
s=newslide(8,"اسیدها","اسیدها در تولید کاغذ و زندگی روزانه","در تولید خمیر کاغذ، علاوه بر آب اکسیژنه، اسید نیز وجود دارد.")
card(s,.75,2.15,5.75,3.6,"اسیدهای خوراکی","در بعضی خوراکی‌ها وجود دارند و معمولاً مزهٔ ترش دارند؛ مانند لیموترش و سرکه.",C["teal"],1)
card(s,6.8,2.15,5.75,3.6,"اسیدهای صنعتی","در صنایع کاربرد دارند؛ بعضی از آن‌ها مانند جوهرنمک خطرناک و سمی هستند.",C["coral"],2)
text(s,"کاغذ pH وسیله‌ای برای شناسایی اسیدی‌بودن مواد است.",1,6.15,11.3,.4,15,C["navy"],True,PP_ALIGN.CENTER)

# 9
s=newslide(9,"ایمنی","با اسیدهای صنعتی باید بسیار محتاط بود","نکتهٔ ایمنی کتاب را جدی بگیریم.")
card(s,.85,2.2,3.75,3.4,"لمس نکنیم","از تماس مستقیم با اسیدهای صنعتی خودداری کنیم.",C["coral"],1)
card(s,4.8,2.2,3.75,3.4,"بو نکنیم","برای شناخت ماده، آن را از نزدیک بو نکنیم.",C["orange"],2)
card(s,8.75,2.2,3.75,3.4,"نچشیم","اسید صنعتی هرگز نباید چشیده شود.",C["teal"],3)
text(s,"هر آزمایش مرتبط با مواد شیمیایی فقط با نظارت معلم و رعایت دستورهای ایمنی انجام می‌شود.",.9,6,11.6,.7,14,C["navy"],True,PP_ALIGN.CENTER)

# 10
s=newslide(10,"محیط زیست","فاضلاب کارخانه چرا خطرناک است؟","ورود فاضلاب کارخانه به رودخانه‌ها و مزارع می‌تواند به محیط زیست آسیب برساند.")
card(s,.8,2.2,5.65,3.5,"آب و خاک","آلودگی می‌تواند کیفیت آب و خاک را کاهش دهد و به جانداران آسیب بزند.",C["coral"],1)
card(s,6.85,2.2,5.65,3.5,"مسئولیت کارخانه","پساب صنعتی باید پیش از رهاسازی، به‌درستی مدیریت و تصفیه شود.",C["teal"],2)
text(s,"پرسش کتاب: چرا ورود فاضلاب کارخانه به رودخانه‌ها و مزارع آسیب می‌رساند؟",1,6.05,11.3,.55,15,C["navy"],True,PP_ALIGN.CENTER)

# 11
s=newslide(11,"بازیافت کاغذ","بازیافت؛ مصرف برق کمتر","کتاب مصرف برق برای تولید یک تُن کاغذ را مقایسه می‌کند.")
text(s,"تولید از تنهٔ درخت",7.2,2.1,4.7,.45,17,C["navy"],True)
shape(s,2,2.75,8.5,.55,C["pale"]); shape(s,2,2.75,8.5,.55,C["coral"])
text(s,"۱۴۰۰ کیلووات‌ساعت",2.1,2.78,8.3,.45,16,C["white"],True,PP_ALIGN.CENTER)
text(s,"تولید با بازیافت کاغذ باطله",7.2,4,4.7,.45,17,C["navy"],True)
shape(s,2,4.6,8.5,.55,C["pale"]); shape(s,2,4.6,5.1,.55,C["teal"])
text(s,"۸۴۰ کیلووات‌ساعت",2.1,4.63,8.3,.45,16,C["white"],True,PP_ALIGN.CENTER)
text(s,"در مقایسهٔ کتاب، بازیافت برای تولید یک تُن کاغذ برق کمتری مصرف می‌کند.",1,5.75,11.3,.65,15,C["navy"],True,PP_ALIGN.CENTER)

# 12
s=newslide(12,"جمع‌بندی","چه چیزهایی یاد گرفتیم؟","مرور نکته‌های اصلی صفحات ۱۸ تا ۲۴")
card(s,.75,2.05,5.75,1.55,"۱) آهن","در ساخت غلتک، مخزن و دستگاه‌های کارخانه کاربرد دارد.",C["teal"],1)
card(s,6.8,2.05,5.75,1.55,"۲) فلزها","مس، آلومینیم، طلا و سرب ویژگی‌های گوناگون دارند.",C["coral"],2)
card(s,.75,3.9,5.75,1.55,"۳) اسیدها","خوراکی و صنعتی‌اند؛ اسیدهای صنعتی خطرناک‌اند.",C["orange"],3)
card(s,6.8,3.9,5.75,1.55,"۴) بازیافت","در مثال کتاب، تولید با بازیافت برق کمتری مصرف می‌کند.",C["green"],4)
text(s,"سؤال پایانی: سه راه برای کاهش مصرف کاغذ در مدرسه نام ببرید.",1,6,11.3,.55,16,C["navy"],True,PP_ALIGN.CENTER)

prs.core_properties.title="کارخانهٔ کاغذسازی | علوم ششم"
prs.core_properties.subject="ارائهٔ ۱۲ اسلایدی بر اساس صفحات ۱۸ تا ۲۴ کتاب علوم ششم"
prs.core_properties.author="AR-CODEX"
prs.save(OUT)
print("Created", OUT)
