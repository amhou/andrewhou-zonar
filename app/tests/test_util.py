import json

import util


def test_unique_countries():
    example_countries = [
        {
            "name": "country1",
            "languages": [
                {
                    "iso639_1": "ar",
                    "iso639_2": "ara",
                    "name": "Arabic",
                    "nativeName": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629"
                },
                {
                    "iso639_1": "az",
                    "iso639_2": "aze",
                    "name": "Azerbaijani",
                    "nativeName": "az\u0259rbaycan dili"
                },
                {
                    "iso639_1": "bn",
                    "iso639_2": "ben",
                    "name": "Bengali",
                    "nativeName": "\u09ac\u09be\u0982\u09b2\u09be"
                }
            ]
        },
        {
            "name": "country2",
            "languages": [
                {
                    "iso639_1": "ar",
                    "iso639_2": "ara",
                    "name": "Arabic",
                    "nativeName": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629"
                }
            ]
        }
    ]

    assert util.unique_languages(example_countries) == [
        {
            "iso639_1": "ar",
            "iso639_2": "ara",
            "name": "Arabic",
            "nativeName": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629"
        },
        {
            "iso639_1": "az",
            "iso639_2": "aze",
            "name": "Azerbaijani",
            "nativeName": "az\u0259rbaycan dili"
        },
        {
            "iso639_1": "bn",
            "iso639_2": "ben",
            "name": "Bengali",
            "nativeName": "\u09ac\u09be\u0982\u09b2\u09be"
        }
    ]
