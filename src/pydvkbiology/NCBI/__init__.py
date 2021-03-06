"""Initialize the NCBI subpackage, which can contain multiple python modules (files)."""

from pkg_resources import get_distribution, DistributionNotFound

__project__ = 'PyDkBio'
__version__ = None # required for initial installation

try:
  __version__ = get_distribution('PyDkBio').version
except DistributionNotFound:
  VERSION = __project__ + '-' + '(local)'
else:
  VERSION = __project__ + '-' + __version__
  

