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
            title="한미 방위비 협정",
            categories=['POL']
    )
    issue3 = Issue.objects.create(
            title="5.18 피의자 전두환",
            categories=['POL', 'SOC']
    )
    issue4 = Issue.objects.create(
            title="헌재 인사청문회",
            categories=['POL']
    )
    issue5 = Issue.objects.create(
            title="낙태죄 판결",
            categories=['SOC']
    )
    issue6 = Issue.objects.create(
            title="한미 정상회담",
            categories=['POL', 'WLD']
    )
    issue7 = Issue.objects.create(
            title="WTO 판결",
            categories=['ECON', 'WLD']
    )
    issue8 = Issue.objects.create(
            title="브렉시트",
            categories=['WLD']
    )
    issue9 = Issue.objects.create(
            title="패스트트랙",
            categories=['POL']
    )
    issue10 = Issue.objects.create(
            title="미세먼지 추경안 제출",
            categories=['POL']
    )
    # issues = [issue1, issue2, issue3, issue4, issue5, issue6, issue7, issue8, issue9, issue10]
    # for issue in issues:
    #     if issue.id % 3 == 0:
    #         issue.followers.add(User.objects.order_by("?").first(), User.objects.order_by("?").first(), User.objects.order_by("?").first(), User.objects.order_by("?").first(), User.objects.order_by("?").first())
    #     elif issue.id % 3 == 1:
    #         issue.followers.add(User.objects.order_by("?").first(), User.objects.order_by("?").first(), User.objects.order_by("?").first())
    #     else:
    #         issue.followers.add(User.objects.order_by("?").first(), User.objects.order_by("?").first(), User.objects.order_by("?").first(), User.objects.order_by("?").first())
    #     issue.save()
    return

def create_events(self):
    # event1 = Event.objects.create(
        
    # )
    # categories = ['POL', 'SOC', 'ECON', 'WRD']
    # for i in range(9):
    #     dt = datetime(2019, 4, i*3+4)
    #     dt_aware = timezone.make_aware(dt)
    #     event = Event.objects.create(
    #         title=self.kofake.catch_phrase(),
    #         concept=self.kofake.text(max_nb_chars=50, ext_word_list=None),
    #         issue=Issue.objects.order_by("?").first(),
    #         datetime=dt_aware,
    #         category=random.choice(categories)
    #     )

    event1 = Event.objects.create(
        title="4.3 보궐선거",
        concept="당선인이 임기 개시 이후에 범법 행위로 피선거권을 상실하거나 사망, 사퇴 등의 사유로 궐석이 되었을 때 실시하는 선거야!",
        background="창원시 성산구는 고 노회찬 의원의 사망, 통영시 고성군은 이군현 의원의 피선거권 상실 때문이지 ㅠ_ㅠ",
        category='POL',
        datetime=timezone.make_aware(datetime(2019, 4, 3)),
        issue=Issue.objects.get(title="4.3 보궐선거")
    )
    event2 = Event.objects.create(
        title="헌재 인사청문회 ",
        concept="국회가 대통령이 임명한 고위 공직자의 자질, 능력을 검증하는 제도야.",
        background="조용호, 서기석 헌법재판관이 4월 19일까지만 임기를 수행하고 퇴임하기 때문이야. 재판관 공백 사태를 방지하기 위해, 문재인 대통령이 신임 헌법재판관을 지명하고, 국회 법제사법위원회가 인사청문회를 열어 후보자 적격 여부를 심사해야 해.",
        category='POL',
        datetime=timezone.make_aware(datetime(2019, 4, 9)),
        issue=Issue.objects.get(title="헌재 인사청문회")
    )
    event3 = Event.objects.create(
        title="낙태죄 판결",
        concept="형법 269조로, 부녀가 태아를 자연분만기에 앞서 인위적인 방법으로 모체 밖으로 배출시키거나 약물 등으로 모체 안에서 제거하는 경우 성립하는 범죄야.",
        background="주심인 조용호 재판관이 4월 19일 퇴임 전에 사건을 마무리하려는 의지가 강하대.",
        category='SOC',
        datetime=timezone.make_aware(datetime(2019, 4, 11)),
        issue=Issue.objects.get(title="낙태죄 판결")
    )
    event4 = Event.objects.create(
        title="WTO 판결",
        concept="WTO는 세계무역기구야! 관세 및 무역에 관한 일반 협정을 흡수, 통합해서 세계 무역 질서를 세우고 UR 협정의 이행을 감시하는 역할을 해.",
        background="2011년에 후쿠시마 원전 사고 이후, 일본산 수산물의 방사능 안전 위험이 높아졌어. 우리 정부는 후쿠시마 인근 8개 현에서 어획된 수산물 수입을 금지하는 임시특별조처를 내렸지. 그런데 일본 정부가 “한국 정부가 일본 수산물을 차별하고 있다”며 WTO에 제소를 하게 된거야. 이에 따라 우리 정부는 WTO의 분쟁 해결 절차에 도입하게 되었어. 우리 정부는 2018년 2월, 1심에서 패소를 했어. 이에 다시 상소하기로 결정을 했고, 그래서 이번에 2심이 열리게 된거지.",
        category='ECON',
        datetime=timezone.make_aware(datetime(2019, 4, 12)),
        issue=Issue.objects.get(title="WTO 판결")
    )
    event5 = Event.objects.create(
        title="한미 방위비 협정",
        category='WRD',
        datetime=timezone.make_aware(datetime(2019, 4, 5)),
        issue=Issue.objects.get(title="한미 방위비 협정")
    )
    event6 = Event.objects.create(
        title="전두환 출석",
        category='SOC',
        datetime=timezone.make_aware(datetime(2019, 4, 8)),
        issue=Issue.objects.get(title="5.18 피의자 전두환")
    )
    event7 = Event.objects.create(
        title="브렉시트",
        category='WRD',
        datetime=timezone.make_aware(datetime(2019, 4, 12)),
        issue=Issue.objects.get(title="브렉시트")
    )
    event8 = Event.objects.create(
        title="바른미래당 회의",
        category='POL',
        datetime=timezone.make_aware(datetime(2019, 4, 17)),
    )
    event9 = Event.objects.create(
        title="미세먼지 추경안 제출",
        category='SOC',
        datetime=timezone.make_aware(datetime(2019, 4, 25)),
    )
    event11 = Event.objects.create(
        title="이미선 임명?",
        category='POL',
        datetime=timezone.make_aware(datetime(2019, 4, 19)),
        issue=Issue.objects.get(title="헌재 인사청문회")
    )
    event12 = Event.objects.create(
        title="윤중천 구속여부 심사일",
        category='ECON',
        datetime=timezone.make_aware(datetime(2019, 4, 19))
    )
    event13 = Event.objects.create(
        title="한국당 이미선 고발",
        category='POL',
        datetime=timezone.make_aware(datetime(2019, 4, 15)),
        issue=Issue.objects.get(title="헌재 인사청문회")
    )
    event14 = Event.objects.create(
        title="김경수 공판 기일",
        category='ECON',
        datetime=timezone.make_aware(datetime(2019, 4, 25))
    )
    # events = [event1, event2, event3, event4, event5, event6, event7, event8, event9, event11, event12, event13, event14]
    # for event in events:
    #     if event.id % 3 == 0:
    #         event.followers.add(User.objects.order_by("?").first(), User.objects.order_by("?").first(), User.objects.order_by("?").first(), User.objects.order_by("?").first(), User.objects.order_by("?").first())
    #     elif event.id % 3 == 1:
    #         event.followers.add(User.objects.order_by("?").first(), User.objects.order_by("?").first(), User.objects.order_by("?").first())
    #     else:
    #         event.followers.add(User.objects.order_by("?").first(), User.objects.order_by("?").first(), User.objects.order_by("?").first(), User.objects.order_by("?").first())
    #     event.save()
    return

