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

Endpoint: 
```
localhost:8000/api/pricing-config/
```
HTTP Methods: GET, POST
Description: This endpoint is responsible for managing pricing configurations. It allows retrieving a list of all pricing configurations (GET), and creating a new pricing configuration (POST).

```
{
  "distance_base_price": 80.0,
  "distance_additional_price": 30.0,
  "time_multiplier_factor": 1.0,
  "waiting_charges": 5.0,
  "day_of_week": "Tue-Wed-Thur",
  "active": true
}



```

You will get the GET REQUEST on the below format

```
[
    {
        "id": 1,
        "distance_base_price": "80.00",
        "distance_additional_price": "30.00",
        "time_multiplier_factor": "1.00",
        "waiting_charges": "5.00",
        "day_of_week": "Tue-Wed-Thur",
        "active": true,
        "created_at": "2024-02-23T05:21:44.434311Z",
        "updated_at": "2024-02-23T05:21:44.435310Z",
        "last_modified_at": "2024-02-23T05:21:44.431342Z",
        "last_modified_by": null
    }
]

```

Views:
PricingConfigAPIView: Handles the GET and POST requests for pricing configurations.
Endpoint: 
```
localhost:8000/api/calculate-pricing/
```

HTTP Methods: POST
Description: This endpoint calculates the pricing based on input parameters such as distance, time, waiting duration, and the day of the week. It returns the calculated price.
Views:
CalculatePricingAPIView: Handles the POST request for calculating pricing.

```
{
  "distance": 10.5,
  "time": 2.5,
  "waiting_duration": 1.0,
  "day_of_week": "Tue-Wed-Thur"
}


```

Response:

```
{
    "price": 402.5
}

```

Using API Point logger-info will retrive the information of the log

```
localhost:8000/api/logger-info/
```

response

```
{"root_logger_level": "WARNING", "loggers": ["concurrent.futures", "asyncio", "django.dispatch", "django", "django.utils.autoreload", "django.template", "django.db.models", "django.db.backends", "django.request", "django.server", "django.security.csrf", "django.db.backends.base", "django.db.backends.schema", "django.test", "app.forms", "app.views"]}

```
## Testing

```
python manage.py test
```
