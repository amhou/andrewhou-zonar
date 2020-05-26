def unique_languages(countries):
    """
    Return a list of unique languages from a list of countries.

    Input:
    - countries. A JSON list of countries, response from restcoutries.eu.

    Returns:
    - A unique list of languages in the following format:
    [{'iso639_1': 'it', 'iso639_2': 'ita', 'name': 'Italian', 'nativeName': 'Italiano'},...]
    """
    uniq_languages = {}

    for country in countries:
        country_languages = country['languages']

        for lang in country_languages:
            if lang['iso639_2'] not in uniq_languages:
                uniq_languages[lang['iso639_2']] = lang

    return list(uniq_languages.values())
