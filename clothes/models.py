from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

class Clothes(models.Model):
    titles =  models.CharField(max_length=100)
    descriptoin = models.TextField(max_length=2000, default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt, libero quis laoreet tincidunt, augue risus volutpat ipsum, ut fermentum mauris urna quis nulla. Proin sed ipsum sed justo convallis faucibus. Vivamus viverra, metus ut ullamcorper fringilla, lectus metus dictum purus, ac gravida nisl risus sit amet nisl. Curabitur consequat, mauris at fermentum vulputate, lacus sem gravida turpis, et finibus leo risus iaculis neque. Nullam tincidunt, ipsum sed elementum porttitor, mauris turpis lobortis nisl, sit amet rutrum libero diam id libero. Curabitur blandit erat id odio gravida accumsan. Mauris dolor massa, pharetra vulputate suscipit in, sollicitudin vitae nunc. Morbi fringilla accumsan sapien nec commodo. Ut sit amet est dui. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec elementum purus et libero condimentum tincidunt. Suspendisse tincidunt eget purus sit amet dapibus. Pellentesque et finibus purus. Praesent accumsan lacus lectus, vel imperdiet turpis imperdiet sed. Maecenas bibendum viverra magna, ac tempor ante rutrum dignissim. ')
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.titles}-{", ". join(i.name for i in self.tags.all())}'
    
    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'