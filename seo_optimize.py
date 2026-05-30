#!/usr/bin/env python3
"""SEO оптимизация stroycash — meta, titles, H1, Schema.org"""
import os, re

SITE_DIR = "/Users/macbook/Desktop/1/stroycash_new/stroycash"

# ── Данные по каждой странице ─────────────────────────────────────────────
PAGES = {
    "page51428489.html": {
        "slug": "/",
        "title": "Ремонт квартир и строительство домов под ключ в Москве и МО — СтройКэш",
        "desc":  "СтройКэш — ремонт квартир, строительство домов, дизайн интерьера под ключ в Москве и МО. 380 проектов, гарантия 5 лет, без выходных. Звоните: +7 (930) 334-61-76",
        "h1":    None,
        "schema_service": "Строительная компания — ремонт и строительство под ключ",
    },
    "page34319973.html": {
        "slug": "/remont",
        "title": "Ремонт квартир под ключ в Москве и области — СтройКэш",
        "desc":  "Ремонт квартир под ключ в Москве и МО — СтройКэш. Евроремонт, дизайнерский, черновой, косметический. Фиксированная цена, сроки по договору, гарантия 5 лет.",
        "h1":    None,
        "schema_service": "Ремонт квартир под ключ",
    },
    "page36631847.html": {
        "slug": "/build",
        "title": "Строительство домов из натуральных материалов под ключ — СтройКэш",
        "desc":  "Строительство домов под ключ в Москве и МО — СтройКэш. Монолитные, деревянные, каменные дома от 4 000 000 ₽. Дизайн-проект в подарок, гарантия 5 лет.",
        "h1":    None,
        "schema_service": "Строительство домов из натуральных материалов",
    },
    "page34448363.html": {
        "slug": "/remontdomov",
        "title": "Ремонт домов и коттеджей под ключ в Москве и МО — СтройКэш",
        "desc":  "Ремонт домов и коттеджей под ключ в Москве и МО — СтройКэш. Евроремонт, дизайнерский, черновой ремонт загородного дома. Фиксированная цена, гарантия 5 лет.",
        "h1":    None,
        "schema_service": "Ремонт домов и коттеджей под ключ",
    },
    "page34448545.html": {
        "slug": "/klinika",
        "title": "Ремонт медицинских клиник под ключ в Москве и МО — СтройКэш",
        "desc":  "Ремонт медицинских клиник под ключ в Москве и МО — СтройКэш. Соблюдение норм СанПиН, отделка кабинетов, работаем без остановки клиники. Опыт 20+ объектов.",
        "h1":    None,
        "schema_service": "Ремонт медицинских клиник под ключ",
    },
    "page27262068.html": {
        "slug": "/engineering",
        "title": "Проектирование зданий и помещений в Москве и МО — СтройКэш",
        "desc":  "Проектирование зданий и помещений в Москве и МО — СтройКэш. Архитектурные, конструктивные, инженерные проекты. Согласование в Госстрой, Мосгосэкспертиза.",
        "h1":    None,
        "schema_service": "Проектирование зданий и помещений",
    },
    "page27262073.html": {
        "slug": "/disign",
        "title": "Дизайн интерьера под ключ в Москве и МО — СтройКэш",
        "desc":  "Дизайн интерьера под ключ в Москве и МО — СтройКэш. Авторский дизайн-проект, 3D-визуализация, авторский надзор. Скидка на ремонт при заказе дизайна.",
        "h1":    "Дизайн интерьера под ключ в Москве и МО — СтройКэш",
        "schema_service": "Дизайн интерьера под ключ",
    },
    "page30554334.html": {
        "slug": "/shtukaturka",
        "title": "Механизированная штукатурка стен и потолков в Москве — СтройКэш",
        "desc":  "Механизированная штукатурка стен в Москве и МО — СтройКэш. Машинное нанесение, идеально ровные стены за 1–2 дня. Цена от 350 ₽/кв.м, гарантия качества.",
        "h1":    None,
        "schema_service": "Механизированная штукатурка стен и потолков",
    },
    "page37346001.html": {
        "slug": "/styajka",
        "title": "Полусухая стяжка пола в Москве и МО — от 300 ₽/кв.м — СтройКэш",
        "desc":  "Полусухая стяжка пола в Москве и МО — СтройКэш. Идеально ровный пол за 1 день, нагрузка через 12 часов. Цена от 300 ₽/кв.м, выезд замерщика бесплатно.",
        "h1":    None,
        "schema_service": "Полусухая стяжка пола",
    },
    "page34448315.html": {
        "slug": "/pomesheniya",
        "title": "Ремонт коммерческих помещений под ключ в Москве — СтройКэш",
        "desc":  "Ремонт коммерческих помещений под ключ в Москве и МО — СтройКэш. Офисы, магазины, рестораны, склады. Работаем без остановки бизнеса, гарантия 5 лет.",
        "h1":    None,
        "schema_service": "Ремонт коммерческих помещений под ключ",
    },
    "page34448619.html": {
        "slug": "/stomatologiy",
        "title": "Ремонт стоматологий под ключ в Москве и МО — СтройКэш",
        "desc":  "Ремонт стоматологий под ключ в Москве и МО — СтройКэш. Соблюдение норм Роспотребнадзора и лицензионных требований. Опыт 20+ стоматологических кабинетов.",
        "h1":    None,
        "schema_service": "Ремонт стоматологий под ключ",
    },
    "page39349977.html": {
        "slug": "/mebel",
        "title": "Мебель на заказ в Москве и МО — корпусная, кухни, шкафы — СтройКэш",
        "desc":  "Мебель на заказ в Москве и МО — СтройКэш. Корпусная мебель, шкафы-купе, кухни по индивидуальным размерам. Бесплатный замер, гарантия 3 года.",
        "h1":    None,
        "schema_service": "Мебель на заказ — корпусная мебель, кухни, шкафы",
    },
    "page27262075.html": {
        "slug": "/portfolio",
        "title": "Портфолио выполненных работ — ремонт и строительство — СтройКэш",
        "desc":  "Портфолио СтройКэш — фото выполненных ремонтов и строительных проектов в Москве и МО. 380 объектов: квартиры, дома, офисы, клиники, стоматологии.",
        "h1":    None,
        "schema_service": None,
    },
    "page27176351.html": {
        "slug": "/about",
        "title": "Контакты СтройКэш — строительная компания в Мытищах",
        "desc":  "Контакты СтройКэш — строительная компания. Телефон: +7 (930) 334-61-76. Адрес: г. Мытищи, ул. Медицинская 4А. Работаем без выходных, 8:00–22:00.",
        "h1":    None,
        "schema_service": None,
    },
    "page37551065.html": {
        "slug": "/team",
        "title": "Наша команда — профессиональные строители и дизайнеры — СтройКэш",
        "desc":  "Команда СтройКэш — 9 профессиональных строителей и дизайнеров в Москве и МО. Опыт от 7 лет. Руководитель — Геннадий Васильевич, с 2014 года на рынке.",
        "h1":    None,
        "schema_service": None,
    },
    "page34448199.html": {
        "slug": "/vanna",
        "title": "Ремонт ванной комнаты под ключ в Москве и МО — СтройКэш",
        "desc":  "Ремонт ванной комнаты под ключ в Москве и МО — СтройКэш. Плитка, сантехника, освещение, гидроизоляция. От 180 000 ₽, сроки от 14 дней, гарантия 5 лет.",
        "h1":    None,
        "schema_service": "Ремонт ванной комнаты под ключ",
    },
    "page34448265.html": {
        "slug": "/sanuzel",
        "title": "Ремонт санузла под ключ в Москве и МО — СтройКэш",
        "desc":  "Ремонт санузла под ключ в Москве и МО — СтройКэш. Совмещённый и раздельный санузел, гидроизоляция, плитка, сантехника. Гарантия 5 лет, фиксированная цена.",
        "h1":    None,
        "schema_service": "Ремонт санузла под ключ",
    },
    "page34448395.html": {
        "slug": "/kotedzh",
        "title": "Ремонт коттеджей под ключ в Москве и МО — СтройКэш",
        "desc":  "Ремонт коттеджей под ключ в Москве и МО — СтройКэш. Черновой, чистовой, дизайнерский ремонт загородного дома. Фиксированная цена, гарантия 5 лет.",
        "h1":    None,
        "schema_service": "Ремонт коттеджей под ключ",
    },
    "page34448443.html": {
        "slug": "/ofisov",
        "title": "Ремонт офисов под ключ в Москве и МО — СтройКэш",
        "desc":  "Ремонт офисов под ключ в Москве и МО — СтройКэш. Офисные помещения, переговорные, open space. Работаем без остановки вашего бизнеса, гарантия 5 лет.",
        "h1":    None,
        "schema_service": "Ремонт офисов под ключ",
    },
    "page34448501.html": {
        "slug": "/novostroika",
        "title": "Ремонт квартиры в новостройке под ключ в Москве — СтройКэш",
        "desc":  "Ремонт квартиры в новостройке под ключ в Москве и МО — СтройКэш. Черновой, чистовой, под ключ. Принимаем с нулевой отделкой, гарантия 5 лет.",
        "h1":    None,
        "schema_service": "Ремонт квартиры в новостройке под ключ",
    },
    "page34448654.html": {
        "slug": "/otdelka",
        "title": "Отделка квартир под ключ в Москве и МО — СтройКэш",
        "desc":  "Отделка квартир под ключ в Москве и МО — СтройКэш. Чистовая и финишная отделка стен, полов, потолков. Фиксированная цена, сроки по договору, гарантия 5 лет.",
        "h1":    None,
        "schema_service": "Отделка квартир под ключ",
    },
    "page27262080.html": {
        "slug": "/calculator",
        "title": "Калькулятор стоимости ремонта квартиры онлайн — СтройКэш",
        "desc":  "Рассчитайте стоимость ремонта квартиры онлайн — СтройКэш. Введите площадь и тип ремонта — получите точную смету. Бесплатный выезд замерщика.",
        "h1":    "Калькулятор стоимости ремонта квартиры онлайн",
        "schema_service": None,
    },
    "page55131289.html": {
        "slug": "/quiz",
        "title": "Рассчитать стоимость ремонта квартиры онлайн — СтройКэш",
        "desc":  "Пройдите короткий квиз и получите точный расчёт стоимости ремонта квартиры в Москве. 5 вопросов — 2 минуты. Скидка 10% за заявку через квиз.",
        "h1":    None,
        "schema_service": None,
    },
    "page55192735.html": {
        "slug": "/quizstroy",
        "title": "Рассчитать стоимость строительства дома онлайн — СтройКэш",
        "desc":  "Пройдите короткий квиз и получите точный расчёт стоимости строительства дома в Москве и МО. 5 вопросов — 2 минуты. Бесплатная консультация архитектора.",
        "h1":    None,
        "schema_service": None,
    },
    "page55193637.html": {
        "slug": "/quizmebel",
        "title": "Рассчитать стоимость мебели на заказ онлайн — СтройКэш",
        "desc":  "Пройдите короткий квиз и получите точный расчёт стоимости мебели на заказ. 5 вопросов — 2 минуты. Бесплатный замер и консультация дизайнера.",
        "h1":    "Рассчитайте стоимость мебели на заказ",
        "schema_service": None,
    },
}

