from rest_framework.permissions import BasePermission
from datetime import date

class PermBookingIsOwnerOrStaff(BasePermission):
	message = "You must be the owner of the booking to make this action."

	def has_object_permission(self, request, view, object):
		if request.user.is_staff or (request.user == object.user):
			return True
		return False

class PermBooking3DaysAway(BasePermission):
	message = "Your booking has to be at least 3 days away to make this action."

	def has_object_permission(self, request, view, object):
		if (object.date - date.today()).days > 3:
			return True
		return False