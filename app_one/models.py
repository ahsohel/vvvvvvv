from django.db import models
from django.contrib.auth.models import User

# Create your models here.


from datetime import datetime
from datetime import date, timedelta




class User_info_table(models.Model):
    class Meta:
        verbose_name_plural = 'User Information Table'

    User_name = models.CharField(max_length=256, blank=True, null=True)
    User_photo = models.ImageField(blank=True, null=True, upload_to='image/user_pic/')
    User_Number = models.CharField(max_length=256, blank=True, null=True)
    User_Email = models.CharField(max_length=256, blank=True, null=True) # will be uniq  username
    User_Password = models.CharField(max_length=256, blank=True, null=True)

    Joined_Date = models.DateTimeField(default=datetime.now(), blank=True)


    def __str__(self):
        return str(self.id)+" "+self.User_name +"  "








class accommodationthat_seller_offering_image(models.Model):
    class Meta:
        verbose_name_plural = 'listing of accommodationthat seller offering images'

    model_Property_and_room_images_1 = models.ImageField(blank=True, null=True, upload_to='image/')



    def __str__(self):
        return str(self.id)




class listing_of_accommodationthat_seller_offering(models.Model):
    class Meta:
        verbose_name_plural = 'listing of accommodationthat seller offering'

    link_with_user = models.ForeignKey(User_info_table, on_delete=models.CASCADE)

    model_offering_accommodation = models.CharField(max_length=256)
    model_property = models.CharField(max_length=256, blank=True, null=True)

    model_Property_Address = models.CharField(max_length=256)
    model_property_bedrooms = models.CharField(max_length=256)
    model_property_bathrooms = models.CharField(max_length=256)
    model_Parking = models.CharField(max_length=256)
    model_Internet = models.CharField(max_length=256)

    model_Total_number_of_flatmates = models.CharField(max_length=256)

    model_Room_name = models.CharField(max_length=256)
    model_Room_type = models.CharField(max_length=256)
    model_Room_furnishings = models.CharField(max_length=256)
    model_Bathroom_type = models.CharField(max_length=256)

    model_Bed_Size = models.CharField(max_length=256, blank=True, null=True)
    model_Room_furnishings_features_Bed_side_table = models.CharField(max_length=256, blank=True, null=True)
    model_Room_furnishings_features_Wardrobe = models.CharField(max_length=256, blank=True, null=True)
    model_Room_furnishings_features_Drawers = models.CharField(max_length=256, blank=True, null=True)
    model_Room_furnishings_features_Air_conditioner = models.CharField(max_length=256, blank=True, null=True)
    model_Room_furnishings_features_Heater = models.CharField(max_length=256, blank=True, null=True)
    model_Room_furnishings_features_Desk = models.CharField(max_length=256, blank=True, null=True)
    model_Room_furnishings_features_Lamp = models.CharField(max_length=256, blank=True, null=True)
    model_Room_furnishings_features_Chair = models.CharField(max_length=256, blank=True, null=True)
    model_Room_furnishings_features_Couch = models.CharField(max_length=256, blank=True, null=True)
    model_Room_furnishings_features_TV = models.CharField(max_length=256, blank=True, null=True)
    model_Room_furnishings_features_Balcony = models.CharField(max_length=256, blank=True, null=True)
    model_Room_furnishings_features_Door_lock = models.CharField(max_length=256, blank=True, null=True)
    model_Room_furnishings_features_Kitchenette = models.CharField(max_length=256, blank=True, null=True)

    model_room_Weekly_rent = models.IntegerField()
    model_room_changed_Bond = models.CharField(max_length=256)
    model_room_changed_Bills = models.CharField(max_length=256)

    model_Room_availability_Date = models.DateField(max_length=256)
    model_Room_availability_Minimum_length_stay = models.CharField(max_length=256)
    model_Room_availability_Maximum_length_stay = models.CharField(max_length=256)

    model_Property_and_room_images_1 = models.ManyToManyField(accommodationthat_seller_offering_image, blank=True, null=True)


    model_Flatmate_Preference_name = models.CharField(max_length=256)

    model_Accepting_Backpackers = models.CharField(max_length=256, blank=True, null=True)
    model_Accepting_Students = models.CharField(max_length=256, blank=True, null=True)
    model_Accepting_Smokers = models.CharField(max_length=256, blank=True, null=True)
    model_Accepting_LGBTI = models.CharField(max_length=256, blank=True, null=True)
    model_Accepting_years_olds = models.CharField(max_length=256, blank=True, null=True)
    model_Accepting_Children = models.CharField(max_length=256, blank=True, null=True)
    model_Accepting_Pets = models.CharField(max_length=256, blank=True, null=True)
    model_Accepting_Retirees = models.CharField(max_length=256, blank=True, null=True)
    model_Accepting_On_welfare = models.CharField(max_length=256, blank=True, null=True)
    Can_edit_or_not = models.CharField(max_length=256, blank=True, null=True)

    model_introduce_about_your_flatmates = models.TextField(blank=True, null=True)

    model_introduce_great_about_living = models.TextField(blank=True, null=True)

    List_create_date_time = models.DateTimeField(default=datetime.now(), blank=True, null=True)

    List_create_date = models.DateField(default=date.today(), blank=True, null=True)




    def __str__(self):
        return self.model_offering_accommodation + ' - ' + self.model_property

    def get_img_specifically(self):
        var5 = listing_of_accommodationthat_seller_offering.objects.filter(id=self.id)
        print(var5)
        return 0


