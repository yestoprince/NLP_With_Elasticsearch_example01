indexMapping =  {
    "properties": {
        "URL": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
        "Description":{
            "type": "text",
        },
        "description_embedding": {
            "properties": {
                "is_truncated": {"type": "boolean"},
                "model_id": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "predicted_value": {
                    "type": "dense_vector",
                    "dims": 384,
                    "index": True,
                    "similarity": "l2_norm",
                },
            }
        },
    }
}