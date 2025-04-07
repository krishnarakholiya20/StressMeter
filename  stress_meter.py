from .system_stress import SystemStress
from .environmental_stress import EnvironmentalStress
from .technological_stress import TechnologicalStress
from .academic_stress import AcademicStress
from .social_media_stress import SocialMediaStress

class StressMeter:
    def __init__(self):
        self.system_stress = SystemStress()
        self.environmental_stress = EnvironmentalStress()
        self.technological_stress = TechnologicalStress()
        self.academic_stress = AcademicStress()
        self.social_media_stress = SocialMediaStress()
