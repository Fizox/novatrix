# Novatrix Digital - Deployment Guide

## 🚀 Production Deployment Checklist

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Configuration
- Copy `.env.example` to `.env`
- Update the following in `.env`:
  - `SECRET_KEY`: Generate a new secret key (use Django's `get_random_secret_key()`)
  - `DEBUG`: Set to `False`
  - `ALLOWED_HOSTS`: Add your domain name(s)

### 3. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 5. Security Checklist
- ✅ SECRET_KEY is using environment variable
- ✅ DEBUG is set to False in production
- ✅ ALLOWED_HOSTS is properly configured
- ✅ HTTPS/SSL configured (required for production)
- ✅ WhiteNoise configured for static files
- ✅ Security middleware enabled
- ✅ CSRF protection enabled
- ✅ SQL injection protection (Django ORM)

### 6. Deployment Options

#### Option A: Heroku
```bash
# Install Heroku CLI and login
heroku login

# Create new app
heroku create your-app-name

# Set environment variables
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

#### Option B: VPS (DigitalOcean, AWS, etc.)
```bash
# Install dependencies
sudo apt update
sudo apt install python3-pip python3-venv nginx

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure Gunicorn
gunicorn --bind 0.0.0.0:8000 project.wsgi

# Setup Nginx as reverse proxy
# Configure SSL with Let's Encrypt
```

#### Option C: PythonAnywhere
1. Upload project files
2. Create virtual environment
3. Configure WSGI file
4. Set environment variables
5. Reload web app

### 7. Post-Deployment
- Test contact form functionality
- Verify static files are loading
- Check all pages load correctly
- Test on mobile devices
- Monitor error logs

### 8. Maintenance
```bash
# View logs
tail -f logs/django.log

# Backup database
python manage.py dumpdata > backup.json

# Update dependencies
pip install --upgrade -r requirements.txt
```

## 📧 Contact Form Configuration
The contact form is configured to accept:
- Full name (required, min 2 characters)
- Company name (required)
- Email (required, valid format)
- Phone number (required, max 15 characters, digits and + only)
- Current website (optional, valid URL)
- Service needed (required, dropdown)
- Project description (required, min 10 characters)

## 🔒 Security Features Enabled
- CSRF protection
- XSS filtering
- Content type nosniff
- SSL redirect (production only)
- Secure cookies (production only)
- HSTS headers (production only)
- Clickjacking protection

## 📝 Notes
- Database: SQLite (development) - Switch to PostgreSQL for production
- Static files: Served by WhiteNoise
- Forms: Client-side and server-side validation
- Email: Configure SMTP settings in .env for contact form emails
