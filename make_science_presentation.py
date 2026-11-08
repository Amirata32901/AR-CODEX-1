from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.xmlchemy import OxmlElement
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.text import MSO_AUTO_SIZE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]

BG = RGBColor(10, 18, 34)
PANEL = RGBColor(20, 34, 55)
PANEL2 = RGBColor(27, 45, 68)
WHITE = RGBColor(245, 248, 252)
MUTED = RGBColor(178, 194, 211)
TEAL = RGBColor(42, 207, 190)
GREEN = RGBColor(103, 211, 132)
YELLOW = RGBColor(255, 205, 87)
BLUE = RGBColor(75, 164, 235)
PINK = RGBColor(238, 126, 173)
DARK = RGBColor(8, 14, 26)

def set_rtl(p):
    p.alignment = PP_ALIGN.RIGHT
    pPr = p._p.get_or_add_pPr()
    pPr.set('rtl', '1')

def add_text(slide, text, x, y, w, h, size=20, color=WHITE, bold=False,
             align='right', font='Tahoma', margin=0.06):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = Inches(margin)
    tf.margin_right = Inches(margin)
    tf.margin_top = Inches(margin)
    tf.margin_bottom = Inches(margin)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    for i, line in enumerate(str(text).split('\n')):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        p.font.name = font
        p.font.size = Pt(size)
        p.font.bold = bold
        p.font.color.rgb = color
        p.space_after = Pt(5)
        if align == 'right':
            set_rtl(p)
        elif align == 'center':
            p.alignment = PP_ALIGN.CENTER
        else:
            p.alignment = PP_ALIGN.LEFT
        for r in p.runs:
            r.font.name = font
            rPr = r._r.get_or_add_rPr()
            rPr.set('lang', 'fa-IR')
            rPr.set('rtl', '1' if align == 'right' else '0')
    return box

def rect(slide, x, y, w, h, fill=PANEL, radius=True, line=None):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    sh = slide.shapes.add_shape(shape_type, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    sh.line.fill.background() if line is None else None
    if line:
        sh.line.color.rgb = line
        sh.line.width = Pt(1.2)
    if radius:
        try:
            sh.adjustments[0] = 0.12
        except Exception:
            pass
    return sh

def circle(slide, x, y, d, fill):
    sh = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(d), Inches(d))
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    sh.line.fill.background()
    return sh

def line(slide, x1, y1, x2, y2, color=TEAL, width=2):
    sh = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    sh.line.color.rgb = color
    sh.line.width = Pt(width)
    return sh

def base(title, subtitle, n, accent=TEAL):
    s = prs.slides.add_slide(blank)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = BG
    # soft decorative bars
    rect(s, 0.0, 0.0, 13.333, 0.12, accent, False)
    circle(s, 11.95, 0.48, 0.22, accent)
    add_text(s, 'علوم ششم  |  از طبیعت تا کاغذ', 8.2, 0.34, 4.4, 0.35, 11, MUTED, True)
    add_text(s, title, 0.7, 0.85, 11.9, 0.72, 28, WHITE, True)
    add_text(s, subtitle, 0.75, 1.55, 11.7, 0.45, 13, MUTED, False)
    line(s, 0.75, 2.08, 12.55, 2.08, PANEL2, 1)
    add_text(s, f'{n:02d}  /  ۱۱', 0.72, 7.05, 2.0, 0.22, 9, MUTED, False, 'left')
    add_text(s, 'یادگیری با نگاه علمی', 9.8, 7.02, 2.7, 0.25, 9, accent, True)
    return s

def card(s, x, y, w, h, title, body, accent=TEAL, title_size=17, body_size=13):
    rect(s, x, y, w, h, PANEL, True)
    rect(s, x+w-0.10, y+0.18, 0.06, h-0.36, accent, False)
    add_text(s, title, x+0.18, y+0.12, w-0.42, 0.42, title_size, accent, True)
    add_text(s, body, x+0.18, y+0.62, w-0.42, h-0.76, body_size, WHITE, False)
    
def bullet_list(s, items, x, y, w, h, accent=TEAL, size=16):
    step = h / max(1, len(items))
    for i, item in enumerate(items):
        yy = y + i*step
        circle(s, x+w-0.20, yy+0.15, 0.10, accent)
        add_text(s, item, x, yy, w-0.32, step-0.02, size, WHITE, False)

