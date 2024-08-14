from django.shortcuts import render

# Create your views here.
def fun(request):
    d={'buses':[{'id':1,'name':'Naresh','time':7,'route':'Dharmavaram'},
                {'id':2,'name':'puspa','time':8,'route':'Tadipatri'},
                {'id':3,'name':'Hari','time':7,'route':'ATP'},
    ]}
    return render(request,'temp.html',d)