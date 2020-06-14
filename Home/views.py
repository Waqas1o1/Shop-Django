from django.shortcuts import render
from .models import Product,Item,Promotions,TimeDeal
# Create your views here.
def Home(request):

    # Hole Products
    products = Product.objects.all()

    # Woman Products
    woman_pdt = Product.objects.filter(product_category='Woman')
    # Man Products
    Man_pdt = Product.objects.filter(product_category='Man')
    # Kid Products
    Kid_pdt = Product.objects.filter(product_category='Kid')
    ##### Woman all Items
    woman_items = Item.objects.filter(item_category=woman_pdt.first())
    #Woman Sub_Catagories 
    woman_ctg = { item.item_subCategory for item in woman_items }
    ##### Man all Items
    man_items = Item.objects.filter(item_category=Man_pdt.first())
    #Man Sub_Catagories 
    man_ctgy = { item.item_subCategory for item in man_items}
    ##### Promotion Deals
    #All Promotions
    pro = Promotions.objects.all()
    # Time Promotion
    time_pro = TimeDeal.objects.all()
    send_data = {'Products':products,'Promotions':pro,'Time_Deal':time_pro,"woman_items":woman_items,
                'woman_ctg':woman_ctg,'man_items':man_items,'man_ctg':man_ctgy}
    return render(request,'home/index.html',send_data)
def Product_view(request,pid):
    pdt = Item.objects.filter(item_id=pid)
    ctg = pdt[0].item_subCategory
    relative_pdt = Item.objects.all()
    search_realted = Search_pdt(relative_pdt,ctg)
    #extra images
    send_ex = []
    send_ex.append(pdt[0].item_zoom_pic1)
    send_ex.append(pdt[0].item_zoom_pic2)
    send_ex.append(pdt[0].item_zoom_pic3)

    send_pdt = {"product":pdt[0],'realted_products':search_realted, 'item_zoom_pic':send_ex}
    return render(request,'home/product.html',send_pdt)

def Search_pdt(pdt,ctg):
    related = []
    for pos,p in enumerate(pdt):
        if  ctg in p.item_subCategory or p.item_discription:
            related.append(p)
        if pos == 3:
            break
    return related

