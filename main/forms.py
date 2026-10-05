from django.forms import ModelForm, TextInput, Textarea, URLInput, CheckboxInput, DateInput, DateTimeField, Select
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from main.models import Award, Experience

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
        
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama penghargaan tidak boleh hanya berisi tag HTML.")
        return title

    def clean_issuer(self):
        return strip_tags(self.cleaned_data["issuer"]).strip()

    def clean_tier(self):
        return strip_tags(self.cleaned_data["tier"]).strip()

    def clean_date(self):
        return strip_tags(self.cleaned_data["date"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

class ExperienceForm(ModelForm):
    ended_at = DateTimeField(
        required=False,
        label="Bulan dan Tahun Berakhir (Kosongkan jika masih berlangsung)",
        widget=DateInput(format="%Y-%m", attrs={"type": "month"}),
        input_formats=["%Y-%m"],
    )

    class Meta:
        model = Experience
        fields = [
            "title",
            "category",
            "description",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Judul Posisi atau Peran",
            "category": "Kategori Pengalaman",
            "description": "Deskripsi Tanggung Jawab dan Kontribusi",
            "thumbnail": "Tautan Dokumentasi atau Media (Opsional)",
            "ended_at": "Bulan dan Tahun Berakhir",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Staff Editorial Marketing COMPFEST 18",
                    "maxlength": 255,
                }
            ),
            "category": Select(),
            "description": Textarea(
                attrs={
                    "placeholder": "Jelaskan tanggung jawab utama dan kontribusi Anda dalam kegiatan tersebut",
                    "rows": 4,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://example.com/thumbnail.png",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Judul pengalaman tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"]).strip()
        if not description:
            raise ValidationError("Deskripsi pengalaman tidak boleh hanya berisi tag HTML.")
        return description