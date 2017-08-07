from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from main_app.forms import UserUpdateForm

@login_required
def user_update( pRequest, pUserId):
    '''
    User update view
    @param int pUserId User id
    '''

    user = get_user_model().objects.get( id = pUserId)

    if pRequest.user.id == user.id:

        if pRequest.method == 'POST':

            userUpdateForm = UserUpdateForm( pRequest.POST)

            if userUpdateForm.is_valid():

                user.location = userUpdateForm.cleaned_data['location']
                user.bio = userUpdateForm.cleaned_data['bio']
                user.avatar = userUpdateForm.cleaned_data['avatar']
                user.save()
                return render(pRequest, 'user/item.html', {'user': user})

        else :
            
            updateUserForm = UserUpdateForm( initial = {
                'location': user.location,
                'bio': user.bio,
                'avatar': user.avatar
                })
            return render( pRequest, 'user/update.html', {'user' : user, 'updateUserForm': updateUserForm})
    else:
        return HttpResponseRedirect('/')