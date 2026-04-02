# accounts/utils.py

GROUP_EMAILS = [
    'firoszufa20@gmail.com',
    'firos.aqiela@ui.ac.id',

]

def check_is_group_member(user):
    # Cek apakah user sudah login dan emailnya terdaftar di kelompok
    if user.is_authenticated and user.email in GROUP_EMAILS:
        return True
    return False