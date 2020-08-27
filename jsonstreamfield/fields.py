import json

from wagtail.core.blocks import StreamValue
from wagtail.core.fields import StreamField


class JSONStreamField(StreamField):
    def get_internal_type(self):
        return 'JSONField'

    def to_python(self, value):
        try:
            return super().to_python(value)
        except TypeError:
            if not [isinstance(item, dict) for item in value]:
                raise

        return self.stream_block.to_python(value)
