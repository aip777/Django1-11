from django.contrib.auth import get_user_model

User = get_user_model()
# my followers
random_ = User.objects.last()

# who I follow

random_.is_following.all()
