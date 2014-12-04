#!/usr/bin/env python2
from requests import session
from json import loads, dumps

class DeskCRM(object):
    def __init__(self, user, secret):
        '''Init with Desk user & password. Only basic auth atm.'''
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
        '''return list of articles'''
        url_vars = (self.base_uri)
        articles_url = "%s/articles" % url_vars
        print
        r = self.s.get(articles_url)
        response =  loads(r.content)
        return response

    def articles_show(self, article_id):
        '''show a single article'''
        url_vars = (self.base_uri, article_id)
        articles_url = "%s/articles/%s" % url_vars
        r = self.s.get(articles_url)
        response =  loads(r.content)
        return response

    def articles_create(self, article):
        '''create article'''
        url_vars = (self.base_uri)
        articles_url = "%s/articles" % url_vars
        r = self.s.post(articles_url, data=loads(article))
        response =  loads(r.content)
        return response

    def articles_update(self, article_id, article):
        '''update article'''
        url_vars = (self.base_uri, article_id)
        articles_url = "%s/articles/%s" % url_vars
        r = self.s.patch(articles_url, data=loads(article))
        response =  loads(r.content)
        return response

    def articles_delete(self, article_id):
        '''delete article'''
        url_vars = (self.base_uri, article_id)
        articles_url = "%s/articles/%s" % url_vars
        r = self.s.delete(articles_url)
        response =  loads(r.content)
        return response

    def articles_search(self, query):
        '''search articles'''
        articles_url = "%s/arcticles/search?" % self.base_uri
        for key, value in query.iteritems():    
            articles_url = "%s%s=%s&" % (articles_url, key, value)
        r = self.s.get(articles_url)
        response =  loads(r.content)
        return response

    def articles_list_attachments(self, article_id):
        '''list attachments for article'''
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

    def cases_list(self, query=None):
        url_vars = (self.base_uri)
        if query != None:
            cases_url = "%s/cases?" % url_vars
            for key, value in query.iteritems():
                cases_url = "%s%s=%s&" % (cases_url, key, value)
            cases_url = cases_url[0:-1]
        else:
            cases_url = "%s/cases" % url_vars
        r = self.s.get(cases_url)
        response =  loads(r.content)
        return response

    def cases_search(self, query):
        cases_url = "%s/cases/search?" % self.base_uri
        for key, value in query.iteritems():    
            cases_url = "%s%s=%s&" % (cases_url, key, value)
        cases_url = cases_url[0:-1]
        r = self.s.get(cases_url)
        response =  loads(r.content)
        return response

    def cases_show(self, case_id):
        url_vars = (self.base_uri, case_id)
        cases_url = "%s/cases/%s" % url_vars
        r = self.s.get(cases_url)
        response =  loads(r.content)
        return response

    def cases_case_create(self, case):  
        url_vars = (self.base_uri)
        cases_url = "%s/cases" % url_vars
        r = self.s.post(cases_url, data=dumps(case))
        response =  loads(r.content)
        return response

    def cases_case_update(self, case, case_id):  
        url_vars = (self.base_uri, case_id)
        cases_url = "%s/cases/%s" % url_vars
        r = self.s.patch(cases_url, data=dumps(case))
        response =  loads(r.content)
        return response

    def cases_case_delete(self, case, case_id):  
        url_vars = (self.base_uri, case_id)
        cases_url = "%s/cases/%s" % url_vars
        r = self.s.delete(cases_url, data=dumps(case))
        response =  loads(r.content)
        return response

    def cases_case_forward(self, data, case_id):  
        url_vars = (self.base_uri, case_id)
        cases_url = "%s/cases/%s/forward" % url_vars
        r = self.s.post(cases_url, data=dumps(data))
        response =  loads(r.content)
        return response

#####################
# COMPANIES METHODS #
#####################

    def companies_list(self):
        url_vars = (self.base_uri)
        companies_url = "%s/companies" % url_vars
        r = self.s.get(companies_url)
        response =  loads(r.content)
        return response

    def companies_show(self, company_id):
        url_vars = (self.base_uri, company_id)
        companies_url = "%s/companies/%s" % url_vars
        r = self.s.get(companies_url)
        response =  loads(r.content)
        return response

    def companies_create(self, company):
        url_vars = (self.base_uri)
        companies_url = "%s/companies" % url_vars
        r = self.s.post(companies_url, data=dumps(company))
        response =  loads(r.content)
        return response

    def companies_search(self, query):
        '''Provide a query object. eg: {"q":crm_id}''' 
        companies_url = "%s/companies/search" % self.base_uri
        r = self.s.get(companies_url, data=dumps(query))
        response =  loads(r.content)
        return response

