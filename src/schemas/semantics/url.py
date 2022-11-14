GET_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "has_data": {
      "type": "boolean"
    },
    "data": {
      "type": "object",
      "properties": {
        "items": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "entity": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "url": {
                      "type": "string"
                    },
                    "cdate": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "url",
                    "cdate"
                  ]
                },
                "category": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "name"
                  ]
                },
                "properties": {
                  "type": "object",
                  "properties": {
                    "stat_url": {
                      "type": "integer"
                    },
                    "analitica_isset": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "stat_url",
                    "analitica_isset"
                  ]
                },
                "summary": {
                  "type": "object",
                  "properties": {
                    "queries_count": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "queries_count"
                  ]
                },
                "frequency": {
                  "type": "object",
                  "properties": {
                    "ws1": {
                      "type": "integer"
                    },
                    "ws2": {
                      "type": "integer"
                    },
                    "ws3": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "ws1",
                    "ws2",
                    "ws3"
                  ]
                },
                "top": {
                  "type": "object",
                  "properties": {
                    "top3": {
                      "type": "number"
                    },
                    "top5": {
                      "type": "number"
                    },
                    "top10": {
                      "type": "number"
                    },
                    "top30": {
                      "type": "number"
                    },
                    "top100": {
                      "type": "number"
                    },
                    "position_top30": {
                      "type": "number"
                    },
                    "position": {
                      "type": "number"
                    }
                  },
                  "required": [
                    "top3",
                    "top5",
                    "top10",
                    "top30",
                    "top100",
                    "position_top30",
                    "position"
                  ]
                },
                "frequency_percent": {
                  "type": "object",
                  "properties": {
                    "ws1_top10_percent": {
                      "type": "integer"
                    },
                    "ws2_top10_percent": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "ws1_top10_percent",
                    "ws2_top10_percent"
                  ]
                },
                "potential_traffic": {
                  "type": "object",
                  "properties": {
                    "traffic": {
                      "type": "number"
                    },
                    "traffic_percent": {
                      "type": "number"
                    }
                  },
                  "required": [
                    "traffic",
                    "traffic_percent"
                  ]
                },
                "traffic": {
                  "type": "object",
                  "properties": {
                    "summary": {
                      "type": "null"
                    },
                    "yandex_sum": {
                      "type": "null"
                    },
                    "google_sum": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "summary",
                    "yandex_sum",
                    "google_sum"
                  ]
                },
                "transactions": {
                  "type": "object",
                  "properties": {
                    "transactions": {
                      "type": "null"
                    },
                    "transaction_revenue": {
                      "type": "null"
                    },
                    "conversion": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "transactions",
                    "transaction_revenue",
                    "conversion"
                  ]
                },
                "worth": {
                  "type": "object",
                  "properties": {
                    "worth": {
                      "type": "null"
                    },
                    "worth_percent": {
                      "type": "null"
                    },
                    "worth_max": {
                      "type": "null"
                    },
                    "worth_reserve": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "worth",
                    "worth_percent",
                    "worth_max",
                    "worth_reserve"
                  ]
                },
                "important": {
                  "type": "object",
                  "properties": {
                    "manual": {
                      "type": "integer"
                    },
                    "auto": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "manual",
                    "auto"
                  ]
                }
              },
              "required": [
                "entity",
                "category",
                "properties",
                "summary",
                "frequency",
                "top",
                "frequency_percent",
                "potential_traffic",
                "traffic",
                "transactions",
                "worth",
                "important"
              ]
            }
          ]
        },
        "config": {
          "type": "object",
          "properties": {
            "labels": {
              "type": "object",
              "properties": {
                "frequency": {
                  "type": "object",
                  "properties": {
                    "ws1": {
                      "type": "string"
                    },
                    "ws2": {
                      "type": "string"
                    },
                    "ws3": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "ws1",
                    "ws2",
                    "ws3"
                  ]
                }
              },
              "required": [
                "frequency"
              ]
            }
          },
          "required": [
            "labels"
          ]
        },
        "total": {
          "type": "integer"
        },
        "offset": {
          "type": "integer"
        },
        "has_more": {
          "type": "boolean"
        },
        "per_page": {
          "type": "integer"
        }
      },
      "required": [
        "items",
        "config",
        "total",
        "offset",
        "has_more",
        "per_page"
      ]
    },
    "version": {
      "type": "null"
    },
    "status": {
      "type": "integer"
    },
    "error": {
      "type": "integer"
    },
    "error_messages": {
      "type": "array",
      "items": {}
    },
    "response_time": {
      "type": "number"
    },
    "server_timestamp": {
      "type": "string"
    },
    "server_unixtimestamp": {
      "type": "integer"
    },
    "meta": {
      "type": "object",
      "properties": {
        "features": {
          "type": "object",
          "properties": {
            "semantics_queries_less_tables": {
              "type": "boolean"
            },
            "west_show_cpc_cmp_data": {
              "type": "boolean"
            },
            "semantics_new_indexation": {
              "type": "boolean"
            },
            "project__ru": {
              "type": "boolean"
            },
            "project__com": {
              "type": "boolean"
            },
            "semantics_worth": {
              "type": "boolean"
            },
            "semantics_queries_old_tables": {
              "type": "boolean"
            }
          },
          "required": [
            "semantics_queries_less_tables",
            "west_show_cpc_cmp_data",
            "semantics_new_indexation",
            "project__ru",
            "project__com",
            "semantics_worth",
            "semantics_queries_old_tables"
          ]
        }
      },
      "required": [
        "features"
      ]
    }
  },
  "required": [
    "has_data",
    "data",
    "version",
    "status",
    "error",
    "error_messages",
    "response_time",
    "server_timestamp",
    "server_unixtimestamp",
    "meta"
  ]
}
GET_SCHEMA_PERIOD = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "has_data": {
      "type": "boolean"
    },
    "data": {
      "type": "object",
      "properties": {
        "items": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "entity": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "url": {
                      "type": "string"
                    },
                    "cdate": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "url",
                    "cdate"
                  ]
                },
                "category": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "name"
                  ]
                },
                "properties": {
                  "type": "object",
                  "properties": {
                    "stat_url": {
                      "type": "integer"
                    },
                    "analitica_isset": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "stat_url",
                    "analitica_isset"
                  ]
                },
                "summary": {
                  "type": "object",
                  "properties": {
                    "queries_count": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "queries_count"
                  ]
                },
                "frequency": {
                  "type": "object",
                  "properties": {
                    "ws1": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "integer"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "integer"
                            },
                            "percent": {
                              "type": "number"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    },
                    "ws2": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "integer"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "integer"
                            },
                            "percent": {
                              "type": "number"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    },
                    "ws3": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "integer"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "integer"
                            },
                            "percent": {
                              "type": "number"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    }
                  },
                  "required": [
                    "ws1",
                    "ws2",
                    "ws3"
                  ]
                },
                "top": {
                  "type": "object",
                  "properties": {
                    "top3": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "number"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "number"
                            },
                            "percent": {
                              "type": "integer"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    },
                    "top5": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "number"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "number"
                            },
                            "percent": {
                              "type": "integer"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    },
                    "top10": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "number"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "number"
                            },
                            "percent": {
                              "type": "integer"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    },
                    "top30": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "number"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "number"
                            },
                            "percent": {
                              "type": "integer"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    },
                    "top100": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "number"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "number"
                            },
                            "percent": {
                              "type": "integer"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    },
                    "position_top30": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "number"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "number"
                            },
                            "percent": {
                              "type": "number"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    },
                    "position": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "number"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "number"
                            },
                            "percent": {
                              "type": "number"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    }
                  },
                  "required": [
                    "top3",
                    "top5",
                    "top10",
                    "top30",
                    "top100",
                    "position_top30",
                    "position"
                  ]
                },
                "frequency_percent": {
                  "type": "object",
                  "properties": {
                    "ws1": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "integer"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "integer"
                            },
                            "percent": {
                              "type": "integer"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    },
                    "ws2": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "integer"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "integer"
                            },
                            "percent": {
                              "type": "integer"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    }
                  },
                  "required": [
                    "ws1",
                    "ws2"
                  ]
                },
                "potential_traffic": {
                  "type": "object",
                  "properties": {
                    "traffic": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "number"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "number"
                            },
                            "percent": {
                              "type": "integer"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    },
                    "traffic_percent": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "number"
                            },
                            "previous": {
                              "type": "integer"
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "current",
                            "previous",
                            "type"
                          ]
                        },
                        "diff": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "type": "number"
                            },
                            "percent": {
                              "type": "integer"
                            },
                            "direction": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "value",
                            "percent",
                            "direction"
                          ]
                        }
                      },
                      "required": [
                        "values",
                        "diff"
                      ]
                    }
                  },
                  "required": [
                    "traffic",
                    "traffic_percent"
                  ]
                },
                "traffic": {
                  "type": "object",
                  "properties": {
                    "summary": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "current"
                          ]
                        }
                      },
                      "required": [
                        "values"
                      ]
                    },
                    "yandex_sum": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "current"
                          ]
                        }
                      },
                      "required": [
                        "values"
                      ]
                    },
                    "google_sum": {
                      "type": "object",
                      "properties": {
                        "values": {
                          "type": "object",
                          "properties": {
                            "current": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "current"
                          ]
                        }
                      },
                      "required": [
                        "values"
                      ]
                    }
                  },
                  "required": [
                    "summary",
                    "yandex_sum",
                    "google_sum"
                  ]
                },
                "transactions": {
                  "type": "object",
                  "properties": {
                    "transactions": {
                      "type": "null"
                    },
                    "transaction_revenue": {
                      "type": "null"
                    },
                    "conversion": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "transactions",
                    "transaction_revenue",
                    "conversion"
                  ]
                },
                "worth": {
                  "type": "object",
                  "properties": {
                    "worth": {
                      "type": "null"
                    },
                    "worth_prc": {
                      "type": "null"
                    },
                    "worth_max": {
                      "type": "null"
                    },
                    "worth_reserve": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "worth",
                    "worth_prc",
                    "worth_max",
                    "worth_reserve"
                  ]
                },
                "url_not_equal": {
                  "type": "object",
                  "properties": {
                    "analytic_yandex_url_not_equal": {
                      "type": "null"
                    },
                    "analytic_google_url_not_equal": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "analytic_yandex_url_not_equal",
                    "analytic_google_url_not_equal"
                  ]
                },
                "important": {
                  "type": "object",
                  "properties": {
                    "manual": {
                      "type": "integer"
                    },
                    "auto": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "manual",
                    "auto"
                  ]
                }
              },
              "required": [
                "entity",
                "category",
                "properties",
                "summary",
                "frequency",
                "top",
                "frequency_percent",
                "potential_traffic",
                "traffic",
                "transactions",
                "worth",
                "url_not_equal",
                "important"
              ]
            }
          ]
        },
        "config": {
          "type": "object",
          "properties": {
            "labels": {
              "type": "object",
              "properties": {
                "frequency": {
                  "type": "object",
                  "properties": {
                    "ws1": {
                      "type": "string"
                    },
                    "ws2": {
                      "type": "string"
                    },
                    "ws3": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "ws1",
                    "ws2",
                    "ws3"
                  ]
                }
              },
              "required": [
                "frequency"
              ]
            }
          },
          "required": [
            "labels"
          ]
        },
        "total": {
          "type": "integer"
        },
        "offset": {
          "type": "integer"
        },
        "has_more": {
          "type": "boolean"
        },
        "per_page": {
          "type": "integer"
        }
      },
      "required": [
        "items",
        "config",
        "total",
        "offset",
        "has_more",
        "per_page"
      ]
    },
    "version": {
      "type": "null"
    },
    "status": {
      "type": "integer"
    },
    "error": {
      "type": "integer"
    },
    "error_messages": {
      "type": "array",
      "items": {}
    },
    "response_time": {
      "type": "number"
    },
    "server_timestamp": {
      "type": "string"
    },
    "server_unixtimestamp": {
      "type": "integer"
    },
    "meta": {
      "type": "object",
      "properties": {
        "features": {
          "type": "object",
          "properties": {
            "semantics_queries_less_tables": {
              "type": "boolean"
            },
            "west_show_cpc_cmp_data": {
              "type": "boolean"
            },
            "semantics_new_indexation": {
              "type": "boolean"
            },
            "project__ru": {
              "type": "boolean"
            },
            "project__com": {
              "type": "boolean"
            },
            "semantics_worth": {
              "type": "boolean"
            },
            "semantics_queries_old_tables": {
              "type": "boolean"
            }
          },
          "required": [
            "semantics_queries_less_tables",
            "west_show_cpc_cmp_data",
            "semantics_new_indexation",
            "project__ru",
            "project__com",
            "semantics_worth",
            "semantics_queries_old_tables"
          ]
        }
      },
      "required": [
        "features"
      ]
    }
  },
  "required": [
    "has_data",
    "data",
    "version",
    "status",
    "error",
    "error_messages",
    "response_time",
    "server_timestamp",
    "server_unixtimestamp",
    "meta"
  ]
}