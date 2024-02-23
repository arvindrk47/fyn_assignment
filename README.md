### Installation

Provide step-by-step instructions to install and set up the project.

```
# Clone the repository
git clone https://github.com/your-username/your-project.git

# Change into the project directory
cd your-project

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# (Command may vary based on the operating system)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

```

Usage
Explain how to use or run the project.

```
# Run the development server
python manage.py runserver
```

# Run the development server

python manage.py runserver
Visit http://localhost:8000/ in your browser to view the application.

## API Endpoints
Endpoint: /api/pricing-config/

HTTP Methods: GET, POST
Description: This endpoint is responsible for managing pricing configurations. It allows retrieving a list of all pricing configurations (GET), and creating a new pricing configuration (POST).
Views:
PricingConfigAPIView: Handles the GET and POST requests for pricing configurations.
Endpoint: /api/calculate-pricing/

HTTP Methods: POST
Description: This endpoint calculates the pricing based on input parameters such as distance, time, waiting duration, and the day of the week. It returns the calculated price.
Views:
CalculatePricingAPIView: Handles the POST request for calculating pricing.


## Testing

```
python manage.py test
```
