from ..models import Blog
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        # read_only_fields = ['title']

    # for validate the form use "validate _ [table field name]"

    # def validate_message(self, value):
    #     query = Blog.objects.filter(message=value)
    #     if self.instance:
    #         query = query.exclude(pk=self.instance.pk)
    #     if query.exists():
    #         raise serializers.ValidationError(
    #             "this message has already been used")
    #     return value

    # def validate_description(self, value):
    #     query = Blog.objects.filter(description=value)
    #     if self.instance:
    #         query = query.exclude(pk=self.instance.pk)
    #     if query.exists():
    #         raise serializers.ValidationError(
    #             "your description must be unique")
    #     return value