########################
# customFields methods #
########################

    def customFields(self):
        url_vars = (self.base_uri)
        customFields_url = "%s/custom_fields" % url_vars
        r = self.s.get(customFields_url)
        response =  loads(r.content)
        return response
 
#####################  
# CUSTOMERS METHODS #
#####################

    def customers_list(self):
        url_vars = (self.base_uri)
        customers_url = "%s/customers" % url_vars
        r = self.s.get(customers_url)
        response =  loads(r.content)
        return response

    def customers_show(self, customer_id):
        url_vars = (self.base_uri, customer_id)
        customers_url = "%s/customers/%s" % url_vars
        r = self.s.get(customers_url)
        response =  loads(r.content)
        return response

    def customers_create(self, customer):
        url_vars = (self.base_uri)
        customers_url = "%s/customers" % url_vars
        r = self.s.post(customers_url, data=dumps(customer))
        response =  loads(r.content)
        return response

    def customers_search(self, query):
        '''Provide a query object. eg: {"q":crm_id}''' 
        customers_url = "%s/customers/search?" % self.base_uri
        for key, value in query.iteritems():    
            customers_url = "%s%s=%s&" % (customers_url, key, value)
        customers_url = customers_url[0:-1]
        r = self.s.get(customers_url)
        response =  loads(r.content)
        return response

    def customers_list_cases(self, customer_id):
        url_vars = (self.base_uri, customer_id)
        customers_url = "%s/customers/%s/cases" % url_vars
        r = self.s.get(customers_url)
        response =  loads(r.content)
        return response

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


class CRMTools(DeskCRM):
    def transfer_record(self, doc):
        company = {}
        customer = {}

        #get vars from lead
        crm_id = doc["id"]
        company_name = doc["business"]
        tel_no = doc["customer_phone"]
        customer_name = doc["customer_name"]
        external_url = doc["external"]
        internal_url = doc["internal"]
        email = doc["email"]
        crm_url = "http://reports-bonline.appspot.com/sites/search?query=%s" % crm_id
        status = doc["status"]
        
        #build company object
        company["name"] =  company_name
        if len(external_url) > 4:
            company["domains"] = [external_url]    
        company["custom_fields"] = {}
        company["custom_fields"]["crm_id"] = crm_id
        company["custom_fields"]["crm_url"] = crm_url
        company["custom_fields"]["internal_url"] = internal_url
        
        # Create company in Desk; get Desk URL
        company_create =  self.companies_create(company)
        company_url = company_create["_links"]["self"]["href"]
   
        #build customer object
        #customer["emails"] = [email]
        try:
            first_name = customer_name.split(" ")[0]
            last_name = customer_name.split(" ")[-1]
        except:
            first_name = customer_name
            last_name = "na"
        
        customer["first_name"] = first_name
        customer["last_name"] = last_name
        customer["custom_fields"] = {}
        customer["custom_fields"]["crm_id"] = crm_id
        customer["custom_fields"]["crm_url"] = crm_url
        customer["custom_fields"]["internal_url"] = internal_url
        customer["_links"] = {}
        customer["_links"]["company"] = {}
        customer["_links"]["company"]["href"] = company_url
        customer["_links"]["company"]["class"] = "company"
        customer_create =  self.customers_create(customer)
        customer["customer_url"] = customer_create["_links"]["self"]["href"]
        
        #build transfer obejct 
        transfer_object = {"company":company, "customer":customer}
        return transfer_object

    def convert_crm_id(self, crm_id):
        desk_id = None
        customer_query = self.customers_search({"custom_crm_id": crm_id })
        if len(customer_query["_embedded"]["entries"]) >= 1: 
            desk_id = str(customer_query["_embedded"]["entries"][0]["id"])
        return desk_id

    def crm_get_cases(self, crm_id):
        desk_id = self.convert_crm_id(crm_id)
        cases = self.customers_list_cases(desk_id)
        return cases