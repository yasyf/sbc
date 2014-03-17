from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from home.models import CalendarItem, Member, MemberList

class CalendarItemSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return CalendarItem.objects.all()

    def lastmod(self, item):
        return item.time

    def location(self, item):
        return item.get_location()

class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1

    def items(self):
        return ['about', 'contact', 'subscribe', 'events_all', 'index', 'ine_admin', 'ine_drop']

    def location(self, item):
        return reverse(item)

class MemberListSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return MemberList.objects.all()

    def location(self, item):
         return item.get_location()

class MemberSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
    	YEAR = 2014
        return range(YEAR,YEAR+4)

    def location(self, item):
         return reverse('members_by_year',kwargs={'year': item})