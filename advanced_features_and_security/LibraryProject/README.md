""
# Django Permissions Setup

This project demonstrates how to set up and enforce permissions using Django's groups and permissions system.

## Steps Implemented:

### Step 1: Define Custom Permissions
- Added custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) to the `Document` model.

### Step 2: Create and Configure Groups
- Created groups: `Viewers`, `Editors`, and `Admins`.
- Assigned permissions to these groups using a management script.

### Step 3: Enforce Permissions in Views
- Used `@permission_required` decorators to restrict access to views based on permissions.

### Step 4: Test Permissions
- Created test users and assigned them to groups.
- Verified permissions by logging in as test users and accessing different views.

### Step 5: Documentation
- Added inline comments and this README file to explain the setup.

## Testing Instructions:
1. Run the `configure_groups` management command:
 ```
   python manage.py configure_groups
   ```
2. Create test users in the Django admin and assign them to the appropriate groups.
3. Log in as different users and attempt to access the views for creating, editing, deleting, and viewing documents.
"""





jango Security Measures

## Step 1: Configure Secure Settings
- Set `DEBUG` to `False` in production.
- Enabled browser security headers: `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, and `SECURE_CONTENT_TYPE_NOSNIFF`.
- Enforced HTTPS cookies with `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE`.
- Added a basic Content Security Policy (CSP) using `django-csp` middleware.

## Step 2: Protect Views with CSRF Tokens
- Updated all templates with `{% csrf_token %}` for CSRF protection.

## Step 3: Secure Data Access in Views
- Used Django ORM to parameterize queries, avoiding SQL injection.
- Implemented input validation using Django forms in views handling user input.

## Step 4: Implement Content Security Policy (CSP)
- Configured CSP headers using `django-csp` middleware to restrict resource loading to the same domain.

## Step 5: Documentation and Testing
- Added comments in code for clarity.
- Conducted manual testing to ensure inputs are sanitized and secure headers are included in responses.

### Testing Checklist:
1. Verify CSRF protection by checking for CSRF tokens in forms.
2. Ensure SQL injection protection by attempting malicious inputs.
3. Test CSP by loading external resources and ensuring they are blocked.
"""
