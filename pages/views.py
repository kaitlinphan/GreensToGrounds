from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django import forms
from . import forms
from django.views.generic.edit import FormView, CreateView
from .forms import OrderForm

from .models import Order

def homeview(request):
    context = {
        'monthly_boxes': [
            ('March', 'Apples, Spinach, Herbs'),
            ('April', 'Apples, Asparagus, Spinach, Herbs, Strawberries, Onions'),
            ('May', 'Asparagus, Beets, Spinach, Herbs, Strawberries, Onions'),
            ('Add-Ons (Vary Weekly)', 'Cheese, Freshly-Baked Bread, Granola, Chorizo Sausage, Pastured Ground Beef, Hummus, Queso, Salsa, Apple Cider Donuts, Eggs, Honey'),
        ]
    }
    return render(request, 'pages/home.html', context)


# def place_order(request):
#     form = OrderForm(request.POST)


class OrderFormView(FormView):
    template_name = 'g2g/order_form.html'
    form_class = OrderForm
    success_url = 'orderform'

    def form_valid(self, form):
        form.place_order()
        return super().form_valid(form)

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'g2g/order_form.html'
    # fields = ['name']

    def form_valid(self, form):
        form.place_order()
        return super().form_valid(form)

def calendar_view(request):
    return render(request, "pages/calendar.html")

# temporary for navbar
def blog_view(request):
    return render(request, "g2g/blog.html")

def social_view(request):
    return render(request, "g2g/social.html")

def FAQ_view(request):
    return render(request, "g2g/FAQ.html")

