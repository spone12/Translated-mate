from classes.menu.actions.actionInterface import ActionInterface


class GoToRouteAction(ActionInterface):
    def __init__(self, widget, navigator, route, beforeAction=None):
        self.navigator = navigator
        self.route = route

        # Registering prepare-logic
        self.navigator.register(route, beforeAction)

        # UI subscription
        widget.clicked.connect(self.execute)
        

    def execute(self):
        """
            Initializing program windows
        """
        
        self.navigator.goTo(self.route)