def tree_icon(s, x, y, scale=1.0):
    rect(s, x+0.37*scale, y+0.75*scale, 0.22*scale, 0.85*scale, RGBColor(151, 103, 65), False)
    circle(s, x+0.02*scale, y+0.18*scale, 0.78*scale, GREEN)
    circle(s, x+0.45*scale, y+0.02*scale, 0.78*scale, RGBColor(74, 184, 111))
    circle(s, x+0.62*scale, y+0.38*scale, 0.64*scale, RGBColor(91, 196, 121))

def paper_icon(s, x, y, scale=1.0, accent=TEAL):
    sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(1.0*scale), Inches(1.28*scale))
    sh.fill.solid(); sh.fill.fore_color.rgb = RGBColor(238, 244, 249)
    sh.line.color.rgb = accent; sh.line.width = Pt(2)
    for j in range(4):
        line(s, x+0.18*scale, y+(0.35+0.19*j)*scale, x+0.80*scale, y+(0.35+0.19*j)*scale, RGBColor(105, 130, 150), 1)

def recycle_icon(s, x, y, scale=1.0):
    # three arrow-like chevrons arranged around a center
    for xx, yy, rot, col in [(x+0.32*scale,y,0,TEAL),(x+0.72*scale,y+0.52*scale,120,GREEN),(x-0.06*scale,y+0.52*scale,240,YELLOW)]:
        sh=s.shapes.add_shape(MSO_SHAPE.CHEVRON, Inches(xx), Inches(yy), Inches(0.62*scale), Inches(0.34*scale))
        sh.rotation=rot; sh.fill.solid(); sh.fill.fore_color.rgb=col; sh.line.fill.background()
    circle(s, x+0.38*scale, y+0.40*scale, 0.25*scale, PANEL)

# 1 Cover
s = prs.slides.add_slide(blank)
s.background.fill.solid(); s.background.fill.fore_color.rgb = BG
rect(s, 0, 0, 13.333, 0.14, TEAL, False)
circle(s, 10.8, 1.0, 1.45, RGBColor(20, 68, 82))
circle(s, 11.7, 1.55, 0.82, GREEN)
tree_icon(s, 9.45, 3.05, 1.35)
paper_icon(s, 11.25, 3.2, 1.0, YELLOW)
add_text(s, 'پاورپوینت علوم پایه ششم', 6.0, 1.12, 5.7, 0.45, 17, TEAL, True)
add_text(s, 'از طبیعت\nتا کاغذ', 4.0, 1.75, 7.7, 1.65, 38, WHITE, True)
add_text(s, 'مواد طبیعی و مصنوعی، ساخت کاغذ و بازیافت', 3.7, 3.55, 7.9, 0.62, 18, MUTED, False)
rect(s, 4.8, 4.55, 6.5, 0.72, PANEL, True)
add_text(s, 'از یک درخت تا برگه‌ای که روی آن می‌نویسیم', 5.0, 4.64, 6.1, 0.48, 16, YELLOW, True, 'center')
add_text(s, '۱۱ اسلاید آموزشی', 5.3, 6.55, 3.0, 0.35, 12, MUTED, False, 'center')

# 2 Preserving information
s = base('انسان‌ها در گذشته چگونه اطلاعات را نگه می‌داشتند؟',
         'پیش از رواج کاغذ، مردم از مواد گوناگون برای ثبت نوشته‌ها و تصویرها استفاده می‌کردند.', 2, YELLOW)
card(s, 8.7, 2.35, 3.75, 1.45, 'سنگ و دیوار غار', 'نقاشی‌ها و نشانه‌ها روی سنگ یا دیوارهٔ غار ثبت می‌شدند.', YELLOW, 16, 12)
card(s, 4.75, 2.35, 3.65, 1.45, 'چوب و پوست', 'برای نوشتن یا نگهداری نوشته‌ها از سطح چوب و پوست جانوران استفاده می‌شد.', TEAL, 16, 12)
card(s, 0.85, 2.35, 3.6, 1.45, 'سفال و مواد دیگر', 'برخی نوشته‌ها روی لوح‌های گِلی یا سفالی باقی می‌ماندند.', PINK, 16, 12)
rect(s, 1.0, 4.25, 11.4, 1.55, PANEL2, True)
add_text(s, 'چرا به روش‌های بهتر نیاز بود؟', 7.0, 4.42, 4.9, 0.4, 18, YELLOW, True)
add_text(s, 'با زیاد شدن دانش و جمعیت، نگهداری و جابه‌جایی اطلاعات اهمیت بیشتری پیدا کرد. انسان‌ها به دنبال وسیله‌ای سبک‌تر و مناسب‌تر برای نوشتن بودند.', 1.35, 4.92, 10.45, 0.65, 15, WHITE)
add_text(s, 'نکته: هر ماده‌ای که برای ثبت اطلاعات استفاده می‌شد، مزایا و محدودیت‌های خودش را داشت.', 1.1, 6.05, 11.0, 0.45, 12, MUTED)