# ── Schema.org JSON-LD ────────────────────────────────────────────────────
def make_schema(slug, service_name):
    base = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
                "@id": "https://stroycash.ru/#business",
                "name": "СтройКэш",
                "alternateName": "Stroy Cash",
                "description": "Ремонт квартир, строительство домов и дизайн интерьера под ключ в Москве и Московской области",
                "url": "https://stroycash.ru",
                "telephone": "+7-930-334-61-76",
                "email": "stroycash2020@mail.ru",
                "foundingDate": "2014",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "ул. Медицинская 4А",
                    "addressLocality": "Мытищи",
                    "addressRegion": "Московская область",
                    "postalCode": "141009",
                    "addressCountry": "RU"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 55.9112,
                    "longitude": 37.7317
                },
                "areaServed": [
                    {"@type": "City", "name": "Москва"},
                    {"@type": "AdministrativeArea", "name": "Московская область"}
                ],
                "openingHoursSpecification": [{
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
                    "opens": "08:00",
                    "closes": "22:00"
                }],
                "priceRange": "$$",
                "image": "https://stroycash.ru/images/tild6535-3636-4261-b963-313361326437___stroy_cash.png",
                "numberOfEmployees": {"@type": "QuantitativeValue", "value": 9},
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": "4.9",
                    "reviewCount": "127",
                    "bestRating": "5"
                }
            }
        ]
    }
    if service_name:
        base["@graph"].append({
            "@type": "Service",
            "provider": {"@id": "https://stroycash.ru/#business"},
            "name": service_name,
            "areaServed": [
                {"@type": "City", "name": "Москва"},
                {"@type": "AdministrativeArea", "name": "Московская область"}
            ],
            "url": f"https://stroycash.ru{slug}"
        })
    import json
    return f'<script type="application/ld+json">\n{json.dumps(base, ensure_ascii=False, indent=2)}\n</script>'

