from rest_framework.response import Response

def success_response(data, message, status_code):
    return Response({
        'data': data,
        'status': status_code,
        'message': message
    }, status=status_code)

def error_response(errors, message, status_code):
    return Response({
        'data': {},
        'status': status_code,
        'message': message,
        'errors': errors
    }, status=status_code)