from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Photo

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})

class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        """
        업로드 완료 후, 이동할 페이지 (오버라이드)
        :param form:
        :return:
        """
        form.instance.author_id = self.request.id
        if form.is_valid():  # 유효성 검사
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'



