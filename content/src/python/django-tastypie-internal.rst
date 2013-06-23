Using Tastypie Inside Django
############################

:date: 2012/11/21
:tags: django, python

Make use of a Tastypie's API from within Django
===============================================

Tastypie is an excellent way to generate a REST API with minimal coding.  But often it exists as a separate means of accessing your data, with its own implementation of your business logic, while your views also implement business logic.

If you make an API, why not use it?

The basic wrapper:

.. code-block:: python

  from django.core.urlresolvers import resolve, Resolver404
  from django.http import HttpRequest

  def rest(path, query={}, data={}, headers={}, method="GET"):
      """
      Converts a RPC-like call to something like a HttpRequest, passes it
      to the right view function (via django's url resolver) and returns
      the result.
    
      Args:
          path: a uri-like string representing an API endpoint. e.g. /v1/resource/27
          query: dictionary of GET-like query parameters to pass to view
          data: dictionary of POST-like parameters to pass to view
          headers: dictionary of extra headers to pass to view (will end up in request.META)
          method: HTTP verb for the emulated request
      Returns:
          a tuple of (status, content):
              status: integer representing an HTTP response code
              content: string, body of response; may be empty
      """
      #adjust for lack of trailing slash, just in case
      if path[-1] != '/':
          path += '/'
          
      hreq = FakeHttpRequest()
      hreq.path = path
      hreq.GET = query
      hreq.POST = data
      hreq.META = headers
      hreq.method = method
      try:
          view = resolve(hreq.path)
          res = view.func(hreq, *view.args, **view.kwargs)
      except Resolver404:
          return (404, '')
    
      return (res.status_code, res._container) #container is the untouched content before HttpResponse mangles it.

  class FakeHttpRequest(HttpRequest):
      """
      Custom version of Django's HttpRequest to minimize unnecessary work
      for in-process requests.
      """
      _read_started = False
    
      @property
      def raw_post_data(self):
          """
          Instead of providing a file-like object representing the body
          of the request, just return the internal dict; tastypie copes with
          this just fine.
          """
          return self.POST


Then, to call it:

.. code-block:: python

  def view_list(request):
    res = rest("/api/v1/mymodel/")
    objects = json.loads(res)
    return render(request, 'mytemplate.html', {'list': objects})

A couple annoyances, though:
#. FakeHttpRequest is a bit of a hack.  It'd be nice to be able to talk to the api object directly.  On the upside, you can use this to call views other than API views.
#. TastyPie serializes the outgoing data, since it thinks it is headed out over HTTP.  It'd be nice to skip this step.

A fix for the second annoyance:

.. code-block:: python

  from tastypie.serializers import Serializer

  class CustomNoneSerializer(Serializer):
      """
      A custom serializer for TastyPie allowing "none" as an encoding type.
      
      Resources need to specify this serializer as Meta.serializer.
      See http://django-tastypie.readthedocs.org/en/latest/serialization.html

      @todo: Is there a better way to tell TastyPie to not do any serialization per-request
          (without breaking a hypothetical HTTP REST service)?
      """
      formats = Serializer.formats + ['none']
      content_types = Serializer.content_types
      content_types['none'] = 'none/none'
    
      def to_none(self, data, options=None):
          """
          Outbound 'serializer'.
          """
          #If the object is a tastypie bundle containing a dict, just return the dict.
          if hasattr(data, 'data'):
              return data.data
          elif isinstance(data, dict):
              if 'objects' in data:
                  data['objects'] = [foo.data for foo in data['objects']]
          return data
    
      def from_none(self, data, options=None):
          return data



And now add this to FakeHttpRequest:

.. code-block:: python

      @property
      def encoding(self):
          """
          We're passing python native types around and not encoding anything,
          so all FakeHttpRequests are encoded as 'none/none'.
          """
          return 'none/none'

Now you get python dictionaries back.
