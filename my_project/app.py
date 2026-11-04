from flask import Flask, render_template, request

app = Flask(__name__)


def generate_recommendations(destination, budget):
    dest_lower = destination.lower()

    # Логіка підбору оптимального маршруту залежно від напрямку та бюджету
    if 'львів' in dest_lower or 'карпати' in dest_lower or 'ужгород' in dest_lower:
        if budget >= 15000:
            route = "Швидкісний потяг Інтерсіті+ (1клас) або комбінований тур з трансфером"
        else:
            route = "Нічний потяг (купе) або комфортабельний рейсовий автобус"
    elif 'одеса' in dest_lower or 'моршин' in dest_lower:
        if budget >= 20000:
            route = "Фірмовий швидкісний потяг або переліт (за наявності)"
        else:
            route = "Плацкарт/купе потяга далекого прямування"
    else:
        if budget >= 15000:
            route = "Швидкісний потяг або власний автомобіль (високий комфорт)"
        else:
            route = "Зручний потяг або автобусне сполучення"

    # Підбір проживання та розваг залежно від бюджету
    if budget < 8000:
        accommodation = "Хостел у центрі міста або затишна бюджетна квартира (Airbnb)"
        entertainment = "Безкоштовні пішохідні прогулянки, відвідування кав’ярень та парків"
    elif budget < 30000:
        accommodation = "Готель 3* у зручному районі з включеними сніданками"
        entertainment = "Оглядові екскурсії з гідом, музеї, затишні ресторани"
    else:
        accommodation = "П'ятизірковий готель або апартаменти класу люкс"
        entertainment = "Ресторани високої кухні, приватні тури, спа-процедури"

    return {
        'route': route,
        'accommodation': accommodation,
        'entertainment': entertainment
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    destination = ""
    dates = ""
    budget = ""

    if request.method == 'POST':
        destination = request.form.get('destination', '')
        dates = request.form.get('dates', '')
        try:
            budget = float(request.form.get('budget', 0))
        except ValueError:
            budget = 0

        recommendations = generate_recommendations(destination, budget)

    return render_template(
        'index.html',
        recommendations=recommendations,
        destination=destination,
        dates=dates,
        budget=budget
    )


if __name__ == '__main__':
    app.run(debug=True)