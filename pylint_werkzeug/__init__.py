'''pylint_werkzeug module'''

from astroid import MANAGER
from astroid.builder import AstroidBuilder
from astroid import nodes
import textwrap


def register(_):
    '''register is expected by pylint for plugins, but we are creating a transform,
     not registering a checker.

    '''
    pass


def werkzeug_transform(_):
    '''Replace Werkzeug module with the imports it lazily loads.'''
    code = textwrap.dedent('''
        from werkzeug.utils import (escape, environ_property,
            append_slash_redirect, redirect, cached_property, import_string,
            dump_cookie, parse_cookie, unescape, format_string, find_modules,
            header_property, html, xhtml, HTMLBuilder, validate_arguments,
            ArgumentValidationError, bind_arguments, secure_filename)

        from werkzeug.formparser import parse_form_data

        from werkzeug.useragents import UserAgent

        from werkzeug._internal import _easteregg

        from werkzeug.http import (parse_etags, parse_date, http_date,
            cookie_date, parse_cache_control_header, is_resource_modified,
            parse_accept_header, parse_set_header, quote_etag, unquote_etag,
            generate_etag, dump_header, parse_list_header, parse_dict_header,
            parse_authorization_header, parse_www_authenticate_header,
            remove_entity_headers, is_entity_header, remove_hop_by_hop_headers,
            parse_options_header, dump_options_header, is_hop_by_hop_header,
            unquote_header_value, quote_header_value, HTTP_STATUS_CODES)

        from werkzeug.exceptions import abort, Aborter

        from werkzeug.debug import DebuggedApplication

        from werkzeug.datastructures import (MultiDict, CombinedMultiDict,
            Headers, EnvironHeaders, ImmutableList, ImmutableDict,
            ImmutableMultiDict, TypeConversionDict,
            ImmutableTypeConversionDict, Accept, MIMEAccept, CharsetAccept,
            LanguageAccept, RequestCacheControl, ResponseCacheControl, ETags,
            HeaderSet, WWWAuthenticate, Authorization, FileMultiDict,
            CallbackDict, FileStorage, OrderedMultiDict,
            ImmutableOrderedMultiDict)

        from werkzeug.local import (Local, LocalManager, LocalProxy,
            LocalStack, release_local)

        from werkzeug.serving import run_simple

        from werkzeug.wsgi import (get_current_url, get_host, pop_path_info,
            peek_path_info, SharedDataMiddleware, DispatcherMiddleware,
            ClosingIterator, FileWrapper, make_line_iter, LimitedStream,
            responder, wrap_file, extract_path_info)

        from werkzeug.security import (generate_password_hash,
            check_password_hash)

        from werkzeug.wrappers import (BaseResponse, BaseRequest, Request,
            Response, AcceptMixin, ETagRequestMixin, ETagResponseMixin,
            ResponseStreamMixin, CommonResponseDescriptorsMixin,
            UserAgentMixin, AuthorizationMixin, WWWAuthenticateMixin,
            CommonRequestDescriptorsMixin)

        from werkzeug.test import (Client, EnvironBuilder, create_environ,
            run_wsgi_app)

        from werkzeug.urls import (url_decode, url_encode, url_quote,
            url_quote_plus, url_unquote, url_unquote_plus, url_fix, Href,
            iri_to_uri, uri_to_iri)

        from werkzeug.testapp import test_app
    ''')
    module = AstroidBuilder().string_build(code)
    module.name = 'werkzeug'
    return module


def is_werkzeug_module(node):
    '''Predicate for checking if we have the werkzeug module.'''
    return node.name == 'werkzeug'

MANAGER.register_transform(nodes.Module,
                           werkzeug_transform,
                           is_werkzeug_module)
