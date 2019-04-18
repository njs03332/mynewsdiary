from django.core.management.base import BaseCommand
import random
from django.contrib.auth.models import User
from newsdiary.models import *
from faker import Faker 
from datetime import datetime
from django.utils import timezone

# python manage.py seed --mode=refresh

class Command(BaseCommand):
    help = "seed database for testing and development."
    enfake = Faker()
    kofake = Faker('ko_KR')

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    # logger.info("Delete all model instances")
    User.objects.all().delete()
    Issue.objects.all().delete()
    Event.objects.all().delete()
    Article.objects.all().delete()
    Journalist.objects.all().delete()
    Memo.objects.all().delete()
    Noti.objects.all().delete()
    NonregularNoti.objects.all().delete()

# def create_superuser():
#     user = User.objects.create_user(
#         username="superuser",
#         password="abababab"
#     )
#     return user
    
def create_users(self):
    """Creates user objects combining different elements from the list"""
    # logger.info("Creating user")

    genders = ["여성", "남성", "기타"]
    # street_localities = ["Bakers Street", "Rajori Gardens", "Park Street", "MG Road", "Indiranagar"]
    # pincodes = ["101234", "101232", "101231", "101236", "101239"]

    for i in range(1,6):
        username = "user" + str(i)
        user = User.objects.create_superuser(
            username=username,
            password='abababab',
            email='a@a.com'
        )
        user.profile.name = self.kofake.name()
        user.profile.gender = random.choice(genders)
        user.profile.age = random.randint(15,30)
        user.save()
    # logger.info("{} user created.".format(user))
    return

def create_issues():
    issue1 = Issue.objects.create(
            title="4.3 보궐선거",
            categories=['POL']
    )
    issue2 = Issue.objects.create(
            title="헌재 인사청문회",
            categories=['POL']
    )
    issue3 = Issue.objects.create(
            title="낙태죄 폐지",
            categories=['POL', 'SOC']
    )
    issue4 = Issue.objects.create(
            title="후쿠시마 수산물 수입 금지",
            categories=['POL']
    )
    issues = [issue1, issue2, issue3, issue4]
    for issue in issues:
        issue.followers.add(User.objects.order_by("?").first(), User.objects.order_by("?").first())
        issue.save()
    return

def create_events(self):
    # event1 = Event.objects.create(
        
    # )
    categories = ['POL', 'SOC', 'ECON', 'WRD']
    for i in range(9):
        dt = datetime(2019, 4, i*3+4)
        dt_aware = timezone.make_aware(dt)
        event = Event.objects.create(
            title=self.kofake.catch_phrase(),
            concept=self.kofake.text(max_nb_chars=50, ext_word_list=None),
            issue=Issue.objects.order_by("?").first(),
            datetime=dt_aware,
            category=random.choice(categories)
        )
    return

def create_articles(self):
    first_event = Event.objects.first().id
    for i in range(5):
        article = Article.objects.create(
            created_at=timezone.now(),
            updated_at=timezone.now(),
            title=self.kofake.catch_phrase(),
            press='한겨레',
            issue=Issue.objects.order_by("?").first()
        )
    for i in range(30):
        article = Article.objects.create(
            created_at=timezone.now(),
            updated_at=timezone.now(),
            title=self.kofake.catch_phrase(),
            press='jtbc뉴스',
            event=Event.objects.order_by("?").first()
        )
    for i in range(9):
        article = Article.objects.create(
            created_at=timezone.now(),
            updated_at=timezone.now(),
            title=self.kofake.catch_phrase(),
            press='연합뉴스',
            parent_event=Event.objects.get(pk=first_event)
        )
        first_event += 1

# def create_journalists():




def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == "clear":
        return

    # Creating instances
    # create_superuser()
    # for i in range(5):
    create_users(self)
    create_issues()
    create_events(self)
    create_articles(self)
    # create_journalists()