from .tasks import router as tasks_router
from .ping import router as ping_router
from .analytics import router as analytics_router

routers = [tasks_router, ping_router, analytics_router]


