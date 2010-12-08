from django.db.models.base import ModelBase

class PubSub(object):
    """
    Manages models to be published

    registry is a dict of nodes mapped to
    models. Nodes are used in pubsub server
    to classify diffrerent event sources
    """
    def __init__(self, registry=None):
        self.registry =  registry or {}
        
    def register(self, model_or_iterable):
        """
        Registers single model or an iterable containing models
        """
        if isinstance(model_or_iterable, ModelBase):
            model_or_iterable = [model_or_iterable]
        for model in model_or_iterable:
            node = make_node(model)
            self.registry[node] =  model

def make_node(model):
    """
    Makes a pubsub node from a model

    E.g. node for 'blog.models.Entry'
    would be 'blog/models/Entry'
    """
    return "%s/%s" %(model.__module__.replace('.', '/'),
            model.__name__)

pubsub = PubSub()
