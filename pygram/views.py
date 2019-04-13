""" Views """

# Django
from django.http import HttpResponse, JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
# Utilities
from datetime import datetime
from pdb import set_trace

# from json import dumps
# dumps(dictionary) Function to parse a dictionary into a JSON object

def hello_word(request):
    """ Hello world endpoint """
    return HttpResponse('Oh, hello to this world! Current server time is {now}'.format(
      now=datetime.now().strftime('%H:%M - %d/%M/%Y')
    ))


def sorted_numbers(request):
  """ Sorted numbers endpoint """
  # set_trace();
  numbers = []
  try:
    numbers = (request.GET['numbers']).split(',')
  except MultiValueDictKeyError as error:
    print(error)
  ordered_numbers = sorted([int(i) for i in numbers])
  res = {
    'status': 200,
    'body': {
      'message': 'OK',
      'data':ordered_numbers
    }
  }
  return JsonResponse(res, safe=False)
  # return HttpResponse(dumps(res), content_type='application/json')


def greetings(request, name, age):
  """ Greetings endpoint """
  if age < 12:
    res = 'Sorry {}, you are not allowed here'.format(name)
  else:
    res = 'Hello {}! Welcome to pygram'.format(name)
  return HttpResponse(res)

