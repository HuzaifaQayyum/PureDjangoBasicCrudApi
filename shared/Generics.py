from shared.mixins.Response import JsonResponse
from django.forms.models import model_to_dict
from django.http import Http404
from django.views import View

class BaseView:
    def get_model(self, *args, **kwargs):
        raise NotImplementedError

    def get_form(self, *args, **kwargs):
        raise NotImplementedError

class BaseDetailView(BaseView):
    def get_pk(self):
        raise NotImplementedError


class ListView(BaseView):
    def get(self, request):
        all_model_objects = self.get_model().objects.all()
        return JsonResponse(all_model_objects)

class CreateView(BaseView):
    def post(self, request, format=None):
        form = self.get_form(request.body)
        if (not form.is_valid()):
            return JsonResponse(form.errors, 400)
        
        data = form.cleaned_data
        category = self.get_model().objects.create(**data)

        return JsonResponse(category, status=200)

class RetrieveView(BaseDetailView):
    def __get_object(self, pk):
        try:
            model_object = self.get_model().objects.get(**{self.get_pk(): pk})
        except self.get_model().DoesNotExist:
            raise Http404
        else:
            return model_object

    def get(self, request, pk, format=None):
        model_object = self.__get_object(pk)
        return JsonResponse(model_object)

    
    def delete(self, request, pk, format=None):
        model_object = self.__get_object(pk)
        model_object.delete()
        return JsonResponse({**model_to_dict(model_object), self.get_pk(): pk })

    def put(self, request, pk, format=None):
        form = self.get_form(request.body)
        if (not form.is_valid()):
            return JsonResponse(form.errors, 400)

        model_object = self.__get_object(pk)

        model_object.__dict__.update(**form.cleaned_data)
        model_object.save()

        return JsonResponse(model_object)

    def patch(self, request, pk, format=None):
        model_object = self.__get_object(pk)

        form = self.get_form({**model_object, **request.body})
        if (not form.is_valid()):
            return JsonResponse(form.errors, 400)


        model_object.__dict__.update(**form.cleaned_data)
        model_object.save()

        return JsonResponse(model_object)