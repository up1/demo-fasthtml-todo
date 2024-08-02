from fasthtml.common import *
import logging

# Disable logging
logging.getLogger("uvicorn.access").disabled = True


app,rt = fast_app()

@rt('/')
def get(): return Div(P('Hello World!'), hx_get="/change")

@rt('/change')
def get(): return P('Nice to be here!')

serve()