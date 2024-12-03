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