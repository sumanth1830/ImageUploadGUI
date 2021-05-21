from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
import os
import glob
from .helperfunctions import predict_cnn_model, create_cnn_model


# Create your views here.
def home(request):
    return render(request, "home.html")


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')


def image_pose_finder(request):
    list_of_files = glob.glob('media/*')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    create_cnn_model()
    result = predict_cnn_model(latest_file)
    return render(request, 'pose_finder.html', {"image_path": latest_file, "pose_name": result})
