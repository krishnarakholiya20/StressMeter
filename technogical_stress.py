class TechnologicalStress:
    def device_overuse(self, hours_screen):
        return f"{'Excessive' if hours_screen > 6 else 'Normal'} screen time ({hours_screen} hrs)"

    def internet_connectivity(self, speed_mbps):
        return f"{'Slow' if speed_mbps < 10 else 'Good'} internet speed ({speed_mbps} Mbps)"

    def data_privacy_concern(self, concern_level):
        return f"{'High' if concern_level > 7 else 'Low'} privacy concern"

    def software_crash_rate(self, crashes):
        return f"{'Frequent' if crashes > 3 else 'Stable'} crash rate"

    def update_overload(self, updates_per_week):
        return f"{'Overloaded' if updates_per_week > 5 else 'Manageable'} updates"

    def digital_notifications(self, notifications_per_day):
        return f"{'Too many' if notifications_per_day > 50 else 'Normal'} notifications"

    def multitasking_demand(self, tasks):
        return f"{'High' if tasks > 5 else 'Low'} multitasking load"

    def ui_overcomplexity(self, ui_score):
        return f"{'Complex' if ui_score > 7 else 'Simple'} UI"

    def dependency_on_tech(self, dependency_score):
        return f"{'High' if dependency_score > 8 else 'Balanced'} tech dependency"

    def digital_fatigue(self, fatigue_level):
        return f"{'Fatigued' if fatigue_level > 6 else 'Refreshed'} digital state"
