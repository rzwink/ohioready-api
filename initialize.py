import os

import django
import dotenv

dotenv.read_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ohioready.settings")

django.setup()

from django.contrib.auth import get_user_model  # noqa
from django.contrib.auth.models import Group  # noqa

from api.models import Publisher, Authorizer, Event

INITIALIZE = os.environ.get("INITIALIZE", False)

if INITIALIZE:
    print("Initializing")
    User = get_user_model()
    try:
        admin_user = User.objects.create_superuser(
            "admin", "rzwink@gmail.com", os.environ.get("INIT_PASS")
        )
    except django.db.utils.IntegrityError:
        pass

    users_list = [
        "rob@zwink.net",
    ]
    groups_list = [
        "publishers",
        "editors",
    ]

    authorizer_list = [
        "Ohio Department of Health",
        "World Health Organizations",
        "Health and Human Services Secretary, Alex M. Azar II",
        "CDC",
        "Governor",
        "Governor of Ohio and Mayor of Columbus",
        "President of Ohio State",
        "The Columbus Foudnation",
    ]

    publishers = [
        {
            "name": "State of Ohio",
            "homepage_url": "https://www.ohio.gov",
            "type": "STATE",
            "phone": "+16145551233",
            "email": "info@ohio.gov",
        },
        {
            "name": "City of Columbus Mayor",
            "homepage_url": "https://www.columbus.gov/columbus-news/",
            "type": "LOCAL",
            "phone": "+16145551231",
            "email": "info@example.gov",
        },
        {
            "name": "Columbus City Council",
            "homepage_url": "https://www.example.com",
            "type": "LOCAL",
            "phone": "+16145551266",
            "email": "info@example.gov",
        },
    ]

    for pub in publishers:
        try:
            publisher, created = Publisher.objects.get_or_create(**pub)
        except django.db.utils.IntegrityError:
            pass

    for authorizer in authorizer_list:
        try:
            Authorizer.objects.get_or_create(name=authorizer)
        except django.db.utils.IntegrityError:
            pass

    for name in groups_list:
        try:
            group, created = Group.objects.get_or_create(name=name)
        except django.db.utils.IntegrityError:
            pass

    for user in users_list:
        try:
            user = User.objects.create_user(
                user, user, os.environ.get("INIT_PASS"), is_staff=True
            )
            Group.objects.get(name="publishers").user_set.add(user)
            Group.objects.get(name="editors").user_set.add(user)
        except django.db.utils.IntegrityError:
            pass
