from .utils import print_info, print_success

class IntelligenceEngine:
    def __init__(self):
        # Weights for different types of "clues"
        self.weights = {
            "exact_match": 0.5,
            "social_mention": 0.3,
            "leak_coexistence": 0.4,
            "domain_trust": 0.2
        }

    def validate_link(self, source, target, snippets):
        """
        Validate if source (e.g. phone) and target (e.g. email) are truly connected.
        Uses a heuristic scoring (Intelligence Model).
        """
        score = 0

        # Exact match of both in same snippet
        for snippet in snippets:
            if source in snippet and target in snippet:
                score += self.weights["exact_match"]

            # Contextual keywords
            if any(word in snippet.lower() for word in ["owner", "contact", "profile", "account"]):
                score += self.weights["social_mention"]

        # Normalize score
        confidence = min(1.0, score)
        return confidence

    def get_summary(self, results):
        print_info("Running Intelligence Engine for cross-verification...")

        verified_links = []

        # Basic logic to cross-examine results
        # This is a simplified ML-like validation
        if 'phone' in results and 'email' in results:
            p_data = results['phone']
            e_data = results['email']

            # Check if phone's associated emails contain the target email
            if p_data and e_data and e_data['email'] in p_data.get('associated_emails', []):
                verified_links.append(f"Phone {p_data['phone']} -> Email {e_data['email']} (HIGH CONFIDENCE)")

        confidence_score = len(verified_links) * 0.5
        return verified_links, confidence_score