def create_articles(self):
    # first_event = Event.objects.first().id
    # for i in range(5):
    #     article = Article.objects.create(
    #         created_at=timezone.now(),
    #         updated_at=timezone.now(),
    #         title=self.kofake.catch_phrase(),
    #         press='한겨레',
    #         issue=Issue.objects.order_by("?").first()
    #     )
    # for i in range(30):
    #     article = Article.objects.create(
    #         created_at=timezone.now(),
    #         updated_at=timezone.now(),
    #         title=self.kofake.catch_phrase(),
    #         press='jtbc뉴스',
    #         event=Event.objects.order_by("?").first()
    #     )
    # for i in range(4):
    #     article = Article.objects.create(
    #         created_at=timezone.now(),
    #         updated_at=timezone.now(),
    #         title=self.kofake.catch_phrase(),
    #         press='연합뉴스',
    #         parent_event=Event.objects.get(pk=first_event)
    #     )
    #     first_event += 1
    article = Article.objects.create(
            created_at=timezone.make_aware(datetime(2019,4,11)),
            # updated_at=timezone.now(),
            title="WTO ‘후쿠시마산 수산물 분쟁’ 끝내 일본 손 들어주나?",
            press='JTBC',
            event=Event.objects.get(title="WTO 판결")
        )
    article2 = Article.objects.create(
            created_at=timezone.make_aware(datetime(2019,4,12)),
            # updated_at=timezone.now(),
            title="후쿠시마 수산물 계속 못 들어온다…한국, WTO 분쟁서 승소",
            press='한겨레',
            event=Event.objects.get(title="WTO 판결")
        )
    article3 = Article.objects.create(
        created_at=timezone.make_aware(datetime(2019,4,9)),
        title="\"노딜 브렉시트는 안돼\"…영국 상·하원 브렉시트 연기",
        press="~~",
        event=Event.objects.get(title="브렉시트")
    )
    article3 = Article.objects.create(
        created_at=timezone.make_aware(datetime(2019,4,9)),
        title="이미선 “주식 처분” 사퇴 거부…정의당은 조건부 찬성 선회",
        press="~~",
        event=Event.objects.get(title="한국당 이미선 고발")
    )
    article3 = Article.objects.create(
        created_at=timezone.make_aware(datetime(2019,4,10)),
        title="또 '반쪽 최고위'…바른정당계 \"총사퇴\" vs 孫 \"한분씩 만날것\"",
        press="~~",
        event=Event.objects.get(title="바른미래당 회의")
    )
    # article = Article.objects.create(
    #         created_at=timezone.make_aware(datetime()),
    #         # updated_at=timezone.now(),
    #         title="",
    #         press='',
    #         issue=Issue.objects.get(title="")
    #     )
    # article = Article.objects.create(
    #         created_at=timezone.make_aware(datetime()),
    #         # updated_at=timezone.now(),
    #         title="",
    #         press='',
    #         issue=Issue.objects.get(title="")
    #     )
    
    return

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