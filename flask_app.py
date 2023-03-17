from flask import Flask, jsonify, request, abort
import db
import logging 

app = Flask(__name__)

@app.get('/')
def homepage():
    return 'The home page'


@app.post('/api/favorite_color')
def add_color():

    submitted_json = request.get_json()

    if 'color' in submitted_json:
        color = submitted_json.get('color')
        if color and type(color) == str:

            success = db.add_color(color)
            if success:
                return jsonify({'result': 'Success - color submitted'}), 201
            else:
                logging.error('Database error')
                abort(500)
        else:
            return jsonify({'error': 'Bad request - color must have a string value'}), 400
    else:
        return jsonify({'error': 'Bad request - must include color'}), 400
    

@app.get('/api/favorite_color')  
def show_all_colors():
    colors = db.get_all_colors()
    if colors is None:
        abort(500)
    else:
        color_list = [ {'name': color.name} for color in colors]
        return jsonify(color_list)


@app.delete('/admin/delete_all_colors')
def clear_db():
    db.delete_all_colors()
    return jsonify({'result': 'All favorite colors deleted'})


@app.errorhandler(400)
def handle_bad_request(e):
    logging.error(e)
    return 'Bad request', 400

@app.errorhandler(404)
def page_not_found(e):
    logging.error(e)
    return 'Not found', 404

@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return 'Server error', 500

if __name__ == '__main__':
    app.run()