# 3 Natural and artificial
s = base('مواد طبیعی و مواد مصنوعی',
         'مواد را می‌توان از نظر چگونگی به‌دست‌آمدن به دو گروه کلی تقسیم کرد.', 3, GREEN)
card(s, 6.85, 2.35, 5.55, 3.55, 'مواد طبیعی', '• در طبیعت یافت می‌شوند.\n• نمونه‌ها: چوب، پنبه، ماسه، سنگ آهن و نفت خام.\n• بعضی از آن‌ها پس از جداشدن یا پاک‌سازی، آمادهٔ استفاده می‌شوند.', GREEN, 19, 16)
card(s, 0.95, 2.35, 5.55, 3.55, 'مواد مصنوعی', '• انسان آن‌ها را با تغییر مواد اولیه و فرایندهای گوناگون می‌سازد.\n• نمونه‌ها: پلاستیک، لاستیک، مداد رنگی و بسیاری از وسایل روزمره.', BLUE, 19, 16)
add_text(s, 'یادت باشد: مصنوعی بودن به معنی بی‌ارتباط بودن با طبیعت نیست؛ بسیاری از مواد مصنوعی از مواد طبیعی ساخته می‌شوند.', 1.1, 6.12, 11.2, 0.48, 13, YELLOW, True)

# 4 Paper type
s = base('کاغذ طبیعی است یا مصنوعی؟',
         'کاغذ یک مادهٔ ساخته‌شده به دست انسان است که مواد اولیهٔ آن معمولاً از گیاهان به دست می‌آید.', 4, TEAL)
paper_icon(s, 9.7, 2.75, 1.55, TEAL)
tree_icon(s, 7.7, 3.15, 1.05)
card(s, 0.95, 2.4, 6.0, 1.35, 'مواد اولیه', 'چوب درختان و بعضی الیاف گیاهی مانند پنبه می‌توانند در تهیهٔ کاغذ به کار بروند.', GREEN, 17, 13)
card(s, 0.95, 4.0, 6.0, 1.35, 'چرا کاغذ مهم است؟', 'برای کتاب، دفتر، روزنامه، نقشه، بسته‌بندی و بسیاری از کارهای روزانه استفاده می‌شود.', YELLOW, 17, 13)
add_text(s, 'پس کاغذ را می‌توان ماده‌ای مصنوعی دانست که از مواد اولیهٔ طبیعی ساخته می‌شود.', 1.05, 5.95, 11.2, 0.5, 16, WHITE, True, 'center')

# 5 From tree to paper
s = base('از درخت تا کاغذ؛ مسیر تولید',
         'در کارخانه، چوب طی چند مرحله به خمیر تبدیل می‌شود و سپس ورقه‌های کاغذ شکل می‌گیرند.', 5, GREEN)
steps = [
 ('۱','برداشت برنامه‌ریزی‌شده','تنهٔ درختان در چارچوب مدیریت درست جنگل آماده می‌شود.'),
 ('۲','حمل چوب','چوب‌ها به کارخانه منتقل می‌شوند.'),
 ('۳','پوست‌گیری','پوست تنه جدا می‌شود.'),
 ('۴','خردکردن','چوب به قطعه‌های کوچک یا تراشه تبدیل می‌شود.'),
 ('۵','ساخت خمیر','الیاف چوب از هم جدا و با آب مخلوط می‌شوند.'),
 ('۶','شکل‌دهی و خشک‌کردن','خمیر به صورت ورقه درمی‌آید، فشرده و خشک می‌شود.')
]
for i,(num,title,body) in enumerate(steps):
    col=i%3; row=i//3
    x=8.55-col*3.9; y=2.38+row*1.82
    rect(s,x,y,3.55,1.48,PANEL,True)
    circle(s,x+2.92,y+0.18,0.42,[GREEN,TEAL,YELLOW,BLUE,PINK,GREEN][i])
    add_text(s,num,x+2.94,y+0.18,0.38,0.4,13,DARK,True,'center')
    add_text(s,title,x+0.15,y+0.18,2.65,0.38,15,[GREEN,TEAL,YELLOW,BLUE,PINK,GREEN][i],True)
    add_text(s,body,x+0.16,y+0.62,3.12,0.68,11,WHITE)
