
from django.test import TestCase
from .forms import AppealForm
from .models import DMHCDecision


class AppealFormTests(TestCase):

    def test_required_fields_cannot_be_blank(self):
        form = AppealForm(data={
            "treatment_category": "",
            "review_type": "",
            "denial_reason": "",
            "justification": "",
            "supporting_documents": "",
        })

        self.assertFalse(form.is_valid())

        self.assertIn("treatment_category", form.errors)
        self.assertIn("review_type", form.errors)
        self.assertIn("denial_reason", form.errors)
        self.assertIn("justification", form.errors)
        self.assertNotIn("supporting_documents", form.errors)

    def test_denial_reason_character_limit(self):
        form = AppealForm(data={
            "treatment_category": "",
            "review_type": "",
            "denial_reason": "A" * 101,
            "justification": "Fictional medical explanation",
            "supporting_documents": "",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("denial_reason", form.errors)

    def test_invalid_treatment_category(self):
        # Add a valid category so this is a meaningful test.
        DMHCDecision.objects.create(
            reference_id="TEST-INVALID-001",
            report_year=2026,
            treatment_category="Pharmacy",
            review_type="Medical Necessity",
            determination="Upheld Decision of Health Plan"
        )

        form = AppealForm(data={
            "treatment_category": "Not a Real Category",
            "review_type": "Medical Necessity",
            "denial_reason": "Fictional denial",
            "justification": "Fictional medical explanation",
            "supporting_documents": "",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("treatment_category", form.errors)

    def test_valid_treatment_category(self):
        # Create a known category in the test database.
        DMHCDecision.objects.create(
            reference_id="TEST-VALID-001",
            report_year=2026,
            treatment_category="Pharmacy",
            review_type="Medical Necessity",
            determination="Upheld Decision of Health Plan"
        )

        form = AppealForm(data={
            "treatment_category": "Pharmacy",
            "review_type": "Medical Necessity",
            "denial_reason": "Fictional denial",
            "justification": "Fictional medical explanation",
            "supporting_documents": "",
        })

        self.assertTrue(form.is_valid())

    def test_required_fields_cannot_be_blank_with_valid_choices(self):
        # Create valid choices to confirm the other fields are required.
        DMHCDecision.objects.create(
            reference_id="TEST-REQUIRED-001",
            report_year=2026,
            treatment_category="Pharmacy",
            review_type="Medical Necessity",
            determination="Upheld Decision of Health Plan"
        )

        form = AppealForm(data={
            "treatment_category": "Pharmacy",
            "review_type": "Medical Necessity",
            "denial_reason": "",
            "justification": "",
            "supporting_documents": "",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("denial_reason", form.errors)
        self.assertIn("justification", form.errors)
        self.assertNotIn("treatment_category", form.errors)
        self.assertNotIn("review_type", form.errors)


class AppealStatisticsTests(TestCase):

    def test_statistics_filter_by_category_and_review_type(self):
        DMHCDecision.objects.create(
            reference_id="TEST-001",
            report_year=2026,
            treatment_category="Pharmacy",
            review_type="Medical Necessity",
            determination="Upheld Decision of Health Plan"
        )

        DMHCDecision.objects.create(
            reference_id="TEST-002",
            report_year=2026,
            treatment_category="Pharmacy",
            review_type="Medical Necessity",
            determination="Overturned Decision of Health Plan"
        )

        DMHCDecision.objects.create(
            reference_id="TEST-003",
            report_year=2026,
            treatment_category="Pharmacy",
            review_type="Urgent Care",
            determination="Overturned Decision of Health Plan"
        )

        DMHCDecision.objects.create(
            reference_id="TEST-004",
            report_year=2026,
            treatment_category="Surgery",
            review_type="Medical Necessity",
            determination="Overturned Decision of Health Plan"
        )

        response = self.client.post("/", data={
            "treatment_category": "Pharmacy",
            "review_type": "Medical Necessity",
            "denial_reason": "Fictional denial",
            "justification": "Fictional medical explanation",
            "supporting_documents": "",
        })

        self.assertEqual(response.status_code, 200)

        statistics = response.context["statistics"]

        self.assertEqual(statistics["total"], 2)
        self.assertEqual(statistics["upheld"], 1)
        self.assertEqual(statistics["overturned"], 1)
        self.assertEqual(
            statistics["source_ids"],
            ["TEST-001", "TEST-002"]
        )

    def test_statistics_filter_by_year(self):
        # Create matching records from two different years.
        DMHCDecision.objects.create(
            reference_id="TEST-2025",
            report_year=2025,
            treatment_category="Pharmacy",
            review_type="Medical Necessity",
            determination="Upheld Decision of Health Plan"
        )

        DMHCDecision.objects.create(
            reference_id="TEST-2026",
            report_year=2026,
            treatment_category="Pharmacy",
            review_type="Medical Necessity",
            determination="Overturned Decision of Health Plan"
        )

        response = self.client.post("/", data={
            "treatment_category": "Pharmacy",
            "review_type": "Medical Necessity",
            "report_year": "2025",
            "denial_reason": "Fictional denial",
            "justification": "Fictional medical explanation",
            "supporting_documents": "",
        })

        self.assertEqual(response.status_code, 200)

        statistics = response.context["statistics"]

        self.assertEqual(statistics["year"], "2025")
        self.assertEqual(statistics["total"], 1)
        self.assertEqual(statistics["upheld"], 1)
        self.assertEqual(statistics["overturned"], 0)
        self.assertEqual(statistics["source_ids"], ["TEST-2025"])
