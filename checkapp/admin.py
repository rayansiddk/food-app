from django.contrib import admin
from .models import Location, Restaurant, MenuItem,Category,DeliveryPerson,Review,Order,OrderItem

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'latitude', 'longitude')

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'address', 'latitude', 'longitude')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image' )

@admin.register(DeliveryPerson)
class DeliveryPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_available', 'current_latitude', 'current_longitude')  # Correct field names
    list_editable = ('is_available',)  # Allows inline editing of availability
    list_filter = ('is_available',)  # Add a filter for availability
    search_fields = ('name',)  # Allow searching by name


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant', 'menu_item', 'rating', 'created_at')
    list_filter = ('restaurant', 'menu_item', 'rating', 'created_at')
    search_fields = ('user__username', 'comment')
    readonly_fields = ('created_at',)
    
    # Optional: you can set the ordering
    ordering = ('-created_at',)

# Register the Review model with the customized admin interface
admin.site.register(Review, ReviewAdmin)

admin.site.register(Order)
admin.site.register(OrderItem)
