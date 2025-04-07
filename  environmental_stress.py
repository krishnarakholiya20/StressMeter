class EnvironmentalStress:
    def noise_pollution(self, noise_level):
        return f"{'High' if noise_level > 70 else 'Normal'} noise pollution ({noise_level} dB)"

    def air_quality(self, aqi):
        return f"{'Poor' if aqi > 100 else 'Good'} air quality (AQI: {aqi})"

    def lighting_conditions(self, light_intensity):
        return f"{'Dim' if light_intensity < 200 else 'Bright'} lighting ({light_intensity} lux)"

    def temperature_stress(self, temp):
        return f"{'Hot' if temp > 30 else 'Comfortable'} room temperature ({temp}°C)"

    def crowd_density(self, people_per_area):
        return f"{'Crowded' if people_per_area > 10 else 'Spacious'} environment"

    def space_availability(self, space_level):
        return f"{'Low' if space_level < 5 else 'Adequate'} space available"

    def nature_exposure(self, hours_outdoors):
        return f"{'Low' if hours_outdoors < 1 else 'Healthy'} outdoor time"

    def environmental_allergens(self, allergen_index):
        return f"{'High' if allergen_index > 5 else 'Low'} allergen exposure"

    def water_quality(self, water_score):
        return f"{'Poor' if water_score < 70 else 'Safe'} water quality ({water_score}/100)"

    def waste_exposure(self, waste_index):
        return f"{'High' if waste_index > 5 else 'Low'} waste exposure"
