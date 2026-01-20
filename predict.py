def predicts(data,model):
    x = data['input']
    if not isinstance(x, list):
        return {'error': 'Input should be a list'}, 400
    prediction = model.predict([x])
    if prediction[0] == 'M':
        p = ['Malignant']
    else:
        p = ['Benign']
    return {'prediction': p}      