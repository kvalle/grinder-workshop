# The Grinder 3.4
# HTTP script recorded by TCPProxy at Mar 28, 2012 10:59:07 PM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("localhost", 8001)

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

connectionDefaults.defaultHeaders = \
  [ NVPair('Accept-Language', 'nb-no,nb;q=0.9,no-no;q=0.8,no;q=0.6,nn-no;q=0.5,nn;q=0.4,en-us;q=0.3,en;q=0.1'),
    NVPair('Accept-Encoding', 'gzip, deflate'),
    NVPair('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:10.0.2) Gecko/20100101 Firefox/10.0.2'), ]

headers0= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ]

headers1= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://grinder.espenhh.com/simple/'), ]

headers2= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'), ]

url0 = 'http://grinder.espenhh.com:80'

# Create an HTTPRequest for each request, then replace the
# reference to the HTTPRequest with an instrumented version.
# You can access the unadorned instance using request101.__target__.
# Espens cimment
request101 = HTTPRequest(url=url0, headers=headers0)
request101 = Test(101, 'GET simple').wrap(request101)

request102 = HTTPRequest(url=url0, headers=headers0)
request102 = Test(102, 'GET /').wrap(request102)

request103 = HTTPRequest(url=url0, headers=headers1)
request103 = Test(103, 'GET img.jpg').wrap(request103)

request104 = HTTPRequest(url=url0, headers=headers2)
request104 = Test(104, 'GET favicon.ico').wrap(request104)

request105 = HTTPRequest(url=url0, headers=headers0)
request105 = Test(105, 'GET favicon.ico').wrap(request105)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET simple (requests 101-105)."""
    
    # Expecting 301 'Moved Permanently'
    result = request101.GET('/simple')

    grinder.sleep(20)
    request102.GET('/simple/')

    grinder.sleep(177)
    request103.GET('/simple/img.jpg')

    grinder.sleep(526)
    request104.GET('/favicon.ico')

    grinder.sleep(28)
    request105.GET('/favicon.ico')

    return result

  def __call__(self):
    """This method is called for every run performed by the worker thread."""
    self.page1()      # GET simple (requests 101-105)


def instrumentMethod(test, method_name, c=TestRunner):
  """Instrument a method with the given Test."""
  unadorned = getattr(c, method_name)
  import new
  method = new.instancemethod(test.wrap(unadorned), None, c)
  setattr(c, method_name, method)

# Replace each method with an instrumented version.
# You can call the unadorned method using self.page1.__target__().
instrumentMethod(Test(100, 'Page 1'), 'page1')
