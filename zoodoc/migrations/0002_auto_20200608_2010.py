# Generated by Django 3.0.7 on 2020-06-08 20:10

from django.db import migrations


def seed(apps, schema_editor):
    Doctor = apps.get_model('zoodoc', 'Doctor')
    Review = apps.get_model('zoodoc', 'Review')

    doctor1 = Doctor(first_name='Dr. Monique', last_name='Jones', gender='Female',
                     image_url='https://dupontvetclinic.com/wp-content/uploads/2018/11/DrJonesHeadshotDVC-1024x701.jpg', specialization=['General', 'Dental', "Surgeon"], office_name='Dupont Veterinary Clinic', website='https://dupontvetclinic.com/veterinarians/', about='Dr. Jones attended the University of California, Davis for her undergraduate degree while working part-time as a veterinary technician, then Tuskegee University for her veterinary degree. After graduating, she completed a one-year general practice internship, which included experience with overnight emergency medicine. Her love and care for pets since childhood gives her an appreciation for pets as extended members of the family. She looks forward to providing the most sensitive and professional care to clients and their pets.', street_address='2022 P Street NW', city='Washington',
                     state='DC', zip_code='20036', phone_number='202-466-211').save()

    doctor2 = Doctor(first_name='Dr. Sophia', last_name='Chiang',
                     gender='Female', image_url='https://vcahospitals.com/alexandria/-/media/vca/images/hospitals/united-states/virginia/alexandria/staff/700x525_alexandria_sophiachiang.jpg?h=525&w=700&la=en&hash=101324895EAF938F567666678BDA6F7B', specialization=['General'], office_name='VCA Alexandria Animal Hospital', about='Dr. Chiang joined the VCA Alexandria Animal Hospital in July 2006. A native Texan, she received her undergraduate degree in Biology at the University of Chicago in 1997. She then taught high school science in rural North Carolina through the Teach For America Service Program before pursuing her veterinary degree at the North Carolina State University College of Veterinary Medicine.', website='https://vcahospitals.com/alexandria', street_address='2660 Duke Street', city='Alexandria',
                     state='VA', zip_code='22314', phone_number='703-751-2022').save()

    doctor3 = Doctor(first_name='Dr. Michael', last_name='Cohen', gender='Male', specialization=[
        'General'], image_url='https://images.squarespace-cdn.com/content/v1/5daf5d565bc9a966f3ea8f6e/1571776440616-PJYX74HZWBPH6X5H1YJ8/ke17ZwdGBToddI8pDm48kK7ZveHm8pdg6pR1a4N_eTlZw-zPPgdn4jUwVcJE1ZvWEtT5uBSRWt4vQZAgTJucoTqqXjS3CfNDSuuf31e0tVEP3MwU0KrqINgz5t1HlAV-YeUN3Jr-LO9jY1nwzkfdWl50gd2D5EdtNM4Q3D6aH4U/Cohen+1.jpg?format=500w', about="Michael Cohen earned his VMD in small animal medicine from the University of Pennsylvania in 2002. Raised just outside of Philadelphia, he graduated with honors from the University of Delaware and received special distinction for his research in dairy cattle nutrition. After graduation, Dr. Cohen was an associate veterinarian at a small practice in Delaware County for two years. To increase his range of experience, he spent six years as an emergency clinician at the Veterinary Specialty Center of Delaware.  Here he gained vital experience dealing with traumatic injuries, metabolic and endocrine diseases, toxin exposure, obstetrical emergencies, among others. Dr. Cohen was inspired to go back into private practice after working with animals whose emergency room visit could have been prevented with proper preventative care at their regular veterinarian's office. Dr. Cohen started Center City Veterinary Hospital to provide quality, modern, and compassionate care to the dogs and cats of Philadelphia.", office_name='Center City Veternary Hospital', website='https: // www.centercityvet.com/ourveterinarians', street_address='37 South 3rd Street', city='Philadelphia', state='PA', zip_code='19106', phone_number='215-923-2284').save()

    doctor4 = Doctor(first_name='Dr. Charles',
                     last_name='Weiss', gender='Male', image_url='https://www.bradleyhills.com/images/about.jpg', specialization=['General', 'Dental', 'Surgeon'], office_name='Bradley Hills Animal Hospital', about='Dr. Charles Weiss is a 1990 graduate of the University Of Missouri School Of Veterinary Medicine as its primary veterinarian. Dr. Weiss grew up in Long Island, NY where he began his veterinary medicine career at 14 years old as a Kennel Assistant at the South Shore Animal Hospital. He specializes in the treatment of dogs, cats, ferrets and other small mammals and Dr. Weiss is well-known in the area for his expertise in laser surgical techniques.', website='https://www.bradleyhills.com/index.html', street_address='7210 Bradley Blvd.', city='Bethesda',
                     state='MD', zip_code='20817', phone_number='301-365-5448').save()

    doctor5 = Doctor(first_name='Dr. Alexandra', last_name='Stocks',
                     gender='Female', image_url='https://40xgj11eopg738tg2n15vusr-wpengine.netdna-ssl.com/wp-content/uploads/2018/01/stocks.png', specialization=['General, Dental'], about='Dr. Stocks is a talented scholar, graduating Summa Cum Laude from Virginia–Maryland College of Veterinary Medicine. She also has associations with the D.C. Academy of Veterinary Medicine, Phi Zeta Veterinary Honor Society, Pi Theta Kappa International Honor Society, Alpha Psi Veterinary Fraternity and Omega Psi Veterinary Service Fraternity. She was named one of “NOVA’s Top Vets,” in 2017 by NOVA Magazine.', website='https://townandcountryanimalh.com/', street_address='9836 Fairfax Blvd', city='Fairfax',
                     state='VA', zip_code='22030', phone_number='703-273-2110',).save()

    doctor6 = Doctor(first_name='Dr. Lydia', last_name='Megremis',
                     gender='female', image_url='https://www.ovvhpets.com/sites/site-4609/images/Dr.%20M%20with%20Chase.jpg', specialization=['General', 'Dental'], about='I attended Purdue University and received my Bachelor of Science degree in Biology and my Doctor of Veterinary Medicine degree there. Shortly after graduation, I moved to the northern Virginia area and have been living and practicing in the area since then. Recently I completed the Canine Physical Rehabilitation course work through the University of Tennessee Veterinary School.', office_name='Oakton-Vienna Veterinary Hospital', website='https://www.ovvhpets.com/', street_address='320 Maple Ave E.', city='Vienna',
                     state='VA', zip_code='22180', phone_number='703-938-2800').save()

    doctor7 = Doctor(first_name='Dr. Howard', last_name='Cohen',
                     gender='Male', image_url='https://urbanvets.com/img/dr_cohen.jpg', specialization=['General', 'Surgeon'], office_name='Urban Vets Animal Hospital', website='https://urbanvets.com/our_mission.php', about="Dr. Cohen attended Brandeis University and graduated cum laude with a Bachelor's Degree in Biology in 1989. He went on to attend Ross University Veterinary School and Purdue University Veterinary School, where he was on the dean's list. He received his Doctorate in Veterinary Medicine in 1996. His professional interests include exotic animals, wellness medicine, cancer diagnostics and treatment and internal medicine.", street_address='163 Avenue 10th St', city='New York', state='NY',
                     zip_code='10009', phone_number='212-674-6200').save()

    doctor8 = Doctor(first_name='Dr, Awilda', last_name='Acaron',
                     gender='Female', specialization=['General', 'Dental', 'Surgeon'], image_url='https://s3-us-west-2.amazonaws.com/oa.vitalpet.net/staffs15859.jpg', office_name='City Vet', website='https://www.vitalpet.com/cityvet/about', about='Dr Acaron is originally from Puerto Rico. She received a Bachelor of Science in Animal Science from the University of Massachusetts- Amherst. Afterwards she attended Cornell University and obtained her Doctorate in Veterinary Medicine. After Cornell she lived in Miami, FL for a few years and then decided to venture back to New York.', street_address='45-44 Vernon Blvd', city='Long Island City',
                     state='NY', zip_code='11101', phone_number='718-433-1334',).save()

    doctor9 = Doctor(first_name='Dr. Beverly', last_name='Jogan', gender='Female', specialization=[
        'General', 'Surgeon'], image_url='https://images.squarespace-cdn.com/content/v1/5daf5d565bc9a966f3ea8f6e/1571776692189-5C2QU8K3OUBHEZU9YBK0/ke17ZwdGBToddI8pDm48kK7ZveHm8pdg6pR1a4N_eTlZw-zPPgdn4jUwVcJE1ZvWEtT5uBSRWt4vQZAgTJucoTqqXjS3CfNDSuuf31e0tVEP3MwU0KrqINgz5t1HlAV-YeUN3Jr-LO9jY1nwzkfdWl50gd2D5EdtNM4Q3D6aH4U/Jogan+1.jpg?format=500w', about='Beverly Jogan graduated from the University of Pennsylvania School of Veterinary Medicine in 2006 after completing her undergraduate degree at Penn where she studied biology and physical anthropology. She is originally from Reading, PA but also had the opportunity to live in South America, where she fell in love with animals by visiting llamas, penguins and toucans in their natural habitats. After completing vet school, Dr. Jogan practiced at a small animal hospital in New Jersey, and later enjoyed working with veterinary students at an animal shelter during a year spent in North Carolina. She has also volunteered on several spay/neuter clinic trips in underserved areas in the US and abroad. Dr. Jogan has special interests in pain management, geriatric medicine, preventive care, and ophthalmology.',  office_name='Center City Veterinary Hospital', website='https://www.centercityvet.com/', street_address='37 South 3rd Street', city='Philadelphia', state='PA', zip_code='19106', phone_number='215-923-2284').save()

    doctor10 = Doctor(first_name='Dr. Megan', last_name='Andeer', gender='Female', specialization=[
                      'General', 'Surgeon'], image_url='https://images.squarespace-cdn.com/content/v1/57e84580cd0f68ae05f0a0fc/1489005610218-5FOYR0L8KAS7KG5K4155/ke17ZwdGBToddI8pDm48kDQNDwN7RbC4y5p8pcw5hHJ7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1UZYOFdHNcPYOkPnUYVirq0DtHyn_95H4acgIa7uN-KRtItSUefHomSqcdhqblM-r5w/DSC00248.jpg?format=500w', about="Dr. Megan Andeer grew up in the Fairmount section of Philadelphia and attended Philadelphia public schools (Bache, Masterman and finally Central High School [253]). After attending University of Massachusetts Amherst for undergraduate work she graduated from University of Pennsylvania's school of Veterinary Medicine in 2001", office_name='City Cat Vets', website='http://www.citycatvets.com/', street_address='2210 South Street', city='Philadelphia', state='PA', zip_code='19146', phone_number='2155452287').save()

    doctor11 = Doctor(first_name='Dr. Killian', last_name='Lenahen', gender='Female', specialization=[
        'Dentist', 'Surgeon'], image_url='https://heartandpaw.com/images/KingofPrussia/iconDoctorKillian.png', about='Dr. Lenahen is a Philadelphia native and received her veterinary degree (VMD) from the University of Pennsylvania School of Veterinary Medicine. Dr. Lenahen is passionate about surgery, dentistry, and internal medicine with specific interests in ultrasonography and nutrition. She also enjoys volunteering for spay/neuter organizations in her spare time. Dr. Lenahen is a member of the AVMA and the PVMA, and is a USDA-accredited veterinarian. When not at work, Dr. Lenahen spends time with her boyfriend - a fellow veterinarian - and their senior dog, Josephine. She also enjoys travelling, cooking, hiking and dancing.', office_name='Low-Stress Veterinary Hospital', website='https://heartandpaw.com/locations/pennsylvania/king-of-prussia/veterinarian', street_address='201 Main St Suite 140', city='King of Prussia', state='PA', zip_code='19406', phone_number='4848034520').save()

    Review(name='Susie', description='The vet was great but I waited so long for my appointment', overall_rating='4',
           bed_side_rating='5', wait_time_rating='2', created_at='2017-09-26 11: 01: 20.547000', doctor=doctor1).save()

    Review(doctor=doctor2, name='Ana',
           description='This place is amazing it has an assortment of pet retail products, pet care services and amazing staff. My little nova cannot get enough of it', overall_rating='3.5', bed_side_rating='4', wait_time_rating='4', created_at='2017-09-26 11: 01: 20').save()


def fallow(apps, schema_editor):
    Doctor = apps.get_model('zoodoc', 'Doctor')
    Review = apps.get_model('zoodoc', 'Review')
    Doctor.objects.all().delete()
    Review.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('zoodoc', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]
