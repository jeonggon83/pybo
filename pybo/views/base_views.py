from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
import matplotlib.pyplot as plt

from ..models import Question

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..models import Question, Company, Serverstatus, Answer
import matplotlib.pyplot as plt
import io
from django.http import HttpResponse
import pymysql
from matplotlib.backends.backend_pdf import PdfPages
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from ..forms import QuestionForm, AnswerForm
#기본글 테스트 from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

#아래부터 메일 보내는 소스
def plot_view(request):
    buf = create_plot()
    return HttpResponse(buf.getvalue(), content_type='image/png')


def download_pdf(request):
    # PDF 파일을 메모리에서 생성하기 위한 버퍼

    buffer = io.BytesIO()

    serverstatus_list = Serverstatus.objects.all()

    temperatures = [serverstatus.temperature for serverstatus in serverstatus_list]
    reg_dates = [serverstatus.reg_date.strftime("%Y-%m-%d") for serverstatus in serverstatus_list]

    # 그래프 생성
    plt.figure()
    plt.bar(reg_dates, temperatures)
    plt.title("Temperature Sensor Data")
    plt.xlabel("Date")
    plt.ylabel("Temperature")

    # PDF로 저장
    with PdfPages(buffer) as pdf:
        pdf.savefig()
        plt.close()

    # 버퍼를 처음으로 되돌림

    buffer.seek(0)

    # HTTP 응답 생성
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="plot.pdf"'

    subject = 'Your Graph Report'
    message = 'Please find attached the PDF report of your graph.'
    #email_from = settings.EMAIL_HOST_USER
    email_from = 'jglee@saminhnt.com'
    recipient_list = ['jglee@saminhnt.com']

    # 이메일 객체 생성
    email = EmailMessage(
        subject,
        message,
        email_from,
        recipient_list
    )

    # PDF 파일 첨부
    email.attach_file('plot.pdf')

    # 이메일 전송
    email.send()
    return response


def send_email(request):
    subject = "message"							# 타이틀
    to = ["jeonggon83@naver.com"]					# 수신할 이메일 주소
    from_email = "jeonggon83@naver.com"			# 발신할 이메일 주소
    message = "메세지 테스트"					# 본문 내용
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()


def create_plot():
    # Creating data
    #여기 쌍
    serverstatus_list = Serverstatus.objects.all()

    for i in serverstatus_list:
        print(i.temperature)
        print(i.reg_date.strftime("%Y-%m-%d"))

    temperatures = [serverstatus.temperature for serverstatus in serverstatus_list]
    reg_dates = [serverstatus.reg_date.strftime("%Y-%m-%d") for serverstatus in serverstatus_list]
    #dates = [item.date for item in data]
    #여기 쌍 끝


    #data = SalesData.objects.all().order_by('date')
    #dates = [item.date for item in data]

    #data = SalesData.objects.all().order_by('date')
    #dates = [item.date for item in data]
    #sales = [item.sales for item in data]

    #serverstatus_list = Serverstatus.objects.all()

    #for i in serverstatus_list:
    #   print("create_plot 들어옴")
    #        print(i.no)
    #    print(i.temperature)

    #x = [10, 20, 30, 40, 500]
    #y = [i**2 for i in temperatures]  # Simple quadratic function

    # Creating a figure and axis
    fig, ax = plt.subplots()
    #ax.plot(reg_dates, temperatures)
    ax.bar(reg_dates, temperatures)
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature")
    ax.set_title("Temperature Sensor Data")
    #ax.title("Temperature Sensor Data")
    #ax.xlabel("Date")
    #ax.ylabel("Temperature")



    # Saving the plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')

    # PDF 파일로 저장
    plt.savefig('plot.pdf')

    # 화면에 보여주기 (필요한 경우)
    #plt.show()

    plt.close(fig)
    buf.seek(0)

    return buf

'''
# 메일 보내는 소스 시작
def index(request):
    #question_list = Question.objects.order_by('-create_date')
    #context = {'question_list': question_list}

    #server_status_list  = ServerStatus.objects.all()
    #context = {'server_status_list': server_status_list}
    #print(server_status_list.no)

    #def __str__(self):
        #return self.company
    #return render(request, 'pybo/question_list.html', context)
    #return HttpResponse("안녕하세요. 기본 페이지입니다.")

    # edit
    #company_list = Company.objects.all()  # Company 모델에 있는 정보를 전부 가져온다.
    #context = {'company_list': company_list}  # company_list의 정보를 context에 담는다.

    serverstatus_list = Serverstatus.objects.all()

    #for i in serverstatus_list:
     #   print(i.no)
      #  print(i.temperature)


    context = {'serverstatus_list': serverstatus_list}

    return render(request, 'pybo/index.html', context)

#메일 보내는 소스 끝
'''