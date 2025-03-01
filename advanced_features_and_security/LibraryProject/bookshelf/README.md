# Permission and Group Setup in Django

This application utilizes custom permissions and user groups to control access:
- **Permissions**: can_view, can_create, can_edit, can_delete (added to the Post model).
- **Groups**:
  - **Viewers**: can only view posts.
  - **Editors**: can create, edit, and view posts.
  - **Admins**: can perform all actions (view, create, edit, delete).

Test users are assigned to these groups to verify correct access control.
