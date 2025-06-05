def logado(request):
    return {
        'logado': request.user.is_authenticated
    }
