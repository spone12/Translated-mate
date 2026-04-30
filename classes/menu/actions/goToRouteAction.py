from .abstractAction import AbstractAction

class GoToRouteAction(AbstractAction):
    def __init__(self, routeWidget, navigator, route, beforeAction=None):
        self.navigator = navigator
        self.route = route
        self.routeWidget = routeWidget

        # Registering prepare-logic
        self.navigator.register(route, beforeAction)

        # UI subscription
        self.widget.clicked.connect(self.execute)
        

    def execute(self):
        """
            Initializing program windows
        """
        
        self.navigator.goTo(self.route)
        
    @property
    def widget(self):
        """ Get current widget """
        return self.routeWidget
