from pyramid.config import Configurator

import sqlahelper
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_route('test1', '/test1')
    config.add_view('.views.test1_func', route_name='test1')
    config.include('pyramid_chameleon')
    config.include('pyramid_tm')
    # config.add_static_view('static', 'static', cache_max_age=3600)
    # config.add_route('view_wiki', '/')
    # config.add_route('view_page', '/{pagename}')
    # config.add_route('add_page', '/add_page/{pagename}')
    # config.add_route('edit_page', '/{pagename}/edit_page')
    config.scan()

    # sqlalchemyを有効に
    engine = engine_from_config(settings)
    sqlahelper.add_engine(engine)

    return config.make_wsgi_app()