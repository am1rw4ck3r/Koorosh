# Amir Zare / KooRoSH

import os


def sqldorks():
	f = open('sqldorks.txt' , 'a')
	f.write('''
    affiliate.php?ID=
	affiliate-agreement.cfm?storeid=
	affiliates.php?id=
	ancillary.php?ID=
	archive.php?id=
	article.php?id=
	phpx?PageID
	basket.php?id=
	Book.php?bookID=
	book_list.php?bookid=
	book_view.php?bookid=
	BookDetails.php?ID=
	browse.php?catid=
	browse_item_details.php
	Browse_Item_Details.php?Store_Id=
	buy.php?
	buy.php?bookid=
	bycategory.php?id=
	cardinfo.php?card=
	cart.php?action=
	cart.php?cart_id=
	cart.php?id=
	cart_additem.php?id=
	cart_validate.php?id=
	cartadd.php?id=
	cat.php?iCat=
	catalog.php
	catalog.php?CatalogID=
	catalog_item.php?ID=
	catalog_main.php?catid=
	category.php
	category.php?catid=
	category_list.php?id=
	categorydisplay.php?catid=
	checkout.php?cartid=
	checkout.php?UserID=
	checkout_confirmed.php?order_id=
	checkout1.php?cartid=
	comersus_listCategoriesAndProducts.php?idCategory=
	comersus_optEmailToFriendForm.php?idProduct=
	comersus_optReviewReadExec.php?idProduct=
	comersus_viewItem.php?idProduct=
	comments_form.php?ID=
	contact.php?cartId=
	content.php?id=
    Browse_Item_Details.php?Store_Id=
    Category.php?cid=
    GetItems.php?itemid=
    OrderForm.php?Cart=
    Product.php?Showproduct=
    ProductDetails.php?ProdID=
    ProductDetails.php?id=
    ProductList.php?id=
    Select_Item.php?id=
    ShopSearch.php?CategoryID=
    StoreRedirect.php?ID=
    Store_ViewProducts.php?Cat=
    TopResources.php?CategoryID=
    ViewProduct.php?misc=
    about.php?cartID=
    accinfo.php?cartId=
    acclogin.php?cartID=
    add-to-cart.php?ID=
    addItem.php
    addToCart.php?idProduct=
    add_cart.php?num=
    addcart.php?
    addtomylist.php?ProdId=
    adminEditProductFields.php?intProdID=
    advSearch_h.php?idCategory=
    articlecategory.php?id=
    basket.php?id=
    browse_item_details.php
    buy.php?
    buy.php?bookid=
    bycategory.php?id=
    campkc-view-event.php?Item_ID=
    carry-detail.php?prodID=
    cart.php?action=
    cart.php?cart_id=
    cart.php?id=
    cart_additem.php?id=
    cart_validate.php?id=
    cartadd.php?id=
    catalog_item.php?ID=
    category.php
    category.php?CID=
    category.php?Category_ID=
    category.php?ID=
    category.php?c=
    category.php?catID=
    category.php?cat_id=
    category.php?category_id=
    category.php?categoryid=
    category.php?catid=
    category.php?cid=
    category.php?id_category=
    category_id.php?id=
    category_list.php?id=
    category_view.php?category_id=
    categorydisplay.php?catid=
    checkout.php?UserID=
    checkout.php?cartid=
    checkout1.php?cartid=
    checkout_confirmed.php?order_id=
    comersus_listCategoriesAndProducts.php?idCategory=
    comersus_optEmailToFriendForm.php?idProduct=
    comersus_optReviewReadExec.php?idProduct=
    comersus_viewItem.php?idProduct=
    con_product.php?prodid=
    contact.php?cartId=
    content.php?categoryId=
    detail.php?item_id=
    detail.php?prodID=
    details.php?ProdID=
    details.php?Product_ID=
    details.php?prodID=
    discont_productpg.php?product_id=
    display-product.php?Product=
    display_item.php?id=
    displayproducts.php
    downloadTrial.php?intProdID=
    editProduct.php?cid=
    emailToFriend.php?idProduct=
    emailproduct.php?itemid=
    eshop.php?id=
    faq.php?cartID=
    fullDisplay.php?item=
    help.php?CartId=
    index.php?cart=
    index.php?cartID=
    index.php?product=
    item-menu.php?idSubCat=
    item.php?ID=
    item.php?SKU=
    item.php?cat=
    item.php?code=
    item.php?eid=
    item.php?id=
    item.php?iid=
    item.php?item=
    item.php?item_id=
    item.php?itemid=
    item.php?model=
    item.php?prodtype=
    item.php?shopcd=
    item.php?sub_id=
    itemDesc.php?CartId=
    item_book.php?CAT=
    item_details.php?catid=
    item_list.php?cat_id=
    item_list.php?maingroup
    item_show.php?code_no=
    item_show.php?id=
    item_show.php?itemID=
    item_show.php?lid=
    itemdetail.php?item=
    itemdetails.php?catalogid=
    itemlist.php?categoryID=
    js_product_detail.php?pid=
    kids-detail.php?prodID=
    learnmore.php?cartID=
    listcategoriesandproducts.php?idCategory=
    main.php?item=
    main.php?prodID=
    manual.php?product=
    model.php?item=
    order-now.php?prodid=
    order.php?BookID=
    order.php?id=
    order.php?item_ID=
    page_prod.php?id_cat=
    payment.php?CartID=
    pdetail.php?item_id=
    portfolio.html?categoryid=
    powersearch.php?CartId=
    preorder.php?bookID=
    prev_results.php?prodID=
    price.php
    privacy.php?cartID=
    prod.php?Cat=
    prod.php?cat=
    prodView.php?idProduct=
    prod_details.php?id=
    prod_details.php?products_id=
    prod_indiv.php?groupid=
    prodbycat.php?intCatalogID=
    proddetail.php?prod=
    proddetails_print.php?prodid=
    prodetails.php?prodid=
    prodlist.php?catid=
    prodotti.php?id_cat=
    prodrev.php?cat=
    product-detail.php?prodid=
    product-details.php?prodID=
    product-details.php?prodId=
    product-info.php?cat=
    product-list.php?ID=
    product-list.php?category_id=
    product-list.php?cid=
    product-list.php?id=
    product-range.php?rangeID=
    product.php?****=
    product.php?ItemID=
    product.php?ItemId=
    product.php?ProductID=
    product.php?bid=
    product.php?bookID=
    product.php?brand=
    product.php?c=
    product.php?cat=
    product.php?cat_id=
    product.php?fdProductId=
    product.php?id=
    product.php?id_h=
    product.php?inid=
    product.php?intProdID=
    product.php?intProductID=
    product.php?lang=
    product.php?par=
    product.php?pcid=
    product.php?pid=
    product.php?pl=
    product.php?prd=
    product.php?proID=
    product.php?prod_num=
    product.php?prodid=
    product.php?product=
    product.php?product_id=
    product.php?product_no=
    product.php?productid=
    product.php?products_id=
    product.php?proid=
    product.php?rangeid=
    product.php?shopprodid=
    product.php?sku=
    product.search.php?proid=
    product2.php?id=
    product3.php?id=
    productDetail.php?prodID=
    productDetail.php?prodId=
    productDetails.php?id=
    productDetails.php?idProduct=
    productDetails.php?prodId=
    productDisplay.php
    productList.php?cat=
    productList.php?id=
    product_customed.php?pid=
    product_detail.php?id=
    product_detail.php?prodid=
    product_detail.php?product_id=
    product_details.php?id=
    product_details.php?prodID=
    product_details.php?prodid=
    product_details.php?product_id=
    product_info.php?id=
    product_info.php?item_id=
    product_info.php?products_id=
    product_page.php?id=
    product_ranges_view.php?ID=http://howucan.gr
    product_reviews.php?feature_id=
    productdetails.php?prodId=
    productdetails.php?prodid=
    productinfo.php?id=
    productinfo.php?item=
    productlist.php?ViewType=Category&CategoryID=
    productlist.php?cat=
    productlist.php?fid=
    productlist.php?grpid=
    productlist.php?id=
    productlist.php?tid=
    productpage.php
    productpage.php?ID=
    products-display-details.php?prodid=
    products.html?file=
    products.php?DepartmentID=
    products.php?ID=
    products.php?act=
    products.php?area_id=
    products.php?cat=
    products.php?catId=
    products.php?cat_id=
    products.php?categoryID=
    products.php?catid=
    products.php?cid=
    products.php?groupid=
    products.php?id=
    products.php?keyword=
    products.php?mainID=
    products.php?openparent=
    products.php?p=
    products.php?page=
    products.php?parent=
    products.php?req=
    products.php?rub=
    products.php?session=
    products.php?sku=
    products.php?sub=
    products.php?subgroupid=
    products.php?type=
    productsByCategory.php?intCatalogID=
    products_category.php?CategoryID=
    products_connections_detail.php?cat_id=
    products_detail.php?CategoryID=
    products_detail.php?id=
    productsview.php?proid=
    productview.php?id=
    pview.php?Item=
    resellers.php?idCategory=
    savecart.php?CartId=
    search.php?CartID=
    shippinginfo.php?CartId=
    shop.php?a=
    shop.php?action=
    shop.php?bookid=
    shop.php?cartID=
    shop.php?id_cat=
    shop_details.php?prodid=
    shop_display_products.php?cat_id=
    shopaddtocart.php
    shopaddtocart.php?catalogid=
    shopbasket.php?bookid=
    shopbycategory.php?catid=
    shopcafe-shop-product.php?bookId=
    shopcart.php?title=
    shopcreatorder.php
    shopcurrency.php?cid=
    shopdc.php?bookid=
    shopdisplaycategories.php
    shopdisplayproduct.php?catalogid=
    shopdisplayproducts.php
    shopexd.php
    shopexd.php?catalogid=
    shopping.php?id=
    shopping_article.php?id=
    shopping_basket.php?cartID=
    shopprojectlogin.php
    shopquery.php?catalogid=
    shopremoveitem.php?cartid=
    shopreviewadd.php?id=
    shopreviewlist.php?id=
    shoptellafriend.php?id=
    shopthanks.php
    shopwelcome.php?title=
    show.php?item=
    showStore.php?catID=
    show_item.php?id=
    show_item_details.php?item_id=
    show_prod.php?p=
    showproduct.php?cat=
    showproduct.php?prodid=
    showproduct.php?productId=
    showproducts.php?cid=
    shprodde.php?SKU=
    stdetail.php?prodID=
    store-detail.php?ID=
    store-details.php?id=
    store.php?cat_id=
    store.php?id=
    store_bycat.php?id=
    store_listing.php?id=
    store_prod_details.php?ProdID=
    storefront.php?id=
    storefronts.php?title=
    storeitem.php?item=
    subcategory-page.php?id=
    subcategory.php?id=
    template.php?Action=Item&pid=
    updatebasket.php?bookid=
    viewCart.php?userID=
    viewCat_h.php?idCategory=
    viewPrd.php?idcategory=
    view_cart.php?title=
    view_item.php?id=
    view_item.php?item=
    view_items.php?id=
    viewcart.php?CartId=
    viewitem.php?recor=
    viewproduct.php?id=
    viewproduct.php?prod=
    viewproducts.php?id=
    viewstore.php?cat_id=
    voteList.php?item_ID=
    whatsnew.php?idCategory=
    workshopview.php?id=
    ''')
	print " sqldorks are saved in sqldorks.txt"