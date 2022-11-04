from flask_admin.contrib.sqla import ModelView

class IllegalDumpingAdminView(ModelView):
    column_searchable_list = (
        "vehicle",
    )
    column_editable_list = (
        "vehicle",
        "created_date"
    )
    column_filters = (
        "vehicle",
    )
    column_sortable_list = (
        "vehicle",
    )
    column_default_sort = ("created_date", True)
