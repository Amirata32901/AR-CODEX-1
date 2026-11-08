from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.oxml import parse_xml
from pptx.oxml.ns import nsdecls
from pptx.enum.text import MSO_AUTO_SIZE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

BG = RGBColor(12, 15, 28)
PANEL = RGBColor(23, 28, 48)
PURPLE = RGBColor(147, 92, 255)
YELLOW = RGBColor(255, 211, 74)
WHITE = RGBColor(245, 247, 255)
MUTED = RGBColor(184, 192, 215)
GREEN = RGBColor(87, 214, 163)

slides = [
("از درخت تا کاغذ", "سفر شگفت‌انگیز چوب؛ از جنگل تا دفترهای ما", ["علوم تجربی پایه ششم", "آشنایی با مراحل تولید کاغذ و اهمیت بازیافت"], "cover"),
("کاغذ از کجا می‌آید؟", "کاغذ از الیاف گیاهی ساخته می‌شود؛ یکی از منابع مهم این الیاف، چوب درختان است.", ["در کارخانه، چوب طی چند مرحله به خمیر تبدیل می‌شود.", "خمیر روی توری پخش می‌شود و آب آن گرفته می‌شود.", "در پایان، ورقه‌ها خشک و برش داده می‌شوند."], "origin"),
("مرحلهٔ اول؛ آماده‌سازی چوب", "پس از انتخاب و آماده‌سازی چوب در مراکز مجاز، تنه‌ها به کارخانه منتقل می‌شوند.", ["۱. بریدن و آماده‌کردن تنه‌های درخت", "۲. حمل چوب‌ها با کامیون به کارخانهٔ کاغذسازی", "هدف: رساندن مادهٔ اولیه به خط تولید"], "truck"),
("مرحلهٔ دوم؛ پوست‌گیری", "در کارخانه، پوست تنه جدا می‌شود تا چوب برای خردشدن و فرآوری آماده شود.", ["پوست‌گیری باعث آماده‌شدن سطح چوب می‌شود.", "بخش‌های نامناسب و اضافی جدا می‌شوند.", "چوب تمیز وارد مرحلهٔ بعدی می‌شود."], "bark"),
("مرحلهٔ سوم؛ خردکردن چوب", "چوب‌های آماده‌شده به قطعه‌های کوچک‌تری به نام «تراشه» تبدیل می‌شوند.", ["تراشه‌ها اندازه‌ای کوچک و تقریباً یکنواخت دارند.", "خردشدن چوب، انجام مراحل بعدی را آسان‌تر می‌کند.", "تراشه‌ها مادهٔ اولیهٔ ساخت خمیر کاغذ هستند."], "chips"),
("مرحلهٔ چهارم؛ ساخت خمیر کاغذ", "در فرایند کارخانه‌ای، الیاف چوب از هم جدا می‌شوند و خمیر کاغذ به دست می‌آید.", ["خمیر کاغذ مخلوطی از الیاف ریز و آب است.", "الیاف همان رشته‌های بسیار نازکی هستند که ورقهٔ کاغذ را می‌سازند.", "خمیر باید به‌طور یکنواخت آماده شود."], "pulp"),
("مرحلهٔ پنجم؛ شکل‌گیری ورقه", "خمیر روی توری مخصوص پخش می‌شود؛ آب اضافی از آن جدا می‌شود و لایه‌ای نازک شکل می‌گیرد.", ["الیاف در کنار هم قرار می‌گیرند.", "با خارج‌شدن آب، ورقه کم‌کم شکل می‌گیرد.", "فشار و خشک‌کردن به استحکام ورقه کمک می‌کند."], "sheet"),
("مرحلهٔ ششم؛ خشک‌کردن و برش", "ورقهٔ شکل‌گرفته خشک، صاف و سپس در اندازه‌های موردنیاز برش داده می‌شود.", ["رطوبت باقی‌مانده گرفته می‌شود.", "سطح کاغذ صاف و آمادهٔ استفاده می‌شود.", "کاغذها بسته‌بندی و به بازار فرستاده می‌شوند."], "finish"),
("کاغذ بازیافتی چگونه تولید می‌شود؟", "کاغذهای باطله می‌توانند دوباره به مادهٔ اولیه تبدیل شوند.", ["کاغذهای مصرف‌شده جمع‌آوری و دسته‌بندی می‌شوند.", "با آب، خمیر تازه‌ای از الیاف آن‌ها تهیه می‌شود.", "پس از پاک‌سازی و آماده‌سازی، دوباره ورقه ساخته می‌شود."], "recycle"),
("چرا باید کاغذ را بازیافت کنیم؟", "بازیافت، مصرف منابع طبیعی را کمتر می‌کند و به حفاظت از محیط‌زیست کمک می‌کند.", ["نیاز به قطع درختان تازه کاهش می‌یابد.", "در مصرف آب و انرژی صرفه‌جویی می‌شود.", "حجم زباله‌ها کمتر می‌شود.", "از زیستگاه جانوران و سلامت طبیعت بهتر محافظت می‌کنیم."], "benefits"),
("جمع‌بندی؛ سهم ما در حفاظت از طبیعت", "هر برگ کاغذ ارزشمند است؛ با مصرف درست، به طبیعت فرصت نفس‌کشیدن می‌دهیم.", ["از هر دو روی کاغذ استفاده کنیم.", "کاغذهای باطله را جداگانه جمع‌آوری کنیم.", "تا جای ممکن از کاغذ کمتر استفاده کنیم.", "پرسش پایانی: کدام مرحلهٔ تولید کاغذ برایت جالب‌تر بود؟"], "end"),
]

