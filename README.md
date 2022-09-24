# Project: Test Django Migration
When working with django models, I found some bug which I think could be improved. 
- As a solution to solve the bug, I have proposed a solution with associated description and created a pull request. The pull request is available at: https://github.com/django/django/pull/16080
- The associated Ticket is available at: https://code.djangoproject.com/ticket/34050
Because of the improper name of the generated migrations file, `python manage.py migrate` was not able to detect the newly generated migrations file. This can be looked at the commit stage: [Commit with migration file containing `.` in file name excluding `.py` extension](https://github.com/bisalgt/test-django-migrations/commit/7624f46c1c2cd2d46705e2f0f255739104ffd116)
As a solution, the description of constraint was changed which resulted in proper migration file name, as available in commit: [Commit with changed name of constraint that gives migration file with proper name](https://github.com/bisalgt/test-django-migrations/commit/ffc9ab81ecd38848da02490f50881ba1c40efe9a) Now the migration file is detected by `migrate` command.
