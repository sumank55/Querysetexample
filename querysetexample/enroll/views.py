from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q
from django.db.models import Max,Avg,Sum


# Create your views here.
def StudentView(request):


    '''
    # student=Student.objects.order_by('name','address')
    # student=Student.objects.order_by('id')


# it will remove duplicate data from after matching exact data
    # qs1=Student.objects.values_list('id','name',named=True)
    # qs2=Teacher.objects.values_list('id','name',named=True)
    # student=qs2.union(qs1)


# it will show only matched data from both table
    # qs1=Student.objects.values_list('name',named=True)
    # qs2=Teacher.objects.values_list('name',named=True)
    # student=qs2.intersection(qs1)

#it will show remove matched data fram table nad show all the data from first qs1
    # qs1=Student.objects.values_list('name',named=True)
    # qs2=Teacher.objects.values_list('name',named=True)
    # student=qs1.difference(qs2)

#        And operator                  it will show
    # student=Student.objects.filter(name='suman') & Student.objects.filter(address='patna')
    # student=Student.objects.filter(name='Sanju',address='Gaya')
    # student=Student.objects.filter(Q(id=1) & Q(name="suman"))



    # Or operator    
    # student=Student.objects.filter(name='Sanju') | Student.objects.filter(address='patna')s
    # student=Student.objects.filter(Q(id=1) | Q(name="suman"))


# we will use get for unique row other wise filter 
    # student=Student.objects.get(pk=1)
    # student=Student.objects.first()
    # student=Student.objects.order_by('name').last()
    # student=Student.objects.latest('pass_date') 
    # student=Student.objects.earliest('pass_date') old data from
    # student=Student.objects.all()
    # print("student",student.exists())
    # student = Student.objects.create(name="Anita",roll=115,address='Delhi',marks=440,pass_date='2015-05-16')

    # student,created=Student.objects.get_or_create(name="Shyam",roll=116,address='Banarash',marks=340,pass_date='2016-05-16')
    # print("created")
    # student=Student.objects.filter(id=1).update(name="Suhani",address="mumbai")


    #update all address where marks matched
    # student=Student.objects.filter(marks=440).update(address="Mohali")


    # student,created=Student.objects.update_or_create(id=5,name='Sameer',defaults={'name':'Karan'})
    # print("student",created)

# for bulk data creation at a time
    # obj=[
    #     Student(name="moni",roll=114,address='Mohali',marks=500,pass_date='2011-12-25'),
    #     Student(name="Gulshan",roll=120,address='Baglapur',marks=750,pass_date='2018-4-25'),
    #     Student(name="Priti",roll=121,address='Hariyana',marks=630,pass_date='2018-12-25'),
    #     Student(name="Priya",roll=122,address='Mumbai',marks=800,pass_date='2016-12-25'),
    # ]
    # student=Student.objects.bulk_create(obj)
    # student=Student.objects.all().order_by('id')


    # for bulk of data updation at a time
    # stu=Student.objects.all()
    # for st in stu:
    #     st.address="Surat"
    # student=Student.objects.bulk_update(stu,['address']) 
    student=Student.objects.filter(address="Mumbai")
    print(student.count())   
    '''

    # student=Student.objects.order_by('marks').last()# it will show higest marks
    # second method
    # student1=Student.objects.aggregate(Max('marks'))
    # print(student1)
    # student=Student.objects.filter(marks=800)

    # third method
    # student=Student.objects.order_by('marks')[:3]
    # print(student)
    # student=Student.objects.filter(Q(id=5) | Q(name="Anita"))
    # student=Student.objects.filter(name="Anita").update(name="sohal")
    # student=Student.objects.count()
    
# Average price across all books.
    # student=Student.objects.aggregate(Avg('marks'))

    # student=Student.objects.all().aggregate(Avg('marks'))
    stu1=Student.objects.aggregate(Max('marks')) 
    stu2= Student.objects.aggregate(Avg('marks'))
    # print(set(stu1.values()).difference(stu2.values()))
    



    # student=Student.objects.aggregate(Sum('marks'))
    # print(student)

    # student=Student.objects.filter(marks__gte=440)
    # student=Student.objects.filter(marks__lte=500)
    # student=Student.objects.exclude(marks=440) & Student.objects.exclude(marks=500)
    # student=Student.objects.count()
    print("no of student",student)
    
   
    return render(request, 'teacher.html',{'student':student})
    


def TeacherView(request):
    teacher=Teacher.objects.all()
    print("teacher",teacher)
    return render(request, 'home.html',{'teacher':teacher})

