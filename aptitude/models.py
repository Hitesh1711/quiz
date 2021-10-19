from django.db import models


class Category(models.Model):
    categoryId = models.IntegerField(primary_key=True)
    categoryName = models.CharField(max_length=100)
    image = models.ImageField(upload_to="aptitude/images", blank = True)
    iconName = models.CharField(max_length=50, default='ti-bar-chart')
    description = models.CharField(max_length=300, default='Content')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.categoryName
    def to_url(self):
        return self.categoryName.replace(' ', '-')



class SubCategory(models.Model):
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategoryId = models.IntegerField(primary_key=True)
    subCategoryName = models.CharField(max_length=250)
    image = models.ImageField(upload_to="aptitude/images", blank = True)
    description = models.CharField(max_length=300, default='Content')

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.subCategoryName
    def to_url(self):
        return self.subCategoryName.replace(' ', '-')



class QuestionBank(models.Model):
    subCategoryId = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    questionId = models.AutoField(primary_key=True)
    question = models.TextField()
    options = models.TextField()
    answer = models.CharField(max_length=5)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question


class Comment(models.Model):

    comment = models.CharField(max_length=500)
    questionId = models.ForeignKey(QuestionBank,on_delete=models.CASCADE,default=1)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.comment