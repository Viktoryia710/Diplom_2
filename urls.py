class URL:
    BASE_URL = "https://qa-stellarburgers.education-services.ru"
    
    CREATE_USER = f"{BASE_URL}/api/auth/register"
    LOGIN_USER = f"{BASE_URL}/api/auth/login"
    USER_DATA = f"{BASE_URL}/api/auth/user"
    
    CREATE_ORDER = f"{BASE_URL}/api/orders"
    GET_ORDERS = f"{BASE_URL}/api/orders"
    GET_INGREDIENTS = f"{BASE_URL}/api/ingredients"