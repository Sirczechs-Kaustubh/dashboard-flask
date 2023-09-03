import datetime
import dbm
import gettext
from pyexpat import model
from flask_login import current_user
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import ModelView
from flask import Flask, abort, redirect, render_template, url_for, request
from flask_admin import BaseView, expose
import sqlite3
import string
import random
from flask_admin.model import typefmt
from flask_sqlalchemy import SQLAlchemy
from markupsafe import Markup



# from app import generate_id,process_data
# from app import generate_id

##app = Flask(__name__)
##db = SQLAlchemy()


class MyModelView(sqla.ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        next_page = request.args.get('next')
        return redirect(next_page or url_for('login'))

    

class usernameview(MyModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        next_page = request.args.get('next')
        return redirect(next_page or url_for('login'))

    

class dashboardView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        next_page = request.args.get('next')
        return redirect(next_page or url_for('login'))
    
    @expose('/')
    def index(self):
        return self.render('admin/dashboard.html')

class pickupDetails(MyModelView):

    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        next_page = request.args.get('next')
        return redirect(next_page or url_for('login'))

    column_display_pk = True
    column_default_sort = ('pickup_id', True)
    #form_columns = ['id', 'desc']
    column_searchable_list = ['pickup_id', 'sample_id',
                              'picked_by', 'picked_date', 'remarks', 'created_by']
    column_filters = ['pickup_id', 'sample_id',
                      'picked_by', 'picked_date', 'remarks', 'created_by']
    column_editable_list = ['picked_by', 'picked_date','remarks']
    can_create = True
    can_edit = True
    column_list = ('pickup_id', 'sample_id', 'picked_by',
                   'picked_date', 'remarks', 'created_by')
    can_view_details = True
    page_size = 50
    create_modal = True
    edit_modal = True
    can_export = True
    @property
    def can_delete(self):
        if (current_user.username=='admin'):
            return True
        return False

    # form_columns = ['picked_by', 'picked_date', 'remarks']

# 4


class receiveDetails(MyModelView):

    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        next_page = request.args.get('next')
        return redirect(next_page or url_for('login'))

    column_display_pk = True
    column_default_sort = ('receive_id', True)
    column_searchable_list = ['receive_id', 'sample_id', 'received_by', 'received_date',
                              'remarks', 'created_by', 'vet_remarks', 'vetremarks_updated_by']
    column_filters = ['receive_id', 'sample_id', 'received_by', 'received_date', 'remarks',
                      'created_by', 'vet_remarks', 'vetremarks_updated_by']
    column_editable_list = ['remarks', 'vet_remarks',
                            'received_by', 'received_date', 'vetremarks_updated_by']
    can_create = True
    can_edit = True
    column_list = ('receive_id', 'sample_id', 'received_by', 'received_date', 'remarks',
                   'created_by', 'vet_remarks', 'vetremarks_updated_by')
    can_view_details = True
    page_size = 50
    create_modal = True
    edit_modal = True
    can_export = True

    @property
    def can_delete(self):
        if (current_user.username=='admin'):
            return True
        return False
# 5



# 6


class Allspecies(MyModelView):

    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        next_page = request.args.get('next')
        return redirect(next_page or url_for('login'))

    column_display_pk = True
    column_default_sort = ('species_id', False)
    #form_columns = ['id', 'desc']
    column_searchable_list = ['species_id', 'species_name']
    column_filters = ['species_id', 'species_name']
    column_editable_list = ['species_name']
    can_create = True
    can_edit = True
    column_list = ('species_id', 'species_name')
    can_view_details = True
    page_size = 50
    create_modal = True
    edit_modal = True
    can_export = True

# 7


class Allspecimen(MyModelView):

    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        next_page = request.args.get('next')
        return redirect(next_page or url_for('login'))

    column_display_pk = True
    column_default_sort = ('specimen_id', False)
    #form_columns = ['id', 'desc']
    column_searchable_list = ['specimen_id', 'specimen_name']
    column_filters = ['specimen_id', 'specimen_name']
    column_editable_list = ['specimen_name']
    can_create = True
    can_edit = True
    column_list = ('specimen_id', 'specimen_name')
    can_view_details = True
    page_size = 50
    create_modal = True
    edit_modal = True
    can_export = True

# 8

# 9


class ourEmployee(MyModelView):

    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        next_page = request.args.get('next')
        return redirect(next_page or url_for('login'))

    column_display_pk = True
    column_default_sort = ('id', False)
    #form_columns = ['id', 'desc']
    column_searchable_list = ['id', 'emp_id', 'emp_name', 'password', 'designation',
                              'status', 'email_id', 'phone_no', 'address', 'location', 'usercode']
    column_filters = ['id', 'emp_id', 'emp_name', 'password', 'designation',
                      'status', 'email_id', 'phone_no', 'address', 'location', 'usercode']
    column_editable_list = ['emp_id', 'emp_name', 'password', 'designation',
                            'status', 'email_id', 'phone_no', 'address', 'location', 'usercode']
    can_create = True
    can_edit = True
    column_list = ('id', 'emp_id', 'emp_name', 'password', 'designation',
                   'status', 'email_id', 'phone_no', 'address', 'location', 'usercode')
    can_view_details = True
    page_size = 50
    create_modal = True
    edit_modal = True
    can_export = True

# 10


# 11
class locationViews(MyModelView):

    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        next_page = request.args.get('next')
        return redirect(next_page or url_for('login'))

    column_display_pk = True
    column_default_sort = ('location_id', False)
    #form_columns = ['id', 'desc']
    column_searchable_list = ['location_id', 'location_name']
    column_filters = ['location_id', 'location_name']
    column_editable_list = ['location_name']
    can_create = True
    can_edit = True
    column_list = ('location_id', 'location_name')
    can_view_details = True
    page_size = 50
    create_modal = True
    edit_modal = True
    can_export = True
    form_columns = ['location_name']


# 12
class clinicalTestViews(MyModelView):

    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        next_page = request.args.get('next')
        return redirect(next_page or url_for('login'))

    column_display_pk = True
    column_default_sort = ('clinicalTest_id',  False)
    #form_columns = ['id', 'desc']
    column_searchable_list = ['clinicalTest_id', 'clinicalTest_name']
    column_filters = ['clinicalTest_id', 'clinicalTest_name']
    column_editable_list = ['clinicalTest_name']
    can_create = True
    can_edit = True
    column_list = ('clinicalTest_id', 'clinicalTest_name')
    can_view_details = True
    page_size = 50
    create_modal = True
    edit_modal = True
    can_export = True


class finalTestTableView(MyModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        next_page = request.args.get('next')
        return redirect(next_page or url_for('login'))

    column_display_pk = False
    column_default_sort = ('test_id',  True)
    #form_columns = ['id', 'desc']
    column_searchable_list = ['test_id', 'sample_id', 'sample_code', 'client_name',
                              'test_name', 'outcome_result', 'city_name', 'created_date']
    column_filters = ['test_id', 'sample_id', 'sample_code', 'client_name',
                      'test_name', 'outcome_result', 'city_name', 'created_date']
    column_editable_list = []
    can_create = False
    can_edit = False
    column_list = ('test_id', 'sample_id', 'sample_code', 'client_name',
                   'test_name', 'outcome_result', 'city_name', 'created_date')
    can_view_details = True
    page_size = 50
    create_modal = True
    edit_modal = False
    can_export = True
    can_delete=True
