CATEGORIES = {
    '📈 Скидки': 'discount?from=50&to=100/',
    '👩‍🦰 Для женщин': 'category/48/',
    '🧍‍ Для девочек': 'category/86/',
    '🧔 Для мужчин' : 'category/47/',
    '🧍 Для мальчиков': 'category/49/',
    '⌚️ Аксессуары': 'category/96/'
}

def get_value(category):
    for k, v in CATEGORIES.items():
        if k == category:
            return v