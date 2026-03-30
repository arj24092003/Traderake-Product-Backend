def set_email_verified(backend, user, response, *args, **kwargs):
    """
    Sets the email_verified flag to True for users who sign in via Google.
    Google verifies email addresses, so we can trust it.
    """
    if backend.name == 'google-oauth2':
        if not user.email_verified:
            user.email_verified = True
            user.save(update_fields=['email_verified'])
