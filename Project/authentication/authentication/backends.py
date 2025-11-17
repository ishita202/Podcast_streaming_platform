import logging
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()
logger = logging.getLogger(__name__)

class EmailOrUsernameBackend(ModelBackend):
    """Custom authentication backend to allow login with both email and username."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        logger.info(f"Authentication attempt for: {username}")

        user = None
        try:
            # Check if input is an email or username
            if '@' in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)

        except User.DoesNotExist:
            logger.warning(f"Authentication failed: User not found ({username})")
            return None  # User does not exist
        
        # Check password
        if user and user.check_password(password):
            logger.info(f"Authentication successful: {username}")
            return user  # Return authenticated user
        
        logger.warning(f"Authentication failed: Invalid password ({username})")
        return None  # Invalid credentials
