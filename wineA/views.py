from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Gin (request):
    return HttpResponse('''<h1> Gin is a flavored alcoholic beverage with juniper as its predominant flavorant, usually produced by distillation in copper stills traditionally used for spirit production </h1>
                        
                        <img src='https://www.nestorliquor.com/cdn/shop/articles/IMG1_10_0c0e793a-2e90-46f9-9390-499192f47054.jpg?v=1692251757' width="450" height="500" >
                        
                        '''
                        )
def vodka (request):
    return HttpResponse('''<h1>Vodka is a clear distilled liquor from Europe with a neutral flavor.</h1>
                        <br>

                          <b> <h2> Popular brand names: Tito’s Vodka, Skyy Vodka, Absolut Vodka </h2> </b> 
                           </br>
                           
                           <img src='https://www.nestorliquor.com/cdn/shop/articles/13_Best_Vodka_Brands_Under_30.jpg?v=1687474771'  width="450" height="500" >
                           ''')
def Whiskey (request):
    return HttpResponse('''<h2> Whiskey is a distilled liquor made from grain mash. There are many types of whiskey from different regions. Popular styles are 
                        <i> Bourbon, Rye Whiskey, Scotch Whisky, Canadian Whisky, Japanese Whisky, Tennessee Whiskey and Irish Whiskey</i> .
                        There are also flavored whiskies, like Peanut Butter Whiskey and Fireball Whisky. </h2>
                        
                        <img src='https://theflaskandbarrel.com/wp-content/uploads/2023/07/whiskey-1024x628.jpg'>
                       ''')