from zope.cachedescriptors.property import CachedProperty
from silva.core.layout.interfaces import ISilvaSkin
from silva.core import conf as silvaconf
from silva.core.layout.porto.porto import Layout as PortoLayout
from silva.core.layout.porto.interfaces import IPorto
from silva.core.interfaces import IPublication


class IStandardIssue(IPorto):
    """Layer for standard issue theme
    """

    silvaconf.resource('default.css')


class IStandardIssueSkin(IStandardIssue, ISilvaSkin):
    """Skin for standard issue theme
    """

    silvaconf.skin('Standard Issue')


silvaconf.layer(IStandardIssue)


class Layout(PortoLayout):
    
    @CachedProperty
    def publication_title(self):
        return self.context.get_publication().get_title()
    
    @CachedProperty
    def publication_url(self):
        return self.context.get_publication().absolute_url()

    def top_menu_items(self):
        root = self.context.get_root()
        def publishable(x):
            return x.is_published() and IPublication.providedBy(x)
        return filter(publishable, root.get_ordered_publishables())

    def current_publication_class(self, publication):
        if publication in self.request.PARENTS:
            return 'active'
        return ''

    def current_navigation_title(self):
        return self.context.get_container().get_title()
