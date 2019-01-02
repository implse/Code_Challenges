# Write a function to flatten a nested dictionary. Namespace the keys with a period.
#
# For example, given the following dictionary:
#
# {
#     "key": 3,
#     "foo": {
#         "a": 5,
#         "bar": {
#             "baz": 8
#         }
#     }
# }
#
# it should become:
#
# {
#     "key": 3,
#     "foo.a": 5,
#     "foo.bar.baz": 8
# }
#
# You can assume keys do not contain dots in them, i.e. bo clobbering will occur.


def flatten_dict(d):
    def expand(key, value):
        if isinstance(value, dict):
            return [ (key + '.' + k, v) for k, v in flatten_dict(value).items() ]
        else:
            return [ (key, value) ]

    items = [ item for k, v in d.items() for item in expand(k, v) ]

    return dict(items)

# Test

foo_bar = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }

print(flatten_dict(foo_bar))
