class ActionRouter:
    def __init__(self):
        self._routes = {}

    def register(self, route, action):
        """ Register route """
        self._routes[route] = action

    def registerAll(self, routes):
        """ Register all routes """
        self._routes.update(routes)

    def get(self, route):
        """ Get action by route """
        if route not in self._routes:
            raise ValueError(f"Route {route} not registered")
        return self._routes[route]

    def execute(self, route):
        """ Execute route """
        action = self.get(route)
        action.execute()
    
    def bind(self, signal, route):
        """ Bind signal with the route """
        signal.connect(lambda: self.execute(route))
