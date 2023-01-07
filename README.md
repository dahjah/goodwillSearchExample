# Goodwill Search Example in Python

Simple Python function showing how to use the undocumented Goodwill API to search for items. This code is intended for educational purposes only, and thus is simplified.

## Quickstart

Goodwill uses an internal undocumented API to power its advanced search feature. There are many options that can be passed, but at a minimum, the following needs to be present:

```
{
  "searchText": "",
  "selectedGroup": "Keyword",
  "lowPrice": "0",
  "highPrice": "999999",
  "searchBuyNowOnly": "",
}
```

This will result in a query as if the user had entered no items in the search and wanted to look at everything.

That is not very useful, so one could enter a search keyword, like "Kitchenaid mixer", to search for any items that contain the word "Kitchenaid" and "mixer".

```
from goodwill import search_goodwill


search_config = {
  "searchText": "Kitchenaid mixer",
  "selectedGroup": "Keyword",
  "lowPrice": "0",
  "highPrice": "999999",
  "searchBuyNowOnly": "",
}

resp = search_goodwill(search_config)
print(resp)
```

The way Goodwill search works, however, means that it will only search for items containing ALL searchText. This works great if one wanted to narrow down their search to only items that contained each word in the search terms. If one wanted to search for items containing any keyword, but not necessarily all of them, they could use the `addtl_keywords` flag in search_goodwill to handle that for them. For example, searching for Kitchenaids, that contain the colors `red`, `green`, or `brown` would look like this:

```
search_config = {
  "searchText": "Kitchenaid",
  "selectedGroup": "Keyword",
  "lowPrice": "0",
  "highPrice": "999999",
  "searchBuyNowOnly": "",
}

# Retrieve any item that contains the word "Kitchenaid" as well as one or more of "red", "green", or "brown".
resp = search_goodwill(search_config, addtl_keywords=["red", "green", "brown")
print(resp)
```

Lastly, there can be a lot of results, so if one wanted to limit those, they can be limited by including the `max_items` param. Also, the results can be limited by pages using the `max_pages` param

```
# Retrieve the first 5 items
search_goodwill(search_config, addtl_keywords=["red", "green", "brown", max_items=5)

# Retrieve the first 2 pages
search_goodwill(search_config, addtl_keywords=["red", "green", "brown", max_pages=2)
```

## All The Search Configuration Options

While the examples above only work with the minimum search configuration json, goodwill provides the following config options that can be used. One or more can 
be added to `search_config` to extend the search filtering.

```
{
  "isSize": False,
  "isWeddingCatagory": "false",
  "isMultipleCategoryIds": False,
  "isFromHeaderMenuTab": False,
  "layout": "",
  "isFromHomePage": False,
  "searchText": "keyword1 keyword2 keyword3",
  "selectedGroup": "Keyword",
  "selectedCategoryIds": "",
  "selectedSellerIds": "",
  "lowPrice": "0",
  "highPrice": "999999",
  "searchBuyNowOnly": "",
  "searchPickupOnly": "false",
  "searchNoPickupOnly": "false",
  "searchOneCentShippingOnly": "false",
  "searchDescriptions": "true",
  "searchClosedAuctions": "false",
  "closedAuctionEndingDate": "1/6/2023",
  "closedAuctionDaysBack": "7",
  "searchCanadaShipping": "false",
  "searchInternationalShippingOnly": "false",
  "sortColumn": "1",
  "page": 1,
  "pageSize": "40",
  "sortDescending": "false",
  "savedSearchId": 0,
  "useBuyerPrefs": "true",
  "searchUSOnlyShipping": "true",
  "categoryLevelNo": "1",
  "categoryLevel": 1,
  "categoryId": 0,
  "partNumber": "",
  "catIds": ""
}
```
