# Inventory Management

ეს აპლიკაცია გამოიყენება საწყობის მენეჯმენტისთვისი.

1. BaseModel:
   - create_date : DateTimeField : auto_add_now
   - write_date : DateTimeField : auto_now
   - archived : BooleanField : default True

2. Item(BaseModel):
   - name : CharField
   - description : TextField
   - height : FloatFiled : nullable
   - width : FloatField : nullable
   - length : FloatField : nullable
   - weight : FloatField : nullable
   - category : m2o -> Category
   - stock_qty : PositiveInteger
   - expiration_date : DateField : nullable
   
3. Category(BaseModel):
    - name : CharField

### EndPoints
- api/about : GET
- api/items : GET
- api/items : POST
- api/items/id : GET
- api/items/id : PUT
- api/items/id : PATCH
- api/items/id : DELETE
- api/categories : GET
- api/categories : POST
- api/categories/id : GET
- api/categories/id : PUT
- api/categories/id : PATCH
- api/categories/id : DELETE
- api/categories/id/items : GET
- api/categories/id/items : POST
- api/categories/id/items/id : GET
- api/categories/id/items/id : PUT
- api/categories/id/items/id : PATCH
- api/categories/id/items/id : DELETE

