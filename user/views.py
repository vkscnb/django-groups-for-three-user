
from rest_framework.permissions import AllowAny

from rest_framework.response import Response

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from .serializers import UserListAndDetailsSerializer
from .models import User
from .user_permission_decorator import permission_decorator
from rest_framework.decorators import api_view, permission_classes


@api_view(['POST'])
@permission_classes((AllowAny,))
def user_login(request):

        ## UserLoginSerializer is authenticate the user with email and password
        ## if any error then raise the exceptions
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
       
        email,user_id = serializer.data['email'].split()
        
        response = {
            'success' : True,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            'id':user_id,
            'email':email
        }

        return Response(response)

@api_view(['POST', 'GET'])

### Custom permission allow this API for Admin
@permission_decorator(['admin_user'])
def create_and_list_of_teacher(request):

    ### create Teacher user
    if request.method == 'POST':
        data = request.data
        try:
            user = User(
                email= data['email'],
                name= data['name'],
                gender= data['gender'],
                type = 'Teacher'
            )

            user.set_password(data['password'])
            user.save()
            group = Group.objects.get(name='teacher_user')
            user.groups.add(group)

            return Response({'success':True, 'message':'Teacher created'})

        except Exception as e:
            return Response({'status':False, "message":str(e)})

     ### get all Teacher users
    if request.method == 'GET':
        data = User.objects.filter(type='Teacher')
        serializer = UserListAndDetailsSerializer(data, many=True)

        return Response({'success':True, "message":'All Teachers list', 'data':serializer.data})


@api_view(['GET'])

### @permission_decorator Custom permission to allow this API only for Admin and Teacher
@permission_decorator(['admin_user', 'teacher_user'])
def details_of_teacher(request, teacher_id):
    try:
        ### get teacher details if user is admin
        data = User.objects.get(id=teacher_id, type='Teacher')

        ### get teacher details if user is Teacher
        if request.user.type == 'Teacher':
            data = User.objects.get(id=request.user.id, type='Teacher')
        
        serializer = UserListAndDetailsSerializer(data)
        
        return Response({'success':True, "message":'Teacher Details', 'data':serializer.data})
    
    ### except exceptions if Teacher not exist in database
    except User.DoesNotExist as e:
        return Response({'success':True, "message":f"Teacher not exist with id {teacher_id}"})

    except Exception as e:
        return Response({'success':True, "message":str(e)})


@api_view(['POST', 'GET'])
@permission_decorator(['admin_user', 'teacher_user'])
def create_and_list_of_student(request):

    if request.method == 'POST':
        data = request.data
        try:
            user = User(
                email= data['email'],
                name= data['name'],
                gender= data['gender'],
                type = 'Student'
            )

            user.set_password(data['password'])
            user.save()
            group = Group.objects.get(name='student_user')
            user.groups.add(group)

            return Response({'success':True, "message":"Student created"})

        except Exception as e:
            return Response({'status':False, "message":str(e)})

    ### get all Student users
    if request.method == 'GET':
        data = User.objects.filter(type='Student')
        serializer = UserListAndDetailsSerializer(data, many=True)

        return Response({'success':True, "message":'All Students list', 'data':serializer.data})

@api_view(['GET'])
@permission_decorator(['admin_user', 'teacher_user', 'student_user'])
def details_of_student(request, student_id):
    try:
        ### get Student details if user is Admin and Teacher
        data = User.objects.get(id=student_id, type='Student')

        ### get Student details if user is Student
        if request.user.type == 'Student':
            data = User.objects.get(id=request.user.id, type='Student')
        
        serializer = UserListAndDetailsSerializer(data)
        
        return Response({'success':True, "message":'Student Details', 'data':serializer.data})
    
    ### except exceptions if Student not exist in database
    except User.DoesNotExist as e:
        return Response({'success':True, "message":f"Student not exist with id {teacher_id}"})

    except Exception as e:
        return Response({'success':True, "message":str(e)})

