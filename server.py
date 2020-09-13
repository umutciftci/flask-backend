from flask import Flask, jsonify ,request
from multiprocessing import Value

counter = Value('i',0)
app = Flask(__name__)

d = []

def id_generator():
    with counter.get_lock():
        counter.value += 1
        return counter.value

@app.route('/keys', methods=['GET'])
def list():
    return jsonify(d)

@app.route('/keys/<int:_id>', methods=['GET'])
def get(_id):
    for data in d:
        if _id == data['id']:
            selected_data = data
            return jsonify(selected_data)
        else : 
            return jsonify({'error': 'Object does not exist'}), 404


@app.route('/keys', methods=['PUT'])
def index():
    data = request.json
    data['id'] = id_generator()
    d.append(data)
    return jsonify({'message': 'Object created'}), 201

@app.route('/keys/<int:_id>', methods=['HEAD'])
def exists(_id):
    for data in d:
        if _id == data['id']:
            return jsonify({'message': 'Object exists'})
        else : 
            return jsonify({'error': 'Object does not exist'}), 404


@app.route('/keys', methods=['DELETE'])
def clear():
    global d
    d= []
    return jsonify({"message": "Objects deleted"}), 200


@app.route('/keys/<int:_id>', methods=['DELETE'])
def delete(_id):
    for data in d:
        if _id == data['id']: 
            deleted_user = (item for item in d if item['id'] == _id).__next__()
            d.remove(deleted_user)
            return jsonify({"message": "Object deleted"}), 200
        else :
            return jsonify({'error': 'Object does not exist'}), 404
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)