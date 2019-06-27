from django.contrib import admin
from . import models


class BootAdmin(admin.ModelAdmin):
    pass


class AccessoryAdmin(admin.ModelAdmin):
    pass


class HatAdmin(admin.ModelAdmin):
    pass


class LowerOuterAdmin(admin.ModelAdmin):
    pass


class UnderPantsAdmin(admin.ModelAdmin):
    pass


class PantsAdmin(admin.ModelAdmin):
    pass


class OuterWearAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Boot, BootAdmin)
admin.site.register(models.Accessory, AccessoryAdmin)
admin.site.register(models.LowerOuter, LowerOuterAdmin)
admin.site.register(models.UnderPants, UnderPantsAdmin)
admin.site.register(models.Pants, PantsAdmin)
admin.site.register(models.OuterWear, OuterWearAdmin)
