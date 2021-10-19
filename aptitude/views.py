from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, SubCategory, QuestionBank, Comment
import ast

cats = Category.objects.all()
subcats = SubCategory.objects.all()


def category(request):
    print(cats)
    cats_dict = {'cats': cats, 'subcats': subcats}
    return render(request, 'category.html', cats_dict)


def question(request, subcatname):
    subcatname = subcatname.replace('-', ' ')
    subcategory = SubCategory.objects.get(subCategoryName=subcatname)
    questions_list = QuestionBank.objects.filter(subCategoryId=subcategory)
    for item in range(len(questions_list)):
        questions_list[item].options = ast.literal_eval(questions_list[item].options)
        questions_list[item].options = [n.strip() for n in questions_list[item].options]

    page = request.GET.get('page', 1)
    paginator = Paginator(questions_list, 5)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'question.html', {'questions': questions, 'cats': cats, 'subcats': subcats})


def sub_category(request, catname):
    catname = catname.replace('-', ' ')
    category = Category.objects.filter(categoryName=catname).first()
    subcat = SubCategory.objects.filter(categoryId=category)
    return render(request, 'sub_category.html',
                  {'subcat': subcat, 'catname': catname, 'cats': cats, 'subcats': subcats})


def discussion(request, qid):
    if request.method == "POST":
        comment = request.POST.get('comment', '')
        questionId = request.POST.get('questionId', '')

        if comment:
            comm = Comment(comment=comment,questionId=QuestionBank.objects.get(questionId=questionId))
            comm.save()
    comments = Comment.objects.filter(questionId=qid)

    length = len(comments)

    ques = QuestionBank.objects.get(questionId=qid)
    ques.options = ast.literal_eval(ques.options)
    ques.options = [n.strip() for n in ques.options]
    return render(request, 'discussion.html',
                  {'comments': comments, 'length': length, 'ques': ques, 'cats': cats, 'subcats': subcats})

def aboutus(request):
    return render(request,'aboutus.html')