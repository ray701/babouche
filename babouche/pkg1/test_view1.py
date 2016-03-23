from pyramid.response import Response


def test3_func(request):
    return Response('test3_func is called')

