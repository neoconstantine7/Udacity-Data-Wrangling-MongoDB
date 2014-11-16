# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 12:00:19 2014

@author: changli
"""
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    params["limit"] = 5
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    #results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    #pretty_print(results)

    #artist_id = results["artist"][1]["id"]
    #print "\nARTIST:"
    #pretty_print(results["artist"][1])

    #artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    #releases = artist_data["releases"]
    #print "\nONE RELEASE:"
    #pretty_print(releases[0], indent=2)
    #release_titles = [r["title"] for r in releases]

    #print "\nALL TITLES:"
    #for t in release_titles:
    #    print t

    
    q1 = query_by_name(ARTIST_URL, query_type["simple"], '"First AID KIT"')
    count = q1["count"]
    print count
    pretty_print(q1)

    q2 = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
    begin_area = q2["artists"][0]["begin-area"]["name"]
    print begin_area
    pretty_print(q2)

    q3 = query_by_name(ARTIST_URL, query_type["simple"], "Beatles")
    pretty_print(q3)
    aliases = q3["artists"][0]["aliases"]
    for a in aliases:  #Great example in finding value based on other given value
        if a["locale"] == "es":
            alias = a["name"]
    print "Q3: Spanish alias for Beatles"
    print alias
    pretty_print(q3) 
           
    q4 = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana") 
    disam = q4["artists"][0]["disambiguation"]
    print disam    
    pretty_print(q4)
    
    q5 = query_by_name(ARTIST_URL, query_type["simple"], "One Direction") 
    begin = q5["artists"][0]["life-span"]["begin"]
    print begin    
    pretty_print(q5)

if __name__ == '__main__':
    main()
