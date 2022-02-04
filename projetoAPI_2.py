# import main Flask class and request object
from flask import Flask, request
from datetime import datetime


# create the Flask app
app = Flask(__name__)


# allow both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def form_example2():

    # handle the POST request
    if request.method == 'POST':
        user = request.form.get('inputKey')
        senha = request.form.get('inputValue')


        if user=='KNOX' and senha=='123456':

            html_2=""
            f = open('html_2.html', 'r')
            for line in f:
                html_2=html_2+line+'\n'
            
            html_2=html_2.replace('TOKEN_01',str(datetime.today())[:19])

            token_05="Ola, " + user.upper() + "!!"
            html_2=html_2.replace('TOKEN_05',token_05)


            return(html_2)



            return '''
                    <h1>The language value is: {}</h1>
                    <h1>The framework value is: {}</h1>'''.format(user, senha)
        else:
            return('<h1>USUARIO OU SENHA INVALIDOS</h1>')

    # otherwise handle the GET request

    html=""
    f = open('html.html', 'r')
    for line in f:
        html=html+line+'\n'
    
    html=html.replace('TOKEN_01',str(datetime.today())[:19])

    return(html)


    
if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=False, port=5000)
    
