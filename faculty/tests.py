from django import test
from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Faculty, Department

class FacultyTest(TestCase):

    def test_faculty_name_should_not_cross_60(self):
        testVal = "Due to the size and power of many eagle species, they are ranked at the top of the food chain as apex predators in the avian world. The type of prey varies by genus. The Haliaeetus and Ichthyophaga eagles prefer to capture fish, though the species in the former often capture various animals, especially other water birds, and are powerful kleptoparasites of other birds. The snake and serpent eagles of the genera Circaetus, Terathopius, and Spilornis predominantly prey on the great diversity of snakes found in the tropics of Africa and Asia. The eagles of the genus Aquila are often the top birds of prey in open habitats, taking almost any medium-sized vertebrate they can catch. Where Aquila eagles are absent, other eagles, such as the buteonine black-chested buzzard-eagle of South America, may assume the position of top raptorial predator in open areas. Many other eagles, including the species-rich genus Spizaetus, live predominantly in woodlands and forests. These eagles often target various arboreal or ground-dwelling mammals and birds, which are often unsuspectingly ambushed in such dense, knotty environments. Hunting techniques differ among the species and genera, with some individual eagles having engaged in quite varied techniques based on their environment and prey at any given time. Most eagles grab prey without landing and take flight with it, so the prey can be carried to a perch and torn apart"
        p = Faculty(facultyName=testVal)
        with self.assertRaises(ValidationError):
            p.full_clean()