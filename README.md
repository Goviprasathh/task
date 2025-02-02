# Overview
This project is a Django-based multilingual FAQ system designed to allow users to manage frequently asked questions (FAQs) in multiple languages. 
The backend test evaluates proficiency in Django, API development, multilingual support, and integration of tools like WYSIWYG editors.

# Features
Multilingual Support: Enables storing and retrieving FAQs in multiple languages. API Development: Implements REST APIs for 
CRUD operations on FAQs. WYSIWYG Editor Integration: Allows rich text formatting for the FAQ content. 
Dockerized Setup: Simplifies deployment and setup using Docker. Efficient Caching: Ensures faster performance for frequently accessed FAQs.

| Feature        | Description                  |
|----------------|------------------------------|
| Multilingual   | Supports multiple languages |
| WYSIWYG Editor | Rich-text content editing   |

**Challenges and Solutions**

1.Setting Up Multilingual Support
  Implementing multilingual support in Django was complex, as it required understanding how gettext works and integrating it seamlessly into the project.
__Solution__: 
  I referred to Django's documentation on translation and localization, used django-admin makemessages and compilemessages, and tested translations across multiple languages to ensure proper functionality.

2.Integrating the WYSIWYG Editor

  Choosing the right WYSIWYG editor for rich-text content formatting and ensuring compatibility with Django forms. Additionally, 
  integrating the editor required serving static files correctly in production, 
  which caused errors initially. Solution: After evaluating several editors like TinyMCE and CKEditor,
  I opted for Django CKEditor due to its built-in support for Django. I debugged static file issues by ensuring STATICFILES_DIRS and STATIC_ROOT were properly configured in the settings file.

3.Deploying with Docker

  Setting up Docker for the first time, especially creating the Dockerfile and docker-compose.yml, was challenging as 
  I encountered network-related issues and dependency conflicts. Solution: I read Docker's official documentation and tested the setup incrementally
  First, I containerized only the Django application. 
  Then, I added the database service and linked it via docker-compose. Solved dependency conflicts by pinning package versions in the requirements.txt file.

4.Handling HTTP 400 Bad Request for API
  I encountered an issue where the API returned an HTTP 400 error with the message:
  **{ "question": ["This field is required."]**
  **"answer": ["This field is required."] }**
  Solution: 
    This was caused by an incorrect POST request format. I resolved it by: Testing the API with Postman to identify the correct payload structure. 
    Updated the documentation in the README to include a clear API usage example: json Copy Edit 
    **{ "question": "What is this project?", 
    "answer": "A Django-based multilingual FAQ system."
    }**

5.Debugging Static Files in Production
  Static files were not loading in production, which broke the admin interface and WYSIWYG editor. Solution: Configured the STATIC_URL and STATIC_ROOT in settings.py. 
  Ran python manage.py collectstaticand verified the files were properly copied. Ensured the web server (PythonAnywhere) was correctly serving the static files directory.

6.Database Connection Issues
  While setting up a database for the Dockerized application, I encountered connectivity issues between the Django app and the database container.
  Solution: Updated the DATABASES configuration in settings.py to usen the correct host (db) as defined in the docker-compose.yml. 
  Verified the database service was running and reachable using docker-compose logs.

# 🎯 API Usage Endpoint: 
    - /faqs/ Method: POST
# Lessons Learned
  Debugging: Efficiently used logs and error messages to identify and resolve issues during deployment. Improved debugging skills
  by analyzing logs and fixing deployment issues Deployment: Gained hands-on experience in deploying 
  Django projects to cloud platforms. Best Practices: Followed proper documentation, version control, and dependency management for a smooth workflow. 
  Gained a deeper understanding of Django's internationalization and static file management. Learned to work with Docker
  for containerized deployment and resolve network-related issues. Enhanced problem-solving abilities when integrating third-party libraries like CKEditor.

**Future Improvements**
  Advanced Caching: Plan to integrate Redis for faster performance. Authentication: Add user management features for secure FAQ access and updates. Frontend Development: Build a user-friendly interface for managing FAQs.

# 🧑‍💻 Author Name: GOVI PRASATH R 
# 0Email: goviprasath18@gmail.com
