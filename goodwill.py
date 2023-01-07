import requests


def search_goodwill(search_config, addtl_keywords=[],
                    max_pages=-1, max_items=-1):
    """This function will search goodwill using a provided search config.
    If also provided, it will also limit results to any containing one or more
    of the addtl_keywords in the title.

    Args:
        search_config (dict): search configuration to use for query
        addtl_keywords (list, optional): list of keywords to filter results by.
            Results containing one or more of these will be returned.
            Defaults to [].
        max_pages (int, optional): maximum number of pages to process.
            -1 indicates all. Defaults to -1.
        max_items (int, optional): maximum number of items to return.
            -1 indicates all. Defaults to -1.

    Returns:
        list: list of results matching query, and optionally provided keywords.
    """

    url = 'https://buyerapi.shopgoodwill.com/api/Search/ItemListing'
    # Since goodwill limits the results to 40 per request, we need to make
    # multiple requests to page through the entirety of the results
    results = []
    total_items = 1
    items_processed = 0
    # In case user does not provided a page number in config, set it to 1
    search_config['page'] = search_config.get('page', 1)
    while items_processed < total_items:
        resp = requests.post(url, json=search_config).json()
        total_items = resp['searchResults']['itemCount']
        items_processed += len(resp['searchResults']['items'])
        # If additional keywords are provided, then we want to only keep the
        # records which contain one or more of the additional keywords.
        # in a perfect world, goodwill would allow us to do this in the search
        # itself, but since they only search for things containing all the
        # keywords, we have to post process if we want records containing any
        # of the keywords.
        if addtl_keywords:
            for item in resp['searchResults']['items']:
                if any(kw in item['title'] for kw in addtl_keywords):
                    results.append(item)
        # if no additional keywords are given, then we can immediately store
        # all results and move on to the next page.
        else:
            results.extend(resp['searchResults']['items'])

        # If max_pages is reached (-1 meaning get all pages), or max_items
        # is reached, then we can stop the search. Because max_items may
        # or may not be divisible by the size of the pages, we can slice
        # the resulting list to be the proper length.
        if max_pages > -1 and search_config['page'] >= max_pages \
                or max_items > -1 and len(results) >= max_items:
            results = results[:max_items] if max_items > -1 else results
            break
        search_config['page'] += 1
    return results