add_text(s, 'در پایان، کاغذها برش می‌خورند و برای مصرف آماده می‌شوند.', 1.0, 6.35, 11.4, 0.35, 14, YELLOW, True, 'center')

# 6 Why wood and fibers
s = base('چرا چوب برای ساخت کاغذ مناسب است؟',
         'چوب دارای الیاف گیاهی است؛ این الیاف پس از آماده‌سازی می‌توانند به هم پیوند بخورند و ورقه بسازند.', 6, YELLOW)
tree_icon(s, 9.8, 2.85, 1.25)
paper_icon(s, 7.5, 3.0, 1.25, YELLOW)
card(s, 0.95, 2.45, 5.8, 1.45, 'تراشه‌های چوب', 'خردکردن چوب باعث می‌شود آماده‌سازی آن در کارخانه آسان‌تر شود.', TEAL, 17, 13)
card(s, 0.95, 4.15, 5.8, 1.45, 'خمیر کاغذ', 'خمیر، مخلوطی از الیاف و آب است که می‌توان آن را روی توری پخش کرد.', GREEN, 17, 13)
add_text(s, 'با گرفتن آب و خشک‌شدن خمیر، الیاف کنار هم می‌مانند و ورقهٔ کاغذ شکل می‌گیرد.', 1.0, 6.0, 11.3, 0.48, 15, WHITE, True, 'center')

# 7 Uses and history
s = base('کاغذ در زندگی ما',
         'کاغذ فقط برای نوشتن نیست؛ در آموزش، اطلاع‌رسانی و بسته‌بندی هم کاربرد دارد.', 7, BLUE)
