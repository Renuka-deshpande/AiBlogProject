from django.shortcuts import render, request, redirect
from . models import AiQuery

def ai_chat(request):
    if request.method == 'POST':
        query_text = request.POST.get('query')
        response = "This is a placeholder response for the query: " + query_text
        
        AiQuery.objects.create(user=request.user, query_text=query_text, response=response)        
        return render(request, 'AIApp/aichat.html', {'response': response})    
    return render(request, 'AIApp/aichat.html')

def ai_summarizer(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        # Here you would typically process the text and generate a summary
        summary = "This is a placeholder summary for the text: " + text
        
        return render(request, 'AIApp/ai_summarizer.html', {'summary': summary})
    
    return render(request, 'AIApp/ai_summarizer.html')

def ai_tags_generator(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        # Here you would typically process the text and generate tags
        tags = "tag1, tag2, tag3"  # Placeholder tags
        
        return render(request, 'AIApp/ai_tags_generator.html', {'tags': tags})
    
    return render(request, 'AIApp/ai_tags_generator.html')
