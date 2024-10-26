import pandas as pd


def fibonacci_levels(min_price, max_price):
    """Функция для вычисления уровней коррекции Фибоначчи."""
    diff = max_price - min_price
    levels = {
        '0%': max_price,
        '23.6%': max_price - diff * 0.236,
        '38.2%': max_price - diff * 0.382,
        '50%': max_price - diff * 0.5,
        '61.8%': max_price - diff * 0.618,
        '100%': min_price
    }
    return levels


def read_data(input_file):
    """Чтение входных данных из CSV."""
    return pd.read_csv(input_file)


def save_forecast(levels, output_file):
    """Сохранение уровней Фибоначчи в файл."""
    pd.DataFrame(list(levels.items()), columns=['Level', 'Price']).to_csv(output_file, index=False)


def forecast_fibonacci(input_file, output_file):
    """Прогнозирование уровней Фибоначчи на основе данных."""
    data = read_data(input_file)

    # Предполагается, что в CSV есть столбец 'Close' с ценами закрытия
    min_price = data['Close'].min()
    max_price = data['Close'].max()

    # Вычисление уровней Фибоначчи
    levels = fibonacci_levels(min_price, max_price)

    # Сохранение прогноза в выходной файл
    save_forecast(levels, output_file)
    print(f"Прогноз сохранен в файл {output_file}")

# Пример использования:
forecast_fibonacci('historical_data.csv', 'fibonacci_forecast.csv')
