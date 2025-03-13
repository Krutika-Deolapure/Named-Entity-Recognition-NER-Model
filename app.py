from flask import Flask, request, jsonify
import spacy
import pickle
from pathlib import Path, PosixPath, WindowsPath

app = Flask(__name__)

# Function to load the model with path conversion
def load_model_with_path_conversion(model_path):
    # Custom unpickler to convert PosixPath to WindowsPath
    class CustomUnpickler(pickle.Unpickler):
        def find_class(self, module, name):
            if module == 'pathlib' and name == 'PosixPath':
                return WindowsPath
            return super().find_class(module, name)
    
    with open(model_path, 'rb') as f:
        model = CustomUnpickler(f).load()
    return model

# Load the trained model
model_path = "optimized_ner_model.pkl"
ner_model = load_model_with_path_conversion(model_path)

# Basic Authentication
def check_auth(username, password):
    return username == 'admin' and password == 'password'

def authenticate():
    return jsonify({"message": "Authentication required"}), 401

def requires_auth(f):
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/predict', methods=['POST'])
@requires_auth
def predict():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "Text is required"}), 400
    
    doc = ner_model(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return jsonify({"entities": entities})

if __name__ == '__main__':
    app.run(debug=True)