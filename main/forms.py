from django.forms import ModelForm, TextInput, Textarea, URLInput, CheckboxInput

from main.models import Award

class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = [
            "title",
            "issuer",
            "tier",
            "date",
            "description",
            "certificate_url",
            "is_winner",
        ]

        labels = {
            "title": "Nama Penghargaan",
            "issuer": "Instansi Penyelenggara Lomba",
            "tier": "Tingkat Penghargaan",
            "date": "Waktu Pelaksanaan",
            "description": "Deskripsi Penghargaan",
            "certificate_url": "Tautan Sertifikat",
            "is_winner": "Apakah Menang?",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Juara 1 Lomba Tidur",
                    "maxlength": 255,
                }
            ),
            "issuer": TextInput(
                attrs={
                    "placeholder": "Dinas Kehutanan",
                    "maxlength": 255,
                }
            ),
            "tier": TextInput(
                attrs={
                    "placeholder": "Nasional/Internasional",
                    "maxlength": 100,
                }
            ),
            "date": TextInput(
                attrs={
                    "placeholder": "Agustus 2026",
                    "maxlength": 100,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Pencapaianmu",
                    "rows": 3,
                }
            ),
            "certificate_url": URLInput(
                attrs={
                    "placeholder": "https://example.com/certificate.pdf",
                }
            ),
            "is_winner": CheckboxInput(),
        }