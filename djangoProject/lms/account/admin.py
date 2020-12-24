from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

# Register your models here.

# class AccountAdmin(UserAdmin):
#     list_display = ('email', 'username', 'date_joined', 'is_admin','is_staff')
#     search_fields = ('email', 'username')
#     readonly_fields = ('date_joined', 'last_login')

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

# admin.site.register(Account, AccountAdmin)


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = '__all__'

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = '__all__'

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class AccountAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    ordering = ('email',)
    fieldsets = ()
    list_filter = ('is_admin','is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('fName', 'mName', 'lName', 'streetAddr',
                                      'district', 'state', 'pinCode', 'phoneNum', 'salary', 'USN', 'course', 'sem')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser',
                                    'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fName', 'mName', 'lName', 'streetAddr',
                       'district', 'state', 'pinCode', 'phoneNum', 'salary', 'USN',
                       'course', 'sem', 'password1', 'password2'),
        }),
    )


# Now register the new UserAdmin...
admin.site.register(Account, AccountAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)
