from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience

from django.utils.html import strip_tags
from rest_framework import serializers
from main.models import Experience, Award

class ExperienceSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source="get_category_display", read_only=True)
    is_ongoing = serializers.BooleanField(read_only=True)
    ended_at = serializers.DateTimeField(
        required=False,
        allow_null=True,
        input_formats=["%Y-%m", "%Y-%m-%d", "iso-8601"],
    )
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id",
            "title",
            "category",
            "category_display",
            "description",
            "thumbnail",
            "started_at",
            "ended_at",
            "is_ongoing",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = ["id", "started_at"]

    def to_internal_value(self, data):
        # Menangani nilai string kosong dari form agar sesuai dengan field URL & DateTime
        if hasattr(data, "copy"):
            data = data.copy()
        else:
            data = dict(data)
        if data.get("ended_at") == "":
            data["ended_at"] = None
        if data.get("thumbnail") == "":
            data["thumbnail"] = None
        return super().to_internal_value(data)

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Description cannot be empty.")
        return value

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())

class AwardSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Award
        fields = [
            "id",
            "title",
            "issuer",
            "tier",
            "date",
            "description",
            "certificate_url",
            "is_winner",
            "created_at",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = ["id", "created_at"]

    def to_internal_value(self, data):
        if hasattr(data, "copy"):
            data = data.copy()
        else:
            data = dict(data)

        if data.get("certificate_url") == "":
            data["certificate_url"] = None

        if "is_winner" in data:
            if isinstance(data["is_winner"], str):
                data["is_winner"] = data["is_winner"].lower() in ("true", "1", "yes", "on")

        return super().to_internal_value(data)

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_issuer(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Issuer cannot be empty.")
        return value

    def validate_tier(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Tier cannot be empty.")
        return value

    def validate_date(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Date cannot be empty.")
        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Description cannot be empty.")
        return value

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())