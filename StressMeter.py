class StressMeter:  # main class
    def __init__(self):
        self.physical_stress = PhysicalStress()
        self.mental_stress = MentalStress()
        self.emotional_stress = EmotionalStress()
        self.behavior_stress = BehaviorStress()
        self.lifecycle_stress = LifecycleStress()

    class PhysicalStress:
        def heart_rate(self, heart_rate):
            #Analyzes heart rate for stress indications.
            self.heart_rate = heart_rate  # Store heart rate
            if heart_rate > 100:
                return "High heart rate, possible physical stress."
            else:
                return "Normal heart rate."

        def blood_pressure(self, systolic, diastolic):
            #Analyzes blood pressure for stress indications."""
            self.systolic = systolic  # Store systolic
            self.diastolic = diastolic  # Store diastolic
            if systolic > 130 or diastolic > 80:
                return "High blood pressure, possible physical stress."
            else:
                return "Normal blood pressure."

        def muscle_tension(self, tension_level):
            """Analyzes muscle tension levels."""
            self.tension_level = tension_level  # Store tension level
            if tension_level > 7:
                return "High muscle tension level, possible physical stress"
            else:
                return "Normal muscle tension."

        def sleep_quality(self, sleep_hours):
            """Assesses sleep quality based on hours of sleep."""
            self.sleep_hours = sleep_hours  # Store sleep hours
            if sleep_hours < 6:
                return "Insufficient sleep, possible physical stress."
            else:
                return "Adequate sleep."

        def check_hydration(self, water_intake):
            """Checks hydration levels based on water intake."""
            self.water_intake = water_intake  # Store water intake
            if water_intake < 2000:
                return "Low hydration, possible physical stress."
            else:
                return "Adequate sleep."  # Corrected the return message

        def breathing_rate(self, breaths_per_minute):
            """Analysis breathing rate for stress"""
            self.breaths_per_minute = breaths_per_minute
            if breaths_per_minute > 20:
                return "Rapid breathing, possible physical stress."
            else:
                return "Normal breathing."

        def check_energy_levels(self, energy_level):
            """checks energy leves."""
            self.energy_level = energy_level
            if energy_level < 5:
                return "Low energy, possible physical stress."
            else:
                return "Normal energy."

        def access_physical_activity(self, physical_activity):
            """access physical activity."""
            self.physical_activity = physical_activity
            if physical_activity < 6:  # Corrected variable name
                return "Low physical activity, possible physical stress."
            else:
                return "Good physical activity."

        def check_nurtation(self, diet_quality):
            """check nurtation quality."""
            self.diet_quality = diet_quality
            if diet_quality < 6:
                return "Poor nurtation, possible physical stress."
            else:
                return "Good nurtation."

        def measure_body_temperature(self, temperature):
            """measures body temperature."""
            self.temperature = temperature
            if temperature > 37.5:
                return "Elevated temperature, possible physical stress."
            else:
                return "Normal temperature."

    class MentalStress:
        # Handles analysis of mental stress factors.

        def analyze_concentration(self, concentration_level):
            """Analyzes concentration levels."""
            self.concentration_level = concentration_level
            if concentration_level < 5:
                return "Low concentration, possible mental stress."
            else:
                return "Normal concentration."

        def assess_memory(self, memory_performance):
            """Assesses memory performance."""
            self.memory_performance = memory_performance
            if memory_performance < 6:
                return "Poor memory, possible mental stress."
            else:
                return "Normal memory."

        def analyze_decision_making(self, decision_quality):
            """Analyzes decision-making quality."""
            self.decision_quality = decision_quality
            if decision_quality < 6:
                return "Impaired decision-making, possible mental stress."
            else:
                return "Normal decision-making."

        def check_mental_clarity(self, clarity_level):
            """Checks mental clarity."""
            self.clarity_level = clarity_level
            if clarity_level < 5:
                return "Low mental clarity, possible mental stress."
            else:
                return "Normal mental clarity."

        def assess_problem_solving(self, problem_solving_ability):
            """Assesses problem-solving ability."""
            self.problem_solving_ability = problem_solving_ability
            if problem_solving_ability < 6:
                return "Reduced problem-solving, possible mental stress."
            else:
                return "Normal problem-solving."

        def measure_cognitive_load(self, load_level):
            """Measures cognitive load."""
            self.load_level = load_level
            if load_level > 7:
                return "High cognitive load, possible mental stress."
            else:
                return "Normal cognitive load."

        def analyze_focus(self, focus_level):
            """Analyzes focus levels."""
            self.focus_level = focus_level
            if focus_level < 5:
                return "Low focus, possible mental stress."
            else:
                return "Normal focus."

        def check_mental_fatigue(self, fatigue_level):
            """Checks mental fatigue."""
            self.fatigue_level = fatigue_level
            if fatigue_level > 7:
                return "High mental fatigue, possible mental stress."
            else:
                return "Normal mental fatigue."

        def assess_learning_ability(self, learning_performance):
            """Assesses learning ability."""
            self.learning_performance = learning_performance
            if learning_performance < 6:
                return "Reduced learning ability, possible mental stress."
            else:
                return "Normal learning ability."

        def analyze_thought_patterns(self, thought_pattern_quality):
            """Analyzes thought patterns."""
            self.thought_pattern_quality = thought_pattern_quality
            if thought_pattern_quality < 6:
                return "Negative thought patterns, possible mental stress."
            else:
                return "Positive thought patterns."

    class EmotionalStress:
        # Handles analysis of emotional stress factors.

        def analyze_mood(self, mood_level):
            """Analyzes mood levels."""
            self.mood_level = mood_level
            if mood_level < 5:
                return "Negative mood, possible emotional stress."
            else:
                return "Positive mood."

        def assess_anxiety(self, anxiety_level):
            """Assesses anxiety levels."""
            self.anxiety_level = anxiety_level
            if anxiety_level > 7:
                return "High anxiety, possible emotional stress."
            else:
                return "Low anxiety."

        def check_irritability(self, irritability_level):
            """Checks irritability levels."""
            self.irritability_level = irritability_level
            if irritability_level > 7:
                return "High irritability, possible emotional stress."
            else:
                return "Low irritability."

        def measure_emotional_stability(self, stability_level):
            """Measures emotional stability."""
            self.stability_level = stability_level
            if stability_level < 5:
                return "Low emotional stability, possible emotional stress."
            else:
                return "High emotional stability."

        def analyze_emotional_resilience(self, resilience_level):
            """Analyzes emotional resilience."""
            self.resilience_level = resilience_level
            if resilience_level < 6:
                return "Low resilience, possible emotional stress."
            else:
                return "High resilience."

        def assess_emotional_regulation(self, regulation_level):
            """Assesses emotional regulation."""
            self.regulation_level = regulation_level
            if regulation_level < 6:
                return "Poor regulation, possible emotional stress."
            else:
                return "Good regulation."

        def check_emotional_awareness(self, awareness_level):
            """Checks emotional awareness."""
            self.awareness_level = awareness_level
            if awareness_level < 5:
                return "Low awareness, possible emotional stress."
            else:
                return "High awareness."

        def measure_emotional_expression(self, expression_quality):
            """Measures emotional expression."""
            self.expression_quality = expression_quality
            if expression_quality < 6:
                return "Poor expression, possible emotional stress."
            else:
                return "Good expression."

        def analyze_emotional_support(self, support_quality):
            """Analyzes emotional support."""
            self.support_quality = support_quality
            if support_quality < 6:
                return "Low support, possible emotional stress."
            else:
                return "High support."

        def assess_emotional_coping(self, coping_effectiveness):
            """Assesses emotional coping."""
            self.coping_effectiveness = coping_effectiveness
            if coping_effectiveness < 6:
                return "Poor coping, possible emotional stress."
            else:
                return "Good coping."

    class BehaviorStress:
        # Handles analysis of behavioral stress factors.

        def analyze_sleep_patterns(self, sleep_duration, sleep_quality):
            """Analyzes sleep patterns."""
            self.sleep_duration = sleep_duration
            self.sleep_quality = sleep_quality
            if sleep_duration < 7 or sleep_quality < 6:
                return "Disrupted sleep patterns, possible behavior stress."
            else:
                return "Healthy sleep patterns."

        def assess_eating_habits(self, eating_frequency, diet_variety):
            """Assesses eating habits."""
            self.eating_frequency = eating_frequency
            self.diet_variety = diet_variety
            if eating_frequency < 3 or diet_variety < 5:
                return "Poor eating habits, possible behavior stress."
            else:
                return "Healthy eating habits."

        def analyze_social_interaction(self, social_engagement):
            """Analyzes social interaction."""
            self.social_engagement = social_engagement
            if social_engagement < 3:
                return "Low social interaction, possible behavior stress."
            else:
                return "Adequate social interaction."

        def check_substance_use(self, substance_frequency, substance_type):
            """Checks substance use."""
            self.substance_frequency = substance_frequency
            self.substance_type = substance_type
            if substance_frequency > 0:
                return f"Substance use detected ({substance_type}), possible behavior stress."
            else:
                return "No substance use."

        def assess_time_management(self, time_efficiency):
            """Assesses time management."""
            self.time_efficiency = time_efficiency
            if time_efficiency < 6:
                return "Poor time management, possible behavior stress."
            else:
                return "Good time management."

        def analyze_procrastination(self, procrastination_level):
            """Analyzes procrastination levels."""
            self.procrastination_level = procrastination_level
            if procrastination_level > 7:
                return "High procrastination, possible behavior stress."
            else:
                return "Low procrastination."

        def check_impulsivity(self, impulsivity_level):
            """Checks impulsivity levels."""
            self.impulsivity_level = impulsivity_level
            if impulsivity_level > 7:
                return "High impulsivity, possible behavior stress."
            else:
                return "Low impulsivity."

        def assess_aggression(self, aggression_level):
            """Assesses aggression levels."""
            self.aggression_level = aggression_level
            if aggression_level > 5:
                return "High aggression, possible behavior stress."
            else:
                return "Low aggression."

        def analyze_withdrawal(self, social_withdrawal):
            """Analyzes social withdrawal."""
            self.social_withdrawal = social_withdrawal
            if social_withdrawal > 5:
                return "High social withdrawal, possible behavior stress."
            else:
                return "Low social withdrawal."

        def check_self_isolation(self, isolation_frequency):
            """Checks self-isolation."""
            self.isolation_frequency = isolation_frequency
            if isolation_frequency > 3:
                return "Frequent self-isolation, possible behavior stress."
            else:
                return "Infrequent self-isolation."

    class LifestyleStress:
        # Handles analysis of lifestyle stress factors.

        def analyze_work_life_balance(self, work_hours, leisure_time):
            """Analyzes work-life balance."""
            self.work_hours = work_hours
            self.leisure_time = leisure_time
            if work_hours > 40 and leisure_time < 10:
                return "Poor work-life balance, possible lifestyle stress."
            else:
                return "Good work-life balance."

        def assess_financial_strain(self, financial_stability):
            """Assesses financial strain."""
            self.financial_stability = financial_stability
            if financial_stability < 5:
                return "High financial strain, possible lifestyle stress."
            else:
                return "Low financial strain."

        def analyze_relationship_stress(self, relationship_quality):
            
            """Analyzes relationship stress."""
            self.relationship_quality = relationship_quality
            if relationship_quality < 6:
                return "Strained relationships, possible lifestyle stress."
            else:
                return "Healthy relationships."

        def check_commute_stress(self, commute_time, commute_method):
            """Checks commute stress."""
            self.commute_time = commute_time
            self.commute_method = commute_method
            if commute_time > 60:
                return f"Long commute ({commute_time} minutes), possible lifestyle stress."
            else:
                return "Reasonable commute time."

        def assess_housing_stability(self, housing_security):
            """Assesses housing stability."""
            self.housing_security = housing_security
            if housing_security < 5:
                return "Unstable housing, possible lifestyle stress."
            else:
                return "Stable housing."

        def analyze_social_support(self, support_network_size, support_quality):
            """Analyzes social support."""
            self.support_network_size = support_network_size
            self.support_quality = support_quality
            if support_network_size < 3 or support_quality < 6:
                return "Inadequate social support, possible lifestyle stress."
            else:
                return "Adequate social support."

        def check_leisure_activities(self, leisure_frequency, leisure_variety):
            """Checks leisure activities."""
            self.leisure_frequency = leisure_frequency
            self.leisure_variety = leisure_variety
            if leisure_frequency < 3:
                return "Insufficient leisure activities, possible lifestyle stress."
            else:
                return "Adequate leisure activities."

        def assess_personal_growth(self, growth_opportunities):
            """Assesses personal growth."""
            self.growth_opportunities = growth_opportunities
            if growth_opportunities < 5:
                return "Limited growth opportunities, possible lifestyle stress."
            else:
                return "Sufficient growth opportunities."

        def analyze_sense_of_purpose(self, purpose_level):
            """Analyzes sense of purpose."""
            self.purpose_level = purpose_level
            if purpose_level < 6:
                return "Low sense of purpose, possible lifestyle stress."
            else:
                return "High sense of purpose."

        def check_exposure_to_stressors(self, stressor_frequency, stressor_intensity):
            """Checks exposure to stressors ."""
            self.stressor_frequency = stressor_frequency
            self.stressor_intensity = stressor_intensity
            if stressor_frequency > 5 or stressor_intensity > 7:
                return "High exposure to stressors, possible lifestyle stress."
            else:
                return "Moderate exposure to stressors."
