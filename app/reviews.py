from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, InvalidPage
from app.models import Review


def embed_review(request, number):
	critic = None
	review = None
	try:
		review = Review.objects.get(id=number)
		review.readings = review.readings + 1;
		review.save()
	except Exception, e:
		pass
	return render_to_response("embed_review.html", {'review':review})
