from django.shortcuts import render


def index(request):

    color_a = '#800080'
    color_b = '#ffffff'
    color_c = '#800080'
    color_d = '#800080'
    color_e = '#800080'
    context={'color_a': color_a, 'color_b': color_b, 'color_c': color_c, 'color_d': color_d, 'color_e': color_e}
    return render(request, 'heatmap/index.html', context)
