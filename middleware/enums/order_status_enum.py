# Order Status Enum
INITIALIZED = "initialized"
CONFIRMED = "confirmed"
IN_PROGRESS = "in_progress"
CREATED = "created"
BEING_DELIVERED = "being_delivered"
DELIVERED = "delivered"
PAID = "paid"

order_statuses = (
    (INITIALIZED, 'Initialized'),
    (CONFIRMED, 'Confirmed'),
    (IN_PROGRESS, 'In Progress'),
    (CREATED, 'Created'),
    (BEING_DELIVERED, 'Being Delivered'),
    (DELIVERED, 'Delivered'),
    (PAID, 'Paid')
)