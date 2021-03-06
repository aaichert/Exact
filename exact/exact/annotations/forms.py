from django import forms

from exact.annotations.models import ExportFormat


class ExportFormatCreationForm(forms.ModelForm):
    class Meta:
        model = ExportFormat
        fields = [
            'name',
            'team',
            'annotations_types',
            'public',
            'base_format',
            'image_format',
            'annotation_format',
            'not_in_image_format',
            'vector_format',
            'name_format',
            'min_verifications',
            'image_aggregation',
            'include_blurred',
            'include_concealed',
        ]


class ExportFormatEditForm(forms.ModelForm):
    class Meta:
        model = ExportFormat
        fields = [
            'name',
            'annotations_types',
            'public',
            'base_format',
            'image_format',
            'annotation_format',
            'not_in_image_format',
            'vector_format',
            'name_format',
            'min_verifications',
            'image_aggregation',
            'include_blurred',
            'include_concealed',
        ]
