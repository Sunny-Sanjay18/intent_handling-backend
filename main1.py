from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import database_helper

app=FastAPI()

@app.get("/")
async def handle_request(request:Request):
    #Retrive the Jason data from the request
    payload= await request.json()
# Extract the necessary information from the payload
#based on the structure of the webhookRequest from dialogflow
intent = payload['query result']['intent']['displayname']
parameters = payload['qr']['parameters']
output_context = ['qr']['output_context']

intent_handler_dict = {
    'order.complete - context: ongoing-order': track_order,
    'order.complete - context: ongoing-order':complete_order,
    'ordeer.remove - context : ongoing- order':remove_from_order,
    'order.add-context: ongoing_order': add to order

}
return intent_handler_dict[intent](parameters)


inprogress_orders={
    "session_id_1":{"pizza":2,"samosa":1},
    "session_id_2":{"chole":1}
}

def track_order(parameters: dict):
    order_id = parameters['order_id']
    order_status=database_helper.get_order_status(order_id)

    if order_status:
        fulfillment_text=f"the order status from order id: {order_id} is: {order-status}"
    else:
        fulfillment_text = f"no found with order id:{order_id} "

    return JSONResponse(content={
        "fulfillment_text": f"Received =={intent}== in the backend"
})