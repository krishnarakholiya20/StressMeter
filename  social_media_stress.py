class SocialMediaStress:
    def screen_time(self, hours):
        return f"{'Excessive' if hours > 4 else 'Healthy'} social media time"

    def comparison_stress(self, comparison_level):
        return f"{'High' if comparison_level > 7 else 'Low'} comparison stress"

    def cyberbullying_incidents(self, count):
        return f"{'Yes' if count > 0 else 'None'} cyberbullying incidents"

    def validation_stress(self, likes_comments):
        return f"{'High' if likes_comments < 10 else 'Low'} validation stress"

    def fomo_score(self, fomo_level):
        return f"{'High' if fomo_level > 6 else 'Low'} FOMO"

    def fake_news_exposure(self, exposure_count):
        return f"{'High' if exposure_count > 5 else 'Low'} fake news exposure"

    def content_overload(self, content_volume):
        return f"{'Overloaded' if content_volume > 100 else 'Controlled'} content volume"

    def privacy_anxiety(self, anxiety_level):
        return f"{'Anxious' if anxiety_level > 6 else 'Calm'} privacy feeling"

    def trolling_experience(self, troll_level):
        return f"{'Trolled' if troll_level > 2 else 'Safe'} trolling experience"

    def social_pressure(self, pressure_score):
        return f"{'High' if pressure_score > 7 else 'Low'} social pressure"
