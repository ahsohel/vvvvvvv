from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import User_info_table


from datetime import datetime
from datetime import date, timedelta


from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt



from .models import listing_of_accommodationthat_seller_offering, accommodationthat_seller_offering_image


def going_for_login(request):
    return render(request, 'views_2_templates/going_for_login.html')

def going_for_signup(request):
    return render(request, 'views_2_templates/going_for_signup.html')





def func_login(request):
    if request.method=="POST":
        user_email = request.POST.get('user_email')
        password = request.POST.get('password')

        see_email_present = User_info_table.objects.filter(User_Email=user_email)
        if see_email_present:
            start_session = User_info_table.objects.get(User_Email=user_email)
            request.session['session_user_id'] = start_session.id
            request.session['session_user_number'] = start_session.User_Number
            request.session['session_User_name'] = start_session.User_name
            request.session['session_User_Email'] = start_session.User_Email
            return redirect('index')

        else:
            messages.warning(request, 'Password Dose Not Match !')
            return redirect('func_login')


        # user_vari = authenticate(username=user_name, password=password)
        #
        # if user_vari is not None:
        #     login(request, user_vari)
        #
        #     request.session['user_id'] = user_vari.id
        #
        #
        #     return redirect('index')

    return redirect('func_login')




def func_signup(request):
    if request.method == "POST":

        first_name=request.POST.get('first_name')
        email=request.POST.get('email')
        Mobile_Number=request.POST.get('Mobile_Number')
        password=request.POST.get('password')

        Is_Username_present = User_info_table.objects.filter(User_Email=email)


        if Is_Username_present:
            print('sdddddddd')
            contex = {
                'show_massage':'Email is already exist'
            }
            return render(request, 'views_2_templates/going_for_signup.html', contex)
        else:
            print('eleleleleelsdddddddd')
            create_new_one = User_info_table(User_name=first_name, User_Number=Mobile_Number, User_Email=email, User_Password=password)
            create_new_one.save()






        return redirect('going_for_login')

    return redirect('index')


def func_logout(request):
    request.session.clear()
    return redirect('index')