def supplier_view(request):
    context = {
        'supplier_list': [
            {
                'name': 'Local Food Hub',
                'address': 'Charlottesville, VA',
                'producers': 'Kristen Suokko (Executive Director)',
                'founded': 'Founded in 2009, G2G Supplier since 2014',
                'extra_details': {},
                'url': 'www.localfoodhub.org',
                'details': 'The Local Food Hub has undoubtedly been one of our most invaluable partners in our mission to connect the UVa community with local produce. The organization was born back in 2009 out of a community-supported discussion that identified a need for greater linkages between small farms and institutions seeking local food: Local farmers were being locked out of markets due to missing infrastructure, delivery minimums, insurance requirements, and time, while businesses and institutions interested in sourcing locally found it challenging to access a consistent supply of produce from small farms. By providing support services, infrastructure, and market opportunities for local farmers, and simplifying the process of buying local for businesses, the Local Food Hub has helped strengthen our local food economy and put local food on more plates in the Charlottesville/Albemarle region.'
            },
            {
                'name': 'Shady Lane Family Farm',
                'address': 'Free Union, Virginia, 20 miles north-west of Charlottesville',
                'producers': 'Luke Yoder & Maynard Swarey',
                'founded': 'Founded in 1999, G2G Supplier since 2014',
                'extra_details': [
                    {'Favorite Products': 'Doris’ homemade granola, free-range eggs GAP Certified*'},
                    {'Awards': 'GAP Certified*, 2012 LFH Partner Producer of the Year'}
                ],
                'url': 'www.shadylanefamilyfarm.com',
                'details': 'For Doris and Nathan Yoder, farming and family go hand in hand - They started Shady Lane Family Farm in 1999 as a way to provide stability and a wholesome upbringing for their ten children. Today, their kitchen table overlooks an orderly four cultivated acres and 5,000 square feet of greenhouse space, which produce a wide variety of vegetables for local markets and wholesale. The Yoders use organic practices - no chemical fertilizers or sprays - and succession planting in order to manage pests and disease, focusing their energy on keeping plants healthy rather than rehabilitating sick ones. Every semester Greens to Grounds staff have enjoyed pulling up to the property to find the kids rope-swinging into the pond and the smell of fresh-baked granola wafting from the bakery. Outside of your Greens to Grounds box, you can find Shady Lane Family Farm produce at both the Market at Foxfield on Thursdays and Charlottesville City Market on Saturdays.'
            },
            {
                'name': 'Caromont Farm',
                'address': 'Albermarle County, 23 miles south of Charlottesville',
                'producers': 'Daniel Page and Gail Hobbs-Page',
                'founded': 'Founded in 2007, G2G Supplier since Spring 2016',
                'extra_details': 'Esmontonian and fresh Farmstead chevre',
                'url': 'www.caromontcheese.com',
                'details': 'Caromont Farm is a hyper-local endeavor that has won national acclaim. Farmers and cheesemakers Daniel Page and Gail Hobbs-Page converted their home and farm into a farmstead goat operation back in 2007 with the goal of crafting quality cheeses with a sense of “place”. Their business centers on the belief that great cheese comes only from great milk. Their goat cheeses come from goats born and milked on the farm - a herd of Alpines, Sannens, and La Mancha goats lovingly referred to as the “Caromont Gals” - while their cow’s milk cheeses are produced with milk from Nathan Vergins’ herd of grass-fed Jerseys at Silky Cow Farm in nearby North Garden, Virginia. Gail and Daniel are strongly committed to supporting their fellow local farmers and producers, so much so that their aged cheeses (Red Row and Esmontonian) are even washed in local apple cider and red wine, respectively.\n\n All Caromont cheeses are made on farm and are hand-ladled, tended daily, and seasonally produced. Their milk comes from animals raised on principles of natural, humane husbandry and grass-based management. To overload the cuteness factor, Caromont flooded national media last winter when they called for volunteers to help snuggle and bottle-feed their 90 new-born kids!'
            },
            {
                'name': 'MarieBette Cafe & Bakery',
                'address': 'Rose Hill, Charlottesville, VA',
                'producers': 'Jason Becton, Patrick Evans (Owners) and Hilary Salmon (Head Baker)',
                'founded': 'Founded 2013, Supplier since Spring, 2016',
                'extra_details': 'Virginia sourdough, traditional baguettes, caneles',
                'url': 'www.mariebette.com',
                'details': 'MarieBette is a European-inspired cafe and bakery, founded on the notion that buying fresh bread from your local bakery should be a daily affair. Owners Jason Becton and Patrick Evans met at the International Culinary Center (formerly the French Culinary Institute) in New York and named the cafe after their daughters, Marian and Betty. Jason’s culinary style was profoundly influenced by his time spent in France, where he saw an appreciation for seasonal ingredients and simple-but-beautiful presentations. Patrick, an Albemarle county native, cites his childhood in a farmhouse in North Garden as foundational to his love of fresh, local ingredients. His background as an artist is evident in Marie Bette’s famous stencil-art.'
            },
            {
                'name': 'Carpe Donut',
                'address': 'Charlottesville, VA',
                'producers': 'Matt Rohdie, Jen Downey & family',
                'founded': 'Founded 2007',
                'extra_details': 'Apple cider donuts, duh!',
                'url': 'www.carpedonut.org',
                'details': 'Carpe Donut! Started in 2007 in Charlottesville as a small, mobile business devoted to making the best and freshest apple cider doughnuts possible; old-fashioned, hand crafted and generously dusted in sugar! And if a delicious and guilt-free donut ever existed, this would be it - Not only are they cooked in 100% pure soybean oil (no trans-fats), but they’re also made with fresh, pasture-raised chicken eggs from Local Food Hub partner farms, and organic flours and apple cider. Carpe Donut! even repurposes some of their used oil as biofuel! Operating from a bright red Gypsy wagon, they’re hard to miss as they make the rounds at local farmers markets, festivals and private events around town, as well as at their retail space on Allied Lane. And as if providing us with their donuts wasn’t enough, they’re also dedicated to giving back to the local food community, acting as friend and incubator to many food entrepreneurs and fledging businesses in Central Virginia by offering guidance, partnership, and production space.'
            },
            {
                'name': "Woodson's Mill",
                'address': 'Lowesville, Virginia (Nelson County)',
                'producers': 'Will Brockenbrough',
                'founded': 'Founded in 1794, G2G Supplier since [semester, year]',
                'extra_details': 'Stone-ground pancake mix',
                'url': 'www.woodsonsmill.com',
                'details': 'Woodson’s Mill is a juxtaposition of history and sustainable innovation - The mill in use today was constructed in 1794 and has been under the care of just a handful of families since then. The Brockenbrough family took the reigns in the 80’s, restoring the mill to operation under the guidance of David Woodson Jr. and miller Steve Roberts. The water-powered mill harnesses energy from the Piney River to stone-grind non-GMO and Virginia-grown corn, wheat, and buckwheat. Slow grinding on hand-dressed millstones helps to preserve the oils, moisture content, nutrients, and unique flavor of each grain. And by sourcing non-GMO, local grains, the Brockenbroughs are investing in non-commodity production among Virginia farms and develop consumer demand for fresh, high quality, and sustainably-produced grains and meals. Outside of your Greens to Grounds box, you can find their products at a variety of markets and specialty shops around Charlottesville.'
            },
        ]
    }
    return render(request, "g2g/supplier.html", context)

def press_view(request):
    return render(request, "g2g/press.html")
