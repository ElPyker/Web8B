from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

from core import models
from core import forms


# # # # #  C R U D G R A N T G O A L S # # # # #


# # # C R E A T E # # #
class NewGrantGoal(generic.CreateView):
    template_name = "core/create_gg.html"
    model = models.GrantGoal
    form_class = forms.NewGrantGoalForm
    success_url = reverse_lazy("core:list_gg")


# # # R E T R I E V E # # #
# # List
class ListGrantGoal(generic.View):
    template_name = "core/list_gg.html"
    context = {}

    def get(self, request):
        self.context = {
            "grantgoals": models.GrantGoal.objects.filter(status=True)
        }
        return render(request, self.template_name, self.context)

# # Detail
class DetailGrantGoal(generic.View):
    template_name = "core/detail_gg.html"
    context = {}

    def get(self, request, pk):
        self.context = {
            "grantgoal": models.GrantGoal.objects.get(pk=pk)
        }
        return render(request, self.template_name, self.context)


# # # U P D A T E # # #
class UpdateGrantGoal(generic.UpdateView):
    template_name = "core/update_gg.html"
    model = models.GrantGoal
    form_class = forms.UpdateGrantGoalForm
    success_url = reverse_lazy("core:list_gg")


# # # D E L E T E # # #
class DeleteGrantGoal(generic.DeleteView):
    template_name = "core/delete_gg.html"
    model = models.GrantGoal
    success_url = reverse_lazy("core:list_gg")


# # # # #  C R U D S U B G R A N T G O A L S # # # # #


# # # C R E A T E # # #
class NewSubGrantGoal(generic.CreateView):
    template_name = "core/create_sgg.html"
    model = models.SubGrantGoal
    form_class = forms.NewSubGrantGoalForm
    success_url = reverse_lazy("core:list_sgg")

# # # R E T R I E V E # # #
# # List

class ListSubGrantGoal(generic.ListView):
    template_name = "core/list_sgg.html"
    queryset = models.SubGrantGoal.objects.filter(status=True)
    
    # def get_queryset(self):
    #     return models.objects.filter(status=True)

# # Detail
class DetailSubGrantGoal(generic.DetailView):
    template_name = "core/detail_sgg.html"
    model = models.SubGrantGoal



# # # U P D A T E # # #
class UpdateSubGrantGoal(generic.UpdateView):
    template_name = "core/update_sgg.html"
    model = models.SubGrantGoal
    form_class = forms.UpdateSubGrantGoalForm
    success_url = reverse_lazy("core:list_sgg")


# # # D E L E T E # # #
class DeleteSubGrantGoal(generic.DeleteView):
    template_name = "core/delete_sgg.html"
    model = models.SubGrantGoal
    success_url = reverse_lazy("core:list_sgg")


# # # # #  C R U D G O A L S # # # # #


# # # C R E A T E # # #
class NewGoal(generic.CreateView):
    template_name = "core/create_g.html"
    model = models.SubGrantGoal
    form_class = forms.NewGoalForm
    success_url = reverse_lazy("core:list_g")

# # # R E T R I E V E # # #
# # List
class ListGoal(generic.ListView):
    template_name = "core/list_g.html"
    queryset = models.Goal.objects.filter(status=True)
    
# # Detail
class DetailGoal(generic.DetailView):
    template_name = "core/detail_g.html"
    model = models.Goal

    def get(self, request, pk):
        self.context = {
            "goal": models.Goal.objects.get(pk=pk)
        }
        return render(request, self.template_name, self.context)

# # # U P D A T E # # #
class UpdateGoal(generic.UpdateView):
    template_name = "core/update_g.html"
    model = models.Goal
    form_class = forms.UpdateGoalForm
    success_url = reverse_lazy("core:list_g")


# # # D E L E T E # # #
class DeleteGoal(generic.DeleteView):
    template_name = "core/delete_g.html"
    model = models.Goal
    success_url = reverse_lazy("core:list_g")


# # # # #  C R U D I S S U E S  # # # # #


# # # C R E A T E # # #
class NewIssue(generic.CreateView):
    template_name = "core/create_i.html"
    model = models.Issue
    form_class = forms.NewIssueForm
    success_url = reverse_lazy("core:list_i")

# # # R E T R I E V E # # #
# # List
class ListIssue(generic.ListView):
    template_name = "core/list_i.html"
    queryset = models.Issue.objects.filter(status=True)
    
# # Detail
class DetailIssue(generic.DetailView):
    template_name = "core/detail_i.html"
    model = models.Issue


# # # U P D A T E # # #
class UpdateIssue(generic.UpdateView):
    template_name = "core/update_i.html"
    model = models.Issue
    form_class = forms.UpdateIssueForm
    success_url = reverse_lazy("core/list_i")


# # # D E L E T E # # #
class DeleteIssue(generic.DeleteView):
    template_name = "core/delete_i.html"
    model = models.Issue
    success_url = reverse_lazy("core:list_i")


# # # # #  C R U D A R E A S # # # # #


# # # C R E A T E # # #
class NewArea(generic.CreateView):
    template_name = "core/create_a.html"
    model = models.Area
    form_class = forms.NewAreaForm
    success_url = reverse_lazy("core:list_a")

# # # R E T R I E V E # # #
# # List
class ListArea(generic.ListView):
    template_name = "core/list_a.html"
    model = models.Area
    
# # Detail
# class DetailArea(generic.DeleteView):
#     template_name = "core/detail_a.html"
#     model = models.Area



# # # U P D A T E # # #
class UpdateArea(generic.UpdateView):
    template_name = "core/update_a.html"
    model = models.Area
    form_class = forms.UpdateAreaForm
    success_url = reverse_lazy("core:list_a")


# # # D E L E T E # # #
class DeleteArea(generic.DeleteView):
    template_name = "core/delete_a.html"
    model = models.Area
    success_url = reverse_lazy("core:list_a")