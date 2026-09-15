from django.test import TestCase, Client


class HealthEndpointTests(TestCase):
    """
    Basic smoke tests — this is what 'Run Tests' in the CI pipeline
    actually executes before the Docker image is built.
    """

    def setUp(self):
        self.client = Client()

    def test_home_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_healthz_returns_healthy(self):
        response = self.client.get("/healthz")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "healthy")

    def test_readyz_returns_ready(self):
        response = self.client.get("/readyz")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ready")
