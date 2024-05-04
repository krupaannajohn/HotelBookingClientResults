

from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        location = request.POST.get("location")
        api_url = f'http://127.0.0.1:8000/rooms/{location}/'  # Replace with your API endpoint URL
        response = requests.get(api_url)
        rooms_data = response.json()
        if response.status_code == 200:
            rooms_data = response.json()
            return render(request, 'room_search_results.html', {'rooms_data': rooms_data})
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch room results. Check Again!'})
    
        
    return render(request, 'index.html')
