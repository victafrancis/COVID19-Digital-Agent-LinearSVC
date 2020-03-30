from flask import Flask, render_template, url_for, request
import pickle
import responses, functions
import numpy as np

# import keras.backend.tensorflow_backend as tb
# tb._SYMBOLIC_SCOPE.value = True

app = Flask(__name__)

# loading the model from pickle
virtual_agent_model = pickle.load(open('LinearSVC-VirtualAgent.pickle','rb'))
#loading the vectorizer from pickle
vectorizer = pickle.load(open('cv_vector.pickle','rb'))

@app.route('/', methods=['POST', 'GET'])
def home():

    content = {'question':'','confidence':'','response_title':'','response_content':''}
    data = functions.getData()
    content['infected_count'] = data['infected']
    content['recovered_count'] = data['recovered']
    content['death_count'] = data['deaths']
    content['death_rate'] = data['death_rate']
    content['recovery_rate'] = data['recovery_rate']
    content['datetime'] = data['datetime']


    if request.method == 'POST':
        question = request.form['question']  #get question from form

        print(question)
        content['question'] = question
        question = functions.check(question)
        print('corrected question: ' + question)
        qtn = vectorizer.transform([question])  #transform to a vector
        qtn = qtn.toarray()  #transform to array
        prediction = virtual_agent_model.predict(qtn)
        print(responses.class_names[np.argmax(prediction[0])])
        content['response_title'] = responses.class_names[prediction[0]]
        content['response_content'] = responses.class_responses[prediction[0]]

    return render_template('index.html', content=content)

# API endpoint
@app.route('/api', methods=['GET'])
def api():
    question = request.args['q']
    question = functions.check(question)
    qtn = vectorizer.transform([question])  #transform to a vector
    qtn = qtn.toarray()  #transform to array
    prediction = virtual_agent_model.predict(qtn)

    data = {
        'question': question,
        'response_title': responses.class_names[prediction[0]],
        'response_content': responses.class_responses[prediction[0]]
    }

    return data


if __name__ == '__main__':
    app.run(debug=True, threaded=False)