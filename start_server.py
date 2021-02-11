from bottle import route, run, template, request
from number_ans import number_ans


@route('/start')
def start():
    return template('image_template', output_text='')


@route('/start', method='POST')
def start_up():
    input_image = request.files.input_image
    output_text = number_ans(input_image)
    return template('image_template', output_text=output_text)


run(host='localhost', port=8080, debug=True)
