#!/usr/bin/env python2
from requests import session
from json import loads, dumps

class DeskCRM(object):
    def __init__(self, user, secret):
        self.user, self.secret = user, secret
        self.auth = (self.user, self.secret)
        self.base_uri = "https://bonline.desk.com/api/v2"
        self.s = session()
        self.s.headers["Accept"] = "application/json"
        self.s.headers["Content-Type"] =  "application/json"
        self.s.auth = self.auth

######################  
## ARTICLES METHODS ##
######################


    def articles_list(self):
        url_vars = (self.base_uri)
        articles_url = "%s/arcticles" % url_vars
        r = self.s.get(articles_url)
        response =  loads(r.content)
        return response

    def articles_show(self, article_id):
        url_vars = (self.base_uri, article_id)
        articles_url = "%s/articles/%s" % url_vars
        r = self.s.get(articles_url)
        response =  loads(r.content)
        return response

    def articles_create(self, article):
        url_vars = (self.base_uri)
        articles_url = "%s/articles" % url_vars
        r = self.s.post(articles_url, data=loads(article))
        response =  loads(r.content)
        return response

    def articles_update(self, article_id, article):
        url_vars = (self.base_uri, article_id)
        articles_url = "%s/articles/%s" % url_vars
        r = self.s.patch(articles_url, data=loads(article))
        response =  loads(r.content)
        return response

    def articles_delete(self, article_id):
        url_vars = (self.base_uri, article_id)
        articles_url = "%s/articles/%s" % url_vars
        r = self.s.delete(articles_url)
        response =  loads(r.content)
        return response

    def articles_search(self, query):
        url_vars = (self.base_uri, 
            query["text"], 
            query["topic_ids"], 
            query["brand_ids"], 
            query["in_support_center"])
        articles_url = "%s/articles/search?" 
        articles_url = articles_url + "text=%s&" 
        articles_url = articles_url + "topic_ids=%s&"
        articles_url = articles_url + "brand_ids=%s&"
        articles_url = articles_url + "in_support_center=%s"
        articles_url = articles_url % url_vars
        r = self.s.get(articles_url)
        response =  loads(r.content)
        return response

    def articles_list_attachments(self, article_id):
        url_vars = (self.base_uri, article_id)
        articles_url = "%s/articles/%s/attachments" % url_vars
        r = self.s.get(articles_url)
        response =  loads(r.content)
        return response

    def articles_attachment_urls(self, article_id, attachment_id):
        url_vars = (self.base_uri, article_id, attachment_id)
        articles_url = "%s/articles/%s/attachments/%s/url" % url_vars
        r = self.s.get(articles_url)
        response =  loads(r.content)
        return response

    def articles_list_translations(self, article_id):
        url_vars = (self.base_uri, article_id)
        articles_url = "%s/articles/%s/translations" % url_vars
        r = self.s.get(articles_url)
        response =  loads(r.content)
        return response

    def articles_show_translation(self, article_id, locale):
        url_vars = (self.base_uri, article_id, locale)
        articles_url = "%s/articles/%s/translations/%s" % url_vars
        r = self.s.get(articles_url)
        response =  loads(r.content)
        return response

    def articles_create_translation(self, article_id, translation):
        url_vars = (self.base_uri, article_id, translation)
        articles_url = "%s/articles/%s/translations" % url_vars
        r = self.s.post(articles_url, data=loads(translation))
        response =  loads(r.content)
        return response

##################  
# BRANDS METHODS #
##################

    def brands_list(self):
        url_vars = (self.base_uri)
        brands_url = "%s/brands" % url_vars
        r = self.s.get(brands_url)
        response =  loads(r.content)
        return response

    def brands_show(self, brand_id):
        url_vars = (self.base_uri, brand_id)
        brands_url = "%s/brands/%s" % url_vars
        r = self.s.get(brands_url)
        response =  loads(r.content)
        return response

    def brands_list_articles(self, brand_id):
        url_vars = (self.base_uri, brand_id)
        brands_url = "%s/brands/%s/articles" % url_vars
        r = self.s.get(brands_url)
        response =  loads(r.content)
        return response

    def brands_list_topics(self, brand_id):
        url_vars = (self.base_uri, brand_id)
        brands_url = "%s/brands/%s/topics" % url_vars
        r = self.s.get(brands_url)
        response =  loads(r.content)
        return response


###################  
#  CASES METHODS  #
###################


    def cases_list(self):
        url_vars = (self.base_uri)
        cases_url = "%s/cases" % url_vars
        r = self.s.get(cases_url)
        response =  loads(r.content)
        return response
    
    def cases_case_create(self, case):  
        url_vars = (self.base_uri)
        cases_url = "%s/cases" % url_vars
        r = self.s.post(cases_url, data=dumps(case))
        response =  loads(r.content)
        return response









    def brands():
        pass

    def cases():
        pass

    def companies():
        pass

    def customFields():
        pass

    def customers():
        pass

    def eTags():
        pass

    def facebookAccounts():
        pass

    def facebookFeeds():
        pass

    def facebookUsers():
        pass

    def filters():
        pass

    def groups():
        pass

    def inboundMailboxes():
        pass

    def insightsV3():
        pass
    
    def integrationURLs():
        pass

    def jobs():
        pass

    def labels():
        pass

    def macros():
        pass

    def outboundMailboxes():
        pass

    def rules():
        pass

    def siteSettings():
        pass

    def systemMessage():
        pass

    def topics():
        pass

    def twitterAccounts():
        pass

    def twitterUsers():
        pass

    def users():
        pass
