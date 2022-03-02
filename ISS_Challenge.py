#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests,datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
#    print(resp)
    lat= resp['iss_position']['latitude']
    lon=resp['iss_position']['longitude']
    coords_tuple= (lat,lon)
    coords= rg.search(coords_tuple)
    print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {datetime.datetime.fromtimestamp(resp['timestamp'])}\nLon: {resp['iss_position']['longitude']}\nLat: {resp['iss_position']['latitude']}\nCountry/City: {coords[0]['cc']}/{coords[0]['name']}")


if __name__ == "__main__":
    main()
