from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Award


class PortofolioTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen Kalkulus 1",
            description="Membantu mahasiswa memahami penggunaan dan implementasi dari kalkulus, terutama turunan, limit, dan integral.",
            category="part-time",
        )
        self.award = Award.objects.create(
            title="Infinitics 8 Math Modelling",
            issuer="HMPSM Universitas Pelita Harapan",
            tier="1st Winner",
            date="November 2024",
            description="Won a national-level mathematical modeling competition.",
            is_winner=True,
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_awards")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen Kalkulus 1")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

    def test_awards_url_is_accessible_and_uses_correct_template(self):
        response = self.client.get(reverse("main:show_awards"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "awards.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_awards")}"')

    def test_awards_model_representation(self):
        self.assertEqual(str(self.award), "Infinitics 8 Math Modelling - HMPSM Universitas Pelita Harapan")
        self.assertTrue(self.award.is_winner)

    def test_awards_page_renders_data_when_present(self):
        response = self.client.get(reverse("main:show_awards"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.award.title)
        self.assertContains(response, self.award.issuer)
        self.assertContains(response, self.award.tier)
        self.assertContains(response, self.award.date)
        self.assertContains(response, self.award.description)
        self.assertContains(response, "badge-gold")
        self.assertContains(response, "highlight-winner")

    def test_empty_awards_page(self):
        Award.objects.all().delete()
        response = self.client.get(reverse("main:show_awards"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada penghargaan atau prestasi yang ditambahkan.")