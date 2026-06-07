# /// script
# dependencies = ["marimo",
#     "matplotlib",
#     "pandas",]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt

    return mo, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 2.3 ГЗ

    Завдання 1

    Варіант 16 (6)

    ## Умова

    Дані (% завантаженості сервера): 60, 65, 70, 68, 75, 80, 85, 75, 85, 80.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Розв'язання:

    Для згладжування часового ряду та виявлення загальної тенденції (тренду) використовується **метод простої ковзної середньої** (Simple Moving Average, SMA).

    Цей метод належить до алгоритмів фільтрації низьких частот і дозволяє усунути короткострокові випадкові коливання (шум).

    Математична модель (формула ковзного вікна) для знаходження згладженого значення $\bar{y}_t$ в момент часу $t$ для вікна розміром $n$ виглядає так:

    $$\bar{y}_t = \frac{1}{n} \sum_{i=0}^{n-1} y_{t-i} = \frac{y_t + y_{t-1} + \dots + y_{t-n+1}}{n}$$

    де:
    * $t$ - момент часу;
    * $\bar{y}_t$ — згладжене значення ряду;
    * $n$ — розмір ковзного вікна (інтервал згладжування);
    * $y_{t-i}$ — фактичні (вихідні) значення часового ряду.

    **Алгоритм застосування:**
    1. **Ініціалізація вікна:** Береться перша група з $n$ значень ряду і розраховується їх середнє арифметичне.
    2. **Зсув (ковзання):** Вікно зсувається на один крок уперед (відкидається найстаріше спостереження і додається наступне нове).
    3. **Мета:** Отриманий новий згладжений ряд дозволяє краще візуалізувати основну динаміку розвитку процесу, приховуючи локальні аномалії.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    y_values = [60, 65, 70, 68, 75, 80, 85, 75, 85, 80]

    window_slider = mo.ui.slider(
        start=2,
        stop=7,
        step=1,
        value=4,
        label='Розмір ковзного вікна:'
    )

    mo.vstack([
        mo.md("### Налаштування параметрів"),
        window_slider
    ])
    return window_slider, y_values


@app.cell(hide_code=True)
def _(mo, pd, window_slider, y_values):
    # Створюємо DataFrame
    df = pd.DataFrame({
        "t": range(1, len(y_values) + 1),
        "Y": y_values
    })

    # Зчитуємо поточне значення з повзунка
    n = window_slider.value
    col_name = f"MA({n})"

    # Обчислюємо ковзну середню вбудованим методом pandas
    df[col_name] = df["Y"].rolling(window=n).mean()

    mo.vstack([
        mo.md(f"## Розрахунки\r### Таблиця розрахунків (вікно n={n})"),
        mo.ui.table(df, selection=None)
    ])
    return col_name, df


@app.cell(hide_code=True)
def _(col_name, df, mo, plt):
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.style.use('seaborn-v0_8-darkgrid')

    # Лінія вихідних даних
    ax.plot(df["t"], df["Y"], marker="o", linestyle="--", color="gray", label="Вихідний ряд (Y)")

    # Лінія згладжених даних
    ax.plot(df["t"], df[col_name], marker="s", linewidth=2, color="blue", label=f"Згладжений ряд {col_name}")

    ax.set_title("Динаміка зміни показників")
    ax.set_xlabel("Час (t)")
    ax.set_ylabel("Значення")
    ax.legend()

    mo.vstack([
        mo.md("## Візуалізація"),
        fig  # <--- Просто передаємо об'єкт fig
    ])
    return


if __name__ == "__main__":
    app.run()