# ── Обработка файла ───────────────────────────────────────────────────────
def process(fname, data):
    path = os.path.join(SITE_DIR, fname)
    with open(path, encoding="utf-8") as f:
        html = f.read()

    changes = []

    # 1. Title
    old_title = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
    if old_title and old_title.group(1) != data["title"]:
        html = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>',
                      html, flags=re.IGNORECASE)
        changes.append("title")

    # 2. Meta description
    old_desc = re.search(r'<meta\s+name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html, re.IGNORECASE)
    old_desc2 = re.search(r'<meta\s+content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', html, re.IGNORECASE)
    new_meta = f'<meta name="description" content="{data["desc"]}">'
    if old_desc:
        html = re.sub(r'<meta\s+name=["\']description["\'][^>]*/?>',
                      new_meta, html, flags=re.IGNORECASE)
        changes.append("meta desc")
    elif old_desc2:
        html = re.sub(r'<meta\s+content=["\'][^"\']*["\'][^>]*name=["\']description["\'][^>]*/?>',
                      new_meta, html, flags=re.IGNORECASE)
        changes.append("meta desc")
    else:
        html = html.replace('</head>', f'{new_meta}\n</head>', 1)
        changes.append("meta desc (new)")

    # 3. og:description
    og_desc_new = f'<meta property="og:description" content="{data["desc"]}">'
    html = re.sub(r'<meta\s+property=["\']og:description["\'][^>]*/?>',
                  og_desc_new, html, flags=re.IGNORECASE)

    # 4. og:title — приводим к title страницы
    og_title_new = f'<meta property="og:title" content="{data["title"]}">'
    html = re.sub(r'<meta\s+property=["\']og:title["\'][^>]*/?>',
                  og_title_new, html, flags=re.IGNORECASE)

    # 5. Schema.org — добавляем перед </head> (удаляем старую если есть)
    html = re.sub(r'<script\s+type=["\']application/ld\+json["\']>.*?</script>',
                  '', html, flags=re.DOTALL|re.IGNORECASE)
    schema = make_schema(data["slug"], data.get("schema_service"))
    html = html.replace('</head>', f'{schema}\n</head>', 1)
    changes.append("schema")

    # 6. H1 — добавляем скрытый после <body если нужен
    if data.get("h1"):
        h1_html = (
            f'<h1 style="position:absolute;width:1px;height:1px;overflow:hidden;'
            f'clip:rect(0,0,0,0);white-space:nowrap;border:0">'
            f'{data["h1"]}</h1>'
        )
        html = re.sub(r'(<body[^>]*>)', r'\1' + h1_html, html, count=1, flags=re.IGNORECASE)
        changes.append("H1")

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    return changes

# ── Запуск ────────────────────────────────────────────────────────────────
print("Обрабатываю страницы...\n")
for fname, data in PAGES.items():
    changes = process(fname, data)
    print(f"  {data['slug']:22s}  [{', '.join(changes)}]")

print(f"\nГотово! Обработано {len(PAGES)} страниц.")
