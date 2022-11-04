from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash

class UsersAdminView(ModelView):
    column_searchable_list = (
        "username",
        "email",
    )
    column_editable_list = (
        "username",
        "email",
        "created_date",
        "password"
    )
    column_filters = (
        "username",
        "email",
    )
    column_sortable_list = (
        "username",
        "email",
        "active",
        "created_date",
    )
    column_default_sort = ("created_date", True)

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.password = generate_password_hash(model.password, method='sha256')
