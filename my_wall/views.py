from django.shortcuts import render, HttpResponse, redirect
from .models import Messages, Comments
from login_reg_app.models import Users 
from django.contrib import messages # if we were to validate

# Create your views here.
def wall(request):

    context = {
        'all_messages' : Messages.objects.all(),
        'all_comments' : Comments.objects.all(),
        'user' : Users.objects.get(id = request.session['user_id']),
    }
    
    
    return render(request, 'wall.html', context)

def createMsg(request):
    print("in create msg method")
    if request.method == 'POST':
        user = Users.objects.get(id = request.session['user_id'])
        message = request.POST['message']

        Messages.objects.create(
            user_id = user,
            message = message
        )

    return redirect('/wall')

def createComment(request):
    if request.method == 'POST':
        msg_id = request.POST['msg']
        comment2 = request.POST['content']
        # Users.objects.get(id = request.session['user_id'])
        Comments.objects.create(
            user_id = Users.objects.get(id = request.session['user_id']),
            comment = comment2,
            message_id = Messages.objects.get(id = msg_id)
        )

    return redirect('/wall')
    

def delete_msg(request , msgID):
    id = int(msgID)
    message_to_delete = Messages.objects.get(id = id).delete()
    
    return redirect('/wall')

def delete_comment(request , commentID):
    id = int(commentID)
    comment_to_delete = Comments.objects.get(id = id).delete()
    
    return redirect('/wall')