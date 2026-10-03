def test1():
    import pickle
    # Загрузка модели из файла pickle
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    import pandas as pd
    # Новые данные
    new_data = pd.DataFrame({
        'Pclass': [3],
        'Age': [5.0],
        'Fare': [7.2500]
    })
    # Предсказание
    predictions = model.predict(new_data)

    # Вывод результатов
    print("Predicted Survival:", predictions)

if __name__ == '__main__':
    test1()