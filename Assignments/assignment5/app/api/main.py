from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from .models import models, schemas
from .controllers import orders, sandwiches, resources, order_details, recipes
from .dependencies.database import engine, get_db
from .models.models import OrderDetail, Recipe
from .models.schemas import SandwichBase, ResourceCreate

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)

@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)

@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order

@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)

@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)

@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwich"])
def createSandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db) ):
    return sandwiches.create(db=db, sandwich=sandwich)


@app.get("/sandwiches/", response_model=list[schemas.Sandwich] , tags=["Sandwich"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)

@app.get("/sandwiches/{sandwich_id}", tags=["Sandwich"], response_model=schemas.Sandwich)
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwichID=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwich

@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwich"])
def update_one_sandwich(sandwichID: int, sandwich: schemas.SandwichUpdate , db: Session = Depends(get_db)):
    db_sandwich = sandwiches.read_one(db, sandwichID=sandwichID)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    updated_sandwich = sandwiches.update(db=db, sandwichID=sandwichID, sandwich=sandwich)
    return updated_sandwich

@app.delete("/sandwiches/{sandwich_id}", tags=["Sandwich"])
def delete_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwichID=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwiches.delete(db=db, sandwichID=sandwich_id)



@app.post("/resources/", response_model=schemas.Resource ,tags=["Resources"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, resource=resource)

@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)

@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def update_one_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    resources_db = resources.read_one(db, resource_id=resource_id)
    if resources_db is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.update(db=db, resource=resource, resource_id=resource_id)

@app.delete("/resources/{resource_id}", tags=["Resources"])
def delete_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.delete(db=db, resource_id=resource_id)


@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipe.create(db=db, recipe=recipe)

@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)

@app.get("/recipes/{recipie_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.put("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def update_one_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    recipe_db = recipes.read_one(db, recipe_id=recipe_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return Recipe.update(db=db, recipe=recipe, recipe_id=recipe_id)

@app.delete("/recipes/", tags=["Recipes"])
def delete_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe.delete(db=db, recipe_id=recipe_id)

@app.post("/orderDetails/", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def create(order_detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db=db, order_details=order_detail)

@app.get("/orderDetails/", response_model=list[schemas.OrderDetail], tags=["OrderDetails"])
def read_order_Details(db: Session = Depends(get_db)):
    return order_details.read_all(db=db)

@app.get("/orderDetails/{order_details_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def read_one_order_detail(order_details_id: int, db: Session = Depends(get_db)):
    order_detail =  order_details.read_one_order_details(db, order_details_id=order_details_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order_detail

@app.put("/orderDetails/{order_details_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def update_one_order(order_details_id: int, order: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    orderDetails_db = order_details.read_one_order_details(db=db, order_details_id=order_details_id)

    if orderDetails_db is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order_details.update(db=db, order_details_id=order_details_id, order_details=order)


@app.delete("/orderDetails/{order_details_id}", tags=["OrderDetails"])
def delete_one_order(order_details_id: int, db: Session = Depends(get_db)):
    orderDetails = order_details.read_one_order_details(db=db, order_details_id=order_details_id)
    if orderDetails is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order_details.delete(db=db, order_details_id=order_details_id)

