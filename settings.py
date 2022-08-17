def init():
    global myVars
    myVars = {
        "default_lang"          : "en",
        "base_url"              : "https://linkedart.participatory-archives.ch/",

        "page_size"             : 500,

        "pia_api_uri"           : "https://data.participatory-archives.ch/api/v1/images",

        "a_collection"         : "data/a_collection",
        "b_mapped"             : "data/b_mapped",
        "c_linked_art"         : "data/c_linked_art",


        "digitalobject_template" : "../templates/digital_object_template.jsonnet",
        "humanmadeobject_template" : "../templates/humanmadeobject_template.jsonnet",

        "types": {
            "http://vocab.getty.edu/aat/300215302": {
                "_label": "Digital Image"
            },
            "http://vocab.getty.edu/aat/300025976": {
                "_label": "Collection"
            },
            "http://vocab.getty.edu/aat/300264578": {
                "_label": "Web Page"
            },
            "http://vocab.getty.edu/aat/300055647": {
                "_label": "Width"
            },
            "http://vocab.getty.edu/aat/300379098": {
                "_label": "Height"
            },
            "http://vocab.getty.edu/aat/300379098": {
                "_label": "Centimetres"
            },
            "http://vocab.getty.edu/aat/300379098": {
                "_label": "Display Title"
            },
            "http://vocab.getty.edu/aat/300128343": {
                "_label": "Black and White Negative"
            },
            "http://vocab.getty.edu/aat/300435443": {
                "_label": "Type of Work"
            },
            "http://vocab.getty.edu/aat/300055647": {
                "_label": "Width"
            },
            "http://vocab.getty.edu/aat/300055644": {
                "_label": "Height"
            },
            "http://vocab.getty.edu/aat/300404669": {
                "_label": "Display Title"
            },
            "http://vocab.getty.edu/aat/300164207": {
                "_label": "Carnival"
            },
            "http://vocab.getty.edu/aat/300404670": {
                "_label": "Owner-Assigned Title"
            },
            "http://vocab.getty.edu/aat/300388344": {
                "_label": "German"
            },
            "http://vocab.getty.edu/aat/300417447": {
                "_label": "Creator-Assigned Number"
            },
            "http://vocab.getty.edu/aat/300312355": {
                "_label": "SGV Signature"
            },
            "http://vocab.getty.edu/aat/300404621": {
                "_label": "PIA ID"
            },
            "":{
                "_label": ""
            },
        }

    }
