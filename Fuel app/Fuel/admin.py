from django.contrib import admin
from .models import User, FuelRequest
from .forms import AssignFuelRequstForm

admin.site.register(User)


def fuel_request_assign(user, batch_size):
    availables = FuelRequest.objects.filter(
        status=FuelRequest.Status.LOOKING_FOR_AGENT, supervisor=None
    ).order_by('created_at').values_list('pk', flat=True)[:batch_size]

    FuelRequest.objects.filter(pk__in=availables).update(supervisor=user)


@admin.register(FuelRequest)
class FuelRequestAdmin(admin.ModelAdmin):
    form = AssignFuelRequstForm

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        queryset = FuelRequest.objects.order_by("created_at").filter(
            supervisor=request.user, status=FuelRequest.Status.LOOKING_FOR_AGENT)
        if not queryset:
            fuel_request_assign(request.user, 5)
            queryset = FuelRequest.objects.order_by("created_at").filter(
                supervisor=request.user, status=FuelRequest.Status.LOOKING_FOR_AGENT)
        return queryset

    def save_model(self, request, obj, form, change) -> None:
        if obj.status == FuelRequest.Status.LOOKING_FOR_AGENT and obj.agent:
            obj.status = FuelRequest.Status.IN_PROGRESS
        return super().save_model(request, obj, form, change)