def user_profile(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        the_user = User_info_table.objects.get(id=session_user_id)

        print('the_user.User_photo')
        print(the_user.User_photo)

        contex = {
            'the_user':the_user,

        }
        return render(request, 'views_2_templates/profile.html', contex)
    return redirect('func_login')

def Change_Password_Or_Information(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        the_user = User_info_table.objects.get(id=session_user_id)

        contex = {
            'the_user': the_user,

        }
        return render(request, 'views_2_templates/profile_change.html', contex)
    return redirect('func_login')


def save_the_edited_part(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:
        Edited_Property_and_room_images_1 = request.FILES.get('Edited_Property_and_room_images_1')
        Edited_user_name = request.POST.get('Edited_user_name')
        Edited_User_Number = request.POST.get('Edited_User_Number')
        Edited_User_Email = request.POST.get('Edited_User_Email')
        Edited_password = request.POST.get('Edited_password')

        print('Edited_Property_and_room_images_1')
        print(Edited_Property_and_room_images_1)
        print(Edited_user_name)
        print(Edited_User_Number)
        print(Edited_User_Email)
        print(Edited_password)
        if Edited_User_Number == 'None':
            Edited_User_Number=''
            print('Edited_User_Number')
            print(Edited_User_Number)
        if Edited_Property_and_room_images_1 == None:
            print('kamon ase image niiiiiiiiiiiiiiiiiiiiiiii')
            the_user = User_info_table.objects.get(id=session_user_id)
            the_user.User_name = Edited_user_name
            the_user.User_Number = Edited_User_Number
            the_user.User_Email = Edited_User_Email
            the_user.User_Password = Edited_password
            the_user.save()

        else:
            print('kamon ase image aseeeeeeeeeeeeeeeeeeee')
            the_user = User_info_table.objects.get(id=session_user_id)
            the_user.User_name = Edited_user_name
            the_user.User_photo = Edited_Property_and_room_images_1
            the_user.User_Number = Edited_User_Number
            the_user.User_Email = Edited_User_Email
            the_user.User_Password = Edited_password
            the_user.save()



        return redirect('user_profile')
    return redirect('func_login')



def show_list(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:

        the_user = User_info_table.objects.get(id=session_user_id)
        print('the_user')
        print(the_user)
        print(the_user)

        the_list = listing_of_accommodationthat_seller_offering.objects.filter(link_with_user=the_user)
        if the_list:
            for i in the_list:

                print('the_list_one.List_create_date')
                print(i.List_create_date)
                print('the_list_one.List_create_date')

                current_date = date.today()
                Til_future_date = i.List_create_date + timedelta(days=45)
                print('current_date')
                print(current_date)

                if current_date < Til_future_date:
                    print('kom')
                    print(i.id)
                    the_edit_able = listing_of_accommodationthat_seller_offering.objects.get(id=i.id)
                    the_edit_able.Can_edit_or_not='Can_Edit'
                    the_edit_able.save()
                else:
                    print('base')
                    the_edit_able = listing_of_accommodationthat_seller_offering.objects.get(id=i.id)
                    the_edit_able.Can_edit_or_not = 'Can_Not_Edit'
                    the_edit_able.save()


        print(the_list)


        print('the_list')
        print(the_list)


        print('datetime.today()')
        print(datetime.today())
        print(datetime.now())
        print(date.today())
        current_date = date.today()
        future_date = current_date + timedelta(days=7)
        print('future_date')
        print(future_date)
        # orders = listing_of_accommodationthat_seller_offering.objects.filter(
        #     date_ordered__range=(current_date, future_date),
        # )

        contex = {
            'the_list': the_list,
            'current_date': current_date,

        }


        return render(request, 'views_2_templates/show_list.html', contex)

    return redirect('func_login')







def go_to_edit_list(request, pk):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        the_edit_able_row = listing_of_accommodationthat_seller_offering.objects.get(id=pk)

        # print(the_edit_able_row.model_Room_availability_Date|date:'m-d-Y')
        print('the_edit_able_row.model_Room_availability_Date')
        print(the_edit_able_row.model_Room_availability_Date)

        x = str(the_edit_able_row.model_Room_availability_Date)
        current_date = the_edit_able_row.model_Room_availability_Date

        contex = {
            'the_edit_able_row':the_edit_able_row,
            'current_date':current_date,
            'x':x,

        }
        return render(request, 'views_2_templates/the_edit_able_row.html', contex)
    return redirect('func_login')





def Show_List_Edit_Image(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:

        p = request.POST.get('get_the_list_id_for_image')
        print('pppppppppppppppppppppppppppppppp')
        print(p)
        the_edit_able_row_for_image = listing_of_accommodationthat_seller_offering.objects.get(id=p)
        count_image = the_edit_able_row_for_image.model_Property_and_room_images_1.all().count()
        contex = {
            'the_edit_able_row_for_image': the_edit_able_row_for_image,
            'count_image': count_image,

        }


        return render(request, 'Show_List_Edit_Image.html', contex)
    return redirect('func_login')



def let_save_edited_image_and_get_back(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:

        first_image = request.FILES.get('image_1_get_for')
        second_image = request.FILES.get('image_2_get_for')
        third_image = request.FILES.get('image_3_get_for')
        four_image = request.FILES.get('image_4_get_for')
        five_image = request.FILES.get('image_5_get_for')

        get_the_main_row_id = request.POST.get('get_the_main_row_id')
        print('pppppppppppppppppppppppppppppppp')
        print(first_image)
        print(second_image)
        print(third_image)
        print(four_image)
        print(five_image)

        print('five_imagefive_image')
        print(get_the_main_row_id)
        get_the_main_row_id_pass = get_the_main_row_id

        if first_image:
            print('5')
            get_the_main = listing_of_accommodationthat_seller_offering.objects.get(id=get_the_main_row_id)

            save_new_image = accommodationthat_seller_offering_image(model_Property_and_room_images_1=first_image)
            save_new_image.save()
            get_the_main_row_id_p = save_new_image.id
            subc1 = accommodationthat_seller_offering_image.objects.get(id=get_the_main_row_id_p)

            get_the_main.model_Property_and_room_images_1.add(subc1)
            get_the_main.save()

        if second_image:
            print('5')
            get_the_main = listing_of_accommodationthat_seller_offering.objects.get(id=get_the_main_row_id)

            save_new_image = accommodationthat_seller_offering_image(model_Property_and_room_images_1=second_image)
            save_new_image.save()
            get_the_main_row_id_p = save_new_image.id
            subc1 = accommodationthat_seller_offering_image.objects.get(id=get_the_main_row_id_p)

            get_the_main.model_Property_and_room_images_1.add(subc1)
            get_the_main.save()

        if third_image:
            print('5')
            get_the_main = listing_of_accommodationthat_seller_offering.objects.get(id=get_the_main_row_id)

            save_new_image = accommodationthat_seller_offering_image(model_Property_and_room_images_1=third_image)
            save_new_image.save()
            get_the_main_row_id_p = save_new_image.id
            subc1 = accommodationthat_seller_offering_image.objects.get(id=get_the_main_row_id_p)

            get_the_main.model_Property_and_room_images_1.add(subc1)
            get_the_main.save()

        if four_image:
            print('5')
            get_the_main = listing_of_accommodationthat_seller_offering.objects.get(id=get_the_main_row_id)

            save_new_image = accommodationthat_seller_offering_image(model_Property_and_room_images_1=four_image)
            save_new_image.save()
            get_the_main_row_id_p = save_new_image.id
            subc1 = accommodationthat_seller_offering_image.objects.get(id=get_the_main_row_id_p)

            get_the_main.model_Property_and_room_images_1.add(subc1)
            get_the_main.save()

        if five_image:
            print('5')
            get_the_main = listing_of_accommodationthat_seller_offering.objects.get(id=get_the_main_row_id)

            save_new_image = accommodationthat_seller_offering_image(model_Property_and_room_images_1=five_image)
            save_new_image.save()
            get_the_main_row_id_p = save_new_image.id
            subc1 = accommodationthat_seller_offering_image.objects.get(id=get_the_main_row_id_p)

            get_the_main.model_Property_and_room_images_1.add(subc1)
            get_the_main.save()



        return redirect('go_to_edit_list', get_the_main_row_id_pass)
    return redirect('func_login')





def Show_List_Edit_Total(request):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:

        get_the_list_id_for_image_all = request.POST.get('get_the_list_id_for_image_all')


        Room_availability_model_offering_accommodation = request.POST.get('Room_availability_model_offering_accommodation')
        Edit_Type_of_model_property = request.POST.get('Edit_Type_of_model_property')
        Edit_Property_Address = request.POST.get('Edit_Property_Address')
        Edit_model_property_bedrooms = request.POST.get('Edit_model_property_bedrooms')
        Edit_Type_model_property_bathrooms = request.POST.get('Edit_Type_model_property_bathrooms')
        Edit_Type_model_Parking = request.POST.get('Edit_Type_model_Parking')
        Edit_Type_model_Internet = request.POST.get('Edit_Type_model_Internet')
        Edit_Type_model_Total_number_of_flatmates = request.POST.get('Edit_Type_model_Total_number_of_flatmates')
        Edit_model_Room_name = request.POST.get('Edit_model_Room_name')
        Edit_model_Room_type = request.POST.get('Edit_model_Room_type')
        Edit_model_Room_furnishings = request.POST.get('Edit_model_Room_furnishings')
        Edit_model_Bathroom_type = request.POST.get('Edit_model_Bathroom_type')


        Edit_model_Bed_Size = request.POST.get('Edit_model_Bed_Size')

        Edit_model_Room_furnishings_features_Bed_side_table = request.POST.get('Edit_model_Room_furnishings_features_Bed_side_table')
        Edit_model_Room_furnishings_features_Wardrobe = request.POST.get('Edit_model_Room_furnishings_features_Wardrobe')
        Edit_model_Room_furnishings_features_Drawers = request.POST.get('Edit_model_Room_furnishings_features_Drawers')
        Edit_model_Room_furnishings_features_Air_conditioner = request.POST.get('Edit_model_Room_furnishings_features_Air_conditioner')
        Edit_model_Room_furnishings_features_Heater = request.POST.get('Edit_model_Room_furnishings_features_Heater')
        Edit_model_Room_furnishings_features_Desk = request.POST.get('Edit_model_Room_furnishings_features_Desk')
        Edit_model_Room_furnishings_features_Lamp = request.POST.get('Edit_model_Room_furnishings_features_Lamp')
        Edit_model_Room_furnishings_features_Chair = request.POST.get('Edit_model_Room_furnishings_features_Chair')
        Edit_model_Room_furnishings_features_Couch = request.POST.get('Edit_model_Room_furnishings_features_Couch')
        Edit_model_Room_furnishings_features_TV = request.POST.get('Edit_model_Room_furnishings_features_TV')
        Edit_model_Room_furnishings_features_Balcony = request.POST.get('Edit_model_Room_furnishings_features_Balcony')
        Edit_model_Room_furnishings_features_Door_lock = request.POST.get('Edit_model_Room_furnishings_features_Door_lock')
        Edit_model_Room_furnishings_features_Kitchenette = request.POST.get('Edit_model_Room_furnishings_features_Kitchenette')

        Edit_model_room_Weekly_rent = request.POST.get('Edit_model_room_Weekly_rent')
        Edit_model_room_changed_Bond = request.POST.get('Edit_model_room_changed_Bond')
        Edit_model_room_changed_Bills = request.POST.get('Edit_model_room_changed_Bills')
        edit_model_Room_availability_Date = request.POST.get('edit_model_Room_availability_Date')
        Edit_model_Room_availability_Minimum_length_stay = request.POST.get('Edit_model_Room_availability_Minimum_length_stay')
        Edit_model_Room_availability_Maximum_length_stay = request.POST.get('Edit_model_Room_availability_Maximum_length_stay')
        Edit_model_Flatmate_Preference_name = request.POST.get('Edit_model_Flatmate_Preference_name')
        edited_model_Accepting_Backpackers = request.POST.get('edited_model_Accepting_Backpackers')
        Edited_model_Accepting_Students = request.POST.get('Edited_model_Accepting_Students')
        edited_model_Accepting_Smokers = request.POST.get('edited_model_Accepting_Smokers')
        edited_model_Accepting_LGBTI = request.POST.get('edited_model_Accepting_LGBTI')
        edited_model_Accepting_years_olds = request.POST.get('edited_model_Accepting_years_olds')
        edited_model_Accepting_Children = request.POST.get('edited_model_Accepting_Children')
        edited_model_Accepting_Pets = request.POST.get('edited_model_Accepting_Pets')
        edited_model_Accepting_Retirees = request.POST.get('edited_model_Accepting_Retirees')
        edited_model_Accepting_On_welfare = request.POST.get('edited_model_Accepting_On_welfare')
        edited_model_introduce_about_your_flatmates = request.POST.get('edited_model_introduce_about_your_flatmates')
        edited_model_introduce_great_about_living = request.POST.get('edited_model_introduce_great_about_living')

        print('Room_availability_model_offering_accommodation')
        print(Room_availability_model_offering_accommodation)
        print(Edit_Type_of_model_property)
        print(Edit_Property_Address)
        print(Edit_model_property_bedrooms)
        print(Edit_Type_model_property_bathrooms)
        print(Edit_Type_model_Parking)
        print(Edit_Type_model_Internet)
        print(Edit_Type_model_Total_number_of_flatmates)
        print(Edit_model_Room_name)
        print(Edit_model_Bed_Size)
        print(Edit_model_Room_furnishings_features_Bed_side_table)
        print(Edit_model_Room_furnishings_features_Wardrobe)
        print(Edit_model_Room_furnishings_features_Drawers)
        print(Edit_model_Room_furnishings_features_Air_conditioner)
        print(Edit_model_Room_furnishings_features_Heater)
        print(Edit_model_Room_furnishings_features_Desk)
        print(Edit_model_Room_furnishings_features_Lamp)
        print(Edit_model_Room_furnishings_features_Chair)
        print(Edit_model_Room_furnishings_features_Couch)
        print(Edit_model_Room_furnishings_features_TV)
        print(Edit_model_Room_furnishings_features_Balcony)
        print(Edit_model_Room_furnishings_features_Door_lock)
        print(Edit_model_Room_furnishings_features_Kitchenette)
        print(Edit_model_room_Weekly_rent)
        print(Edit_model_room_changed_Bond)
        print(Edit_model_room_changed_Bills)
        print(edit_model_Room_availability_Date)
        print(Edit_model_Room_availability_Minimum_length_stay)
        print(Edit_model_Room_availability_Maximum_length_stay)
        print(Edit_model_Flatmate_Preference_name)
        print(edited_model_Accepting_Backpackers)
        print(Edited_model_Accepting_Students)
        print(edited_model_Accepting_Smokers)
        print(edited_model_Accepting_LGBTI)
        print(edited_model_Accepting_years_olds)
        print(edited_model_Accepting_Children)
        print(edited_model_Accepting_Pets)
        print(edited_model_Accepting_Retirees)
        print(edited_model_Accepting_On_welfare)
        print(edited_model_introduce_about_your_flatmates)
        print(edited_model_introduce_great_about_living)
        print('edited_model_introduce_great_about_living')

        get_the_main_info_row = listing_of_accommodationthat_seller_offering.objects.get(id=get_the_list_id_for_image_all)

        get_the_main_info_row.model_offering_accommodation = Room_availability_model_offering_accommodation
        get_the_main_info_row.model_property = Edit_Type_of_model_property
        get_the_main_info_row.model_Property_Address = Edit_Property_Address
        get_the_main_info_row.model_property_bedrooms = Edit_model_property_bedrooms
        get_the_main_info_row.model_property_bathrooms = Edit_Type_model_property_bathrooms
        get_the_main_info_row.model_Parking = Edit_Type_model_Parking
        get_the_main_info_row.model_Internet = Edit_Type_model_Internet
        get_the_main_info_row.model_Total_number_of_flatmates = Edit_Type_model_Total_number_of_flatmates
        get_the_main_info_row.model_Room_name = Edit_model_Room_name
        get_the_main_info_row.model_Room_type = Edit_model_Room_type
        get_the_main_info_row.model_Room_furnishings = Edit_model_Room_furnishings
        get_the_main_info_row.model_Bathroom_type = Edit_model_Bathroom_type
        get_the_main_info_row.model_Bed_Size = Edit_model_Bed_Size

        if Edit_model_Room_furnishings_features_Bed_side_table == 'on':
            get_the_main_info_row.model_Room_furnishings_features_Bed_side_table = Edit_model_Room_furnishings_features_Bed_side_table
        if Edit_model_Room_furnishings_features_Wardrobe == 'on':
            get_the_main_info_row.model_Room_furnishings_features_Wardrobe = Edit_model_Room_furnishings_features_Wardrobe
        if Edit_model_Room_furnishings_features_Drawers == 'on':
            get_the_main_info_row.model_Room_furnishings_features_Drawers = Edit_model_Room_furnishings_features_Drawers
        if Edit_model_Room_furnishings_features_Air_conditioner == 'on':
            get_the_main_info_row.model_Room_furnishings_features_Air_conditioner = Edit_model_Room_furnishings_features_Air_conditioner
        if Edit_model_Room_furnishings_features_Heater == 'on':
            get_the_main_info_row.model_Room_furnishings_features_Heater = Edit_model_Room_furnishings_features_Heater
        if Edit_model_Room_furnishings_features_Desk == 'on':
            get_the_main_info_row.model_Room_furnishings_features_Desk = Edit_model_Room_furnishings_features_Desk
        if Edit_model_Room_furnishings_features_Lamp == 'on':
            get_the_main_info_row.model_Room_furnishings_features_Lamp = Edit_model_Room_furnishings_features_Lamp
        if Edit_model_Room_furnishings_features_Chair == 'on':
            get_the_main_info_row.model_Room_furnishings_features_Chair = Edit_model_Room_furnishings_features_Chair
        if Edit_model_Room_furnishings_features_Couch == 'on':
            get_the_main_info_row.model_Room_furnishings_features_Couch = Edit_model_Room_furnishings_features_Couch
        if Edit_model_Room_furnishings_features_TV == 'on':
            get_the_main_info_row.model_Room_furnishings_features_TV = Edit_model_Room_furnishings_features_TV
        if Edit_model_Room_furnishings_features_Balcony == 'on':
            get_the_main_info_row.model_Room_furnishings_features_Balcony = Edit_model_Room_furnishings_features_Balcony
        if Edit_model_Room_furnishings_features_Door_lock == 'on':
            get_the_main_info_row.model_Room_furnishings_features_Door_lock = Edit_model_Room_furnishings_features_Door_lock
        if Edit_model_Room_furnishings_features_Kitchenette == 'on':
            get_the_main_info_row.model_Room_furnishings_features_Kitchenette = Edit_model_Room_furnishings_features_Kitchenette

        get_the_main_info_row.model_room_Weekly_rent = Edit_model_room_Weekly_rent
        get_the_main_info_row.model_room_changed_Bond = Edit_model_room_changed_Bond
        get_the_main_info_row.model_room_changed_Bills = Edit_model_room_changed_Bills

        get_the_main_info_row.model_Room_availability_Date = edit_model_Room_availability_Date
        get_the_main_info_row.model_Room_availability_Minimum_length_stay = Edit_model_Room_availability_Minimum_length_stay
        get_the_main_info_row.model_Room_availability_Maximum_length_stay = Edit_model_Room_availability_Maximum_length_stay

        if Edit_model_Flatmate_Preference_name == 'on':
            get_the_main_info_row.model_Flatmate_Preference_name = Edit_model_Flatmate_Preference_name
        if edited_model_Accepting_Backpackers == 'on':
            get_the_main_info_row.model_Accepting_Backpackers = edited_model_Accepting_Backpackers
        if Edited_model_Accepting_Students == 'on':
            get_the_main_info_row.model_Accepting_Students = Edited_model_Accepting_Students
        if edited_model_Accepting_Smokers == 'on':
            get_the_main_info_row.model_Accepting_Smokers = edited_model_Accepting_Smokers
        if edited_model_Accepting_LGBTI == 'on':
            get_the_main_info_row.model_Accepting_LGBTI = edited_model_Accepting_LGBTI
        if edited_model_Accepting_years_olds == 'on':
            get_the_main_info_row.model_Accepting_years_olds = edited_model_Accepting_years_olds
        if edited_model_Accepting_Children == 'on':
            get_the_main_info_row.model_Accepting_Children = edited_model_Accepting_Children
        if edited_model_Accepting_Pets == 'on':
            get_the_main_info_row.model_Accepting_Pets = edited_model_Accepting_Pets
        if edited_model_Accepting_Retirees == 'on':
            get_the_main_info_row.model_Accepting_Retirees = edited_model_Accepting_Retirees
        if edited_model_Accepting_On_welfare == 'on':
            get_the_main_info_row.model_Accepting_On_welfare = edited_model_Accepting_On_welfare

        get_the_main_info_row.model_introduce_about_your_flatmates = edited_model_introduce_about_your_flatmates
        get_the_main_info_row.model_introduce_great_about_living = edited_model_introduce_great_about_living

        get_the_main_info_row.save()


        return redirect('show_list')
    return redirect('func_login')




def go_to_delete_list(request, pk):
    session_user_id = request.session.get('session_user_id')
    if session_user_id:
        print('i am in hrere   djsdhsjdhjdhsjdh hs jdshdjshdjs ')
        print('pk')
        print(pk)
        the_edit_able_row = listing_of_accommodationthat_seller_offering.objects.get(id=pk)
        print('the_edit_able_row')
        print(the_edit_able_row)
        print(the_edit_able_row.id)
        the_edit_able_row.delete()

        return redirect('show_list')
    return redirect('func_login')





@csrf_exempt
def lets_delete_the_image_from_edit_option(request):
    this_value = request.POST.get('l')
    print('this_value')
    print(this_value)
    ko = accommodationthat_seller_offering_image.objects.get(id = this_value)
    ko.delete()

    return HttpResponse('Done')