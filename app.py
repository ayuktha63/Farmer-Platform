from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Static credentials
users = {
    'farmer': {'username': 'farmer', 'password': 'farmer'},
    'customer': {'username': 'customer', 'password': 'customer'},
    'retailer': {'username': 'retailer', 'password': 'retailer'}
}

# Load and prepare the model
data = pd.read_csv('crop_data.csv')
encoder = LabelEncoder()
data['SOIL_TYPE'] = encoder.fit_transform(data['SOIL_TYPE'])
X = data.drop('CROP', axis=1)
y = data['CROP']
crop_encoder = LabelEncoder()
y = crop_encoder.fit_transform(y)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/farmer_login', methods=['GET', 'POST'])
def farmer_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == users['farmer']['username'] and password == users['farmer']['password']:
            return redirect(url_for('farmer_dashboard'))
        else:
            return "Invalid credentials for farmer!", 401
    return render_template('farmer_login.html')

@app.route('/farmer_dashboard')
def farmer_dashboard():
    return render_template('farmer_dashboard.html')

@app.route('/customer_login', methods=['GET', 'POST'])
def customer_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == users['customer']['username'] and password == users['customer']['password']:
            return redirect(url_for('customer_dashboard'))
        else:
            return "Invalid credentials for customer!", 401
    return render_template('customer_login.html')

@app.route('/customer_dashboard')
def customer_dashboard():
    return render_template('customer_dashboard.html')

@app.route('/retailer_login', methods=['GET', 'POST'])
def retailer_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == users['retailer']['username'] and password == users['retailer']['password']:
            return redirect(url_for('retailer_dashboard'))
        else:
            return "Invalid credentials for retailer!", 401
    return render_template('retailer_login.html')

@app.route('/farm')
def farm():
    return render_template('farm.html')

@app.route('/crop_prediction', methods=['GET', 'POST'])
def crop_prediction():
    if request.method == 'POST':
        soil_type = request.form['soil_type']
        N_SOIL = float(request.form['N_SOIL'])
        P_SOIL = float(request.form['P_SOIL'])
        K_SOIL = float(request.form['K_SOIL'])
        TEMPERATURE = float(request.form['TEMPERATURE'])
        HUMIDITY = float(request.form['HUMIDITY'])
        pH = float(request.form['pH'])

        # Encode the SOIL_TYPE input
        soil_type_encoded = encoder.transform([soil_type])[0]

        # Create the input data for prediction
        input_data = [[soil_type_encoded, N_SOIL, P_SOIL, K_SOIL, TEMPERATURE, HUMIDITY, pH]]

        # Predict the best crop for the input data
        predicted_crop = model.predict(input_data)
        predicted_crop_name = crop_encoder.inverse_transform(predicted_crop)[0]

        return render_template('crop_prediction.html', result=predicted_crop_name)

    return render_template('crop_prediction.html', result=None)

@app.route('/growth')
def growth():
    return render_template('growth.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/retailer_dashboard')
def retailer_dashboard():
    return render_template('retailer_dashboard.html')
    
@app.route('/irrigation_system')
def irrigation_system():
    return render_template('irrigation_system.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
