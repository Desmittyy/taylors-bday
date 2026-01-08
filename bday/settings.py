# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-78jl*#*19**1gx8kj)m3b(79@rx%ri8m^*rp*=e_7!_qmlym5$'  # Use environment variable in production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['tay-bakes.com', '18.188.172.106', 'www.tay-bakes.com']
# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = '/home/ec2-user/taylors-bday/bday/app/static'

# If you have static folders in your apps, add this too:
STATICFILES_DIRS = [
    # BASE_DIR / 'static',  # Uncomment if you have a project-level static folder
]

# Media files (if you're handling user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = '/ec2-user/taylors-bday/bday/app/media'