def set_rtl(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    pPr.append(parse_xml('<a:rtl %s val="1"/>' % nsdecls('a')))

def textbox(slide, x, y, w, h, text, size, color, bold=False, align=PP_ALIGN.RIGHT):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = Inches(.08); tf.margin_right = Inches(.08)
    tf.margin_top = Inches(.04); tf.margin_bottom = Inches(.04)
    p = tf.paragraphs[0]
    p.alignment = align
    set_rtl(p)
    r = p.add_run(); r.text = text
    r.font.name = "Vazirmatn"
    r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color
    return box

def rounded(slide, x, y, w, h, fill, radius=True):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
                                   Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid(); shape.fill.fore_color.rgb = fill
    shape.line.fill.background()
    return shape

for i, (title, subtitle, bullets, kind) in enumerate(slides, 1):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid(); slide.background.fill.fore_color.rgb = BG
    # Accent rails and decorative circles
    rounded(slide, 12.92, 0, .18, 7.5, PURPLE, False)
    rounded(slide, .42, .45, .12, .8, YELLOW, False)
    # small decorative dots
    for j in range(5):
        dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(.55+j*.22), Inches(6.9), Inches(.07), Inches(.07))
        dot.fill.solid(); dot.fill.fore_color.rgb = PURPLE if j % 2 == 0 else YELLOW
        dot.line.fill.background()

    if kind == "cover":
        textbox(slide, 1.0, 1.25, 11.2, .55, "علوم تجربی پایه ششم  |  فصل مواد و ساخت", 18, YELLOW, True)
        textbox(slide, 1.0, 2.05, 11.2, 1.35, title, 42, WHITE, True)
        textbox(slide, 1.0, 3.55, 10.7, .75, subtitle, 23, MUTED)
        rounded(slide, 1.0, 4.75, 11.0, 1.15, PANEL)
        textbox(slide, 1.35, 4.92, 10.3, .72, "از یک تنهٔ درخت تا برگه‌ای که هر روز روی آن می‌نویسیم...", 21, GREEN, True)
    else:
        textbox(slide, .95, .55, 11.35, .65, title, 29, WHITE, True)
        rounded(slide, .95, 1.42, 11.35, .08, PURPLE, False)
        rounded(slide, .95, 1.82, 11.35, 4.65, PANEL)
        textbox(slide, 1.35, 2.05, 10.55, .9, subtitle, 19, YELLOW, True)
        y = 3.15
        for b in bullets:
            rounded(slide, 10.95, y+.13, .16, .16, GREEN, True)
            textbox(slide, 1.45, y, 9.2, .65, b, 17, WHITE)
            y += .72
        # right-side visual badge, abstract process icon
        rounded(slide, 1.1, 5.75, 1.25, .45, PURPLE)
        textbox(slide, 1.12, 5.77, 1.2, .35, f"{i:02d}", 16, WHITE, True, PP_ALIGN.CENTER)

    textbox(slide, 9.2, 6.88, 2.9, .28, "علوم ششم  •  از درخت تا کاغذ", 10, MUTED)
    textbox(slide, .95, 6.83, 1.4, .32, f"{i} / 11", 10, YELLOW, True, PP_ALIGN.LEFT)

prs.save("OZ_DARAKHT_TA_KAGHAZ_11_SLIDES.pptx")