uses = [('کتاب و دفتر','یادگیری و ثبت یادداشت‌ها'),('روزنامه','انتقال خبر و اطلاعات'),('نقشه','نمایش مسیرها و مکان‌ها'),('بسته‌بندی','محافظت و نگهداری کالاها')]
for i,(t,b) in enumerate(uses):
    x=6.85 if i%2==0 else 0.95
    y=2.35+(i//2)*1.75
    card(s,x,y,5.55,1.42,t,b,[BLUE,TEAL,YELLOW,PINK][i],17,13)
rect(s, 1.05, 6.0, 11.2, 0.62, PANEL2, True)
add_text(s, 'نکتهٔ تاریخی: کاغذسازی نخست در چین گسترش یافت و سپس به سرزمین‌های دیگر راه پیدا کرد.', 1.25, 6.08, 10.8, 0.42, 13, YELLOW, True, 'center')

# 8 Properties and color
s = base('ویژگی‌های کاغذ و تغییر آن‌ها',
         'نوع الیاف و مواد افزوده‌شده می‌تواند ظاهر و بعضی ویژگی‌های کاغذ را تغییر دهد.', 8, PINK)
card(s, 8.55, 2.4, 3.85, 1.55, 'رنگ', 'کاغذ می‌تواند سفید، رنگی یا طرح‌دار باشد.', PINK, 17, 13)
card(s, 4.75, 2.4, 3.55, 1.55, 'ضخامت', 'کاغذها با ضخامت‌های متفاوت تولید می‌شوند.', YELLOW, 17, 13)
card(s, 0.95, 2.4, 3.55, 1.55, 'جذب آب', 'برخی کاغذها آب را بیشتر جذب می‌کنند.', TEAL, 17, 13)
rect(s, 1.0, 4.35, 11.35, 1.45, PANEL2, True)
add_text(s, 'سفیدکردن کاغذ', 8.7, 4.52, 3.0, 0.4, 18, YELLOW, True)
add_text(s, 'در صنعت ممکن است برای کم‌کردن رنگ مواد ناخواسته از فرایندهای کنترل‌شده استفاده شود. این کار باید با تجهیزات و نظارت متخصصان انجام شود.', 1.35, 4.98, 10.45, 0.58, 14, WHITE)
add_text(s, 'در آزمایش‌های مدرسه، فقط مشاهده و نتیجه‌گیریِ توضیح‌داده‌شده توسط معلم را دنبال کنید.', 1.0, 6.1, 11.2, 0.42, 12, MUTED, True, 'center')

# 9 Recycling process
s = base('بازیافت کاغذ چگونه انجام می‌شود؟',
         'کاغذهای مصرف‌شده می‌توانند دوباره به چرخهٔ تولید برگردند.', 9, GREEN)
recycle_icon(s, 5.75, 2.55, 1.8)
recycle_steps = [
 ('۱','جمع‌آوری','کاغذهای قابل بازیافت جدا می‌شوند.'),
 ('۲','خردکردن و خمیرسازی','کاغذ به تکه‌های کوچک و سپس خمیر تبدیل می‌شود.'),
 ('۳','شکل‌دهی','خمیر روی سطح توری پخش می‌شود.'),
 ('۴','فشردن و خشک‌کردن','آب اضافی گرفته می‌شود تا ورقهٔ تازه شکل بگیرد.')
]
for i,(n,t,b) in enumerate(recycle_steps):
    x=9.0 if i%2==0 else 0.95
    y=4.45 if i<2 else 5.75
    if i==1: y=4.45
    if i==2: y=5.8
    if i==3: y=5.8
    card(s,x,y,3.45,1.05,t,b,[GREEN,TEAL,YELLOW,BLUE][i],14,10)
add_text(s, 'بازیافت یعنی استفادهٔ دوباره از مواد، نه اینکه هر کاغذی بدون آماده‌سازی دوباره قابل استفاده باشد.', 1.0, 3.9, 11.3, 0.35, 12, MUTED, False, 'center')

# 10 Environment
s = base('چرا بازیافت و صرفه‌جویی مهم است؟',
         'مصرف آگاهانهٔ کاغذ به حفظ منابع طبیعی و محیط زیست کمک می‌کند.', 10, GREEN)
tree_icon(s, 9.8, 2.8, 1.15)
card(s, 6.75, 2.35, 5.6, 1.25, 'حفظ درختان', 'نیاز به چوب تازه کمتر می‌شود.', GREEN, 17, 13)
card(s, 6.75, 3.85, 5.6, 1.25, 'کاهش زباله', 'کاغذهای مصرف‌شده دوباره وارد چرخه می‌شوند.', TEAL, 17, 13)
card(s, 0.95, 2.35, 5.35, 1.25, 'صرفه‌جویی در منابع', 'در بسیاری از فرایندها، مصرف مواد اولیه و انرژی کاهش می‌یابد.', YELLOW, 17, 12)
card(s, 0.95, 3.85, 5.35, 1.25, 'کمک به زیستگاه‌ها', 'حفاظت از جنگل‌ها برای جانوران و گیاهان هم مهم است.', BLUE, 17, 12)
rect(s, 1.0, 5.55, 11.3, 0.88, PANEL2, True)
add_text(s, 'سه کار ساده: از دو روی کاغذ استفاده کنیم • کاغذ سالم را دور نریزیم • کاغذهای قابل بازیافت را جدا کنیم', 1.2, 5.7, 10.9, 0.55, 14, WHITE, True, 'center')

# 11 Summary and questions
s = base('جمع‌بندی؛ چه چیزهایی یاد گرفتیم؟',
         'با چند پرسش کوتاه، نکته‌های اصلی درس را مرور کنیم.', 11, YELLOW)
card(s, 7.0, 2.35, 5.35, 1.22, '۱. مواد طبیعی چه هستند؟', 'موادی که در طبیعت یافت می‌شوند؛ مانند چوب، پنبه و سنگ.', GREEN, 16, 12)
card(s, 0.95, 2.35, 5.55, 1.22, '۲. کاغذ از چه چیزی ساخته می‌شود؟', 'معمولاً از الیاف گیاهی که به خمیر و سپس ورقه تبدیل می‌شوند.', TEAL, 16, 12)
card(s, 7.0, 3.85, 5.35, 1.22, '۳. بازیافت چه فایده‌ای دارد؟', 'به کاهش مصرف منابع و کم‌شدن زباله کمک می‌کند.', YELLOW, 16, 12)
card(s, 0.95, 3.85, 5.55, 1.22, '۴. ما چه کاری می‌توانیم انجام دهیم؟', 'صرفه‌جویی، استفاده از دو روی کاغذ و جداسازی کاغذهای باطله.', BLUE, 16, 12)
rect(s, 2.0, 5.55, 9.3, 0.78, PANEL2, True)
add_text(s, 'پیام پایانی: با مصرف درست کاغذ، از طبیعت بهتر مراقبت می‌کنیم.', 2.2, 5.7, 8.9, 0.45, 17, YELLOW, True, 'center')

prs.save('Oloom6_Nature_to_Paper_11_Slides.pptx')
print('Created 11-slide presentation.')
