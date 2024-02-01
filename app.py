from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    answer1 = request.form.get('answer1')
    answer2 = request.form.get('answer2')

    # In a real application, you would store these values in a database
    # For simplicity, we'll print them to the console here
    print('Name:', name)
    print('Answer 1:', answer1)
    print('Answer 2:', answer2)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
