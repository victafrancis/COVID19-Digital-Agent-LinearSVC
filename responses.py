
#label classes
class_names = [
    'What is a novel coronavirus?',
    'What is the source of 2019-nCoV?',
    'How does the virus spread?',
    'How can I help protect myself?',
    'Is there a treatment for the infection?',
    'What do I do if I feel sick?',
    'Does CDC recommend the use of facemask in the community to prevent 2019-nCoV?',
    'What are the symptoms and complications that 2019-nCoV can cause?',
    'How do you test a person for 2019-nCoV?',
    'What is CDC doing about 2019-nCoV?',
    'Am I at risk for novel coronavirus from a package or products shipping from China?']
class_names

response0 = ['The 2019 Novel Coronavirus, or 2019-nCoV, is a new respiratory virus first identified in Wuhan, Hubei Province, China.',
    'A novel coronavirus (nCoV) is a new coronavirus that has not been previously identified. The 2019 novel coronavirus (2019-nCoV), is not that same as the coronaviruses that commonly circulate among humans and cause mild illness, like the common cold.',
    'A diagnosis with coronavirus 229E, NL63, OC43, or HKU1 is not the same as a 2019-nCoV diagnosis. These are different viruses and patients with 2019-nCoV will be evaluated and cared for differently than patients with common coronavirus diagnosis.']

response1 = ['Public health officials and partners are working hard to identify the source of the 2019-nCoV. Coronaviruses are a large family of viruses, some causing illness in people and others that circulate among animals, including camels, cats and bats. ',
    'Analysis of the genetic tree of this virus is ongoing to know the specific source of the virus. SARS, another coronavirus that emerged to infect people, came from civet cats, while MERS, another coronavirus that emerged to infect people, came from camels. More information about the source and spread of 2019-nCoV is available on the 2019-nCoV Situation Summary: Source and Spread of the Virus.']

response2 = ['According to preliminary research, it seems moderately infectious, similar to SARS, and is possibly transmitted through the air. Scientists have estimated that each infected person could spread it to somewhere between 1.5 and 3.5 people without effective containment measures.',
    'Much is unknown about how 2019-nCoV, a new coronavirus, spreads. Current knowledge is largely based on what is known about similar coronaviruses. Coronaviruses are a large family of viruses that are common in many different species of animals, including camels, cattle, cats, and bats. Rarely, animal coronaviruses can infect people and then spread between people such as with MERS, SARS, and now with 2019-nCoV.',
    'Most often, spread from person-to-person happens among close contacts (about 6 feet). Person-to-person spread is thought to occur mainly via respiratory droplets produced when an infected person coughs or sneezes, similar to how influenza and other respiratory pathogens spread. ',
    'These droplets can land in the mouths or noses of people who are nearby or possibly be inhaled into the lungs. It is currently unclear if a person can get 2019-nCoV by touching a surface or object that has the virus on it and then touching their own mouth, nose, or possibly their eyes.',
    'Typically, with most respiratory viruses, people are thought to be most contagious when they are most symptomatic (the sickest).','It is important to note that how easily a virus spreads person-to-person can vary. Some viruses are highly contagious (like measles), while other viruses are less so. There is much more to learn about the transmissibility, severity, and other features associated with 2019-nCoV and investigations are ongoing. This information will further inform the risk assessment. Read the latest 2019 Novel Coronavirus, Wuhan, China situation summary.']

response3 = ['There is currently no vaccine to prevent 2019-nCoV infection. The best way to prevent infection is to avoid being exposed to this virus. However, as a reminder, CDC always recommends everyday preventive actions to help prevent the spread of respiratory viruses, including:',
    'Avoid close contact with people who are sick.',
    'Avoid touching your eyes, nose, and mouth with unwashed hands.',
    'Stay home when you are sick.',
    'Cover your cough or sneeze with a tissue, then throw the tissue in the trash.',
    'Clean and disinfect frequently touched objects and surfaces using a regular household cleaning spray or wipe.',
    'Follow CDCs recommendations for using facemask.',
    'CDC does not recommend that people who are well wear facemask to protect themselves from respiratory viruses, including 2019-nCoV.',
    'Facemask should be used by people who show symptoms of 2019 novel coronavirus, in order to protect others from the risk of getting infected. The use of facemasks is also crucial for health workers and people who are taking care of someone in close settings (at home or in a health care facility).',
    'Wash your hands often with soap and water for at least 20 seconds, especially after going to the bathroom, before eating, and after blowing your nose, coughing, or sneezing. If soap and water are not readily available, use an alcohol based hand sanitizer with at least 60 percent alcohol. Always wash hands with soap and water if hands are visibly dirty. For information about handwashing, see CDCs Handwashing website',
    'For information specific to healthcare, see CDCs Hand Hygiene in Healthcare Settings',
    'These are everyday habits that can help prevent the spread of several viruses. CDC does have specific guidance for travelers.']

response4 = ['There is no specific antiviral treatment recommended for 2019-nCoV infection. People infected with 2019-nCoV should receive supportive care to help relieve symptoms. For severe cases, treatment should include care to support vital organ functions.',
    'People who think they may have been exposed to 2019-nCoV should contact your healthcare provider immediately.',
    'See Interim Guidance for Healthcare Professionals for information on persons under investigation']

response5 = ['Call ahead: If you have a medical appointment, call the healthcare provider and tell them that you have or may have COVID-19. This will help the healthcare provider office take steps to keep other people from getting infected or exposed.',
    'Stay away from others: As much as possible, you should stay in a specific room and away from other people in your home. Also, you should use a separate bathroom, if available.',
    'Avoid public areas: Do not go to work, school, or public areas.',
    'Avoid public transportation: Avoid using public transportation, ride-sharing, or taxis.',
    'How COVID-19  Spreads: Person-to-person spread',
    'The virus is thought to spread mainly from person-to-person.',
    'Between people who are in close contact with one another (within about 6 feet).',
    'Through respiratory droplets produced when an infected person coughs or sneezes.These droplets can land in the mouths or noses of people who are nearby or possibly be inhaled into the lungs.',
    'Can someone spread the virus without being sick?',
    'People are thought to be most contagious when they are most symptomatic (the sickest). Some spread might be possible before people show symptoms; there have been reports of this occurring with this new coronavirus, but this is not thought to be the main way the virus spreads.']

response6 = ['CDC does not recommend that people who are well wear a facemask to protect themselves from respiratory viruses, including 2019-nCoV. You should only wear a mask if a healthcare professional recommends it. A facemask should be used by people who have been exposed to 2019-nCoV and are showing symptoms of 2019 novel coronavirus.',
    'This is to protect others from the risk of getting infected. The use of facemasks also is crucial for health workers and other people who are taking care of someone infected with 2019-nCov in close settings (at home or in a health care facility).']

response7 = ['For confirmed 2019-nCoV infections, reported illnesses have ranged from people with mild symptoms to people being severely ill and dying.',
    'Symptoms can include: Fever, Cough, Shortness of breath',
    'CDC believes at this time that symptoms of 2019-nCoV may appear in as few as 2 days or as long as 14 after exposure. This is based on what has been seen previously as the incubation period of MERS viruses.',
    'The latest situation summary updates are available on CDCs web page 2019 Novel Coronavirus.',
    'If you develop a fever and symptoms of respiratory illness, such as cough or shortness of breath, within 14 days after travel from China, you should call ahead to a healthcare professional and mention your recent travel or close contact. If you have had close contact with someone showing these symptoms who has recently traveled from this area, you should call ahead to a healthcare professional and mention your close contact and their recent travel. Your healthcare professional will work with your state public health department and CDC to determine if you need to be tested for 2019-nCoV.']

response8 = ['At this time, diagnostic testing for 2019-nCoV can be conducted only at CDC.',
    'State and local health departments who have identified a person under investigation (PUI) should immediately notify CDCs Emergency Operations Center (EOC) to report the PUI and determine whether testing for 2019-nCoV at CDC is indicated. The EOC will assist local/state health departments to collect, store, and ship specimens appropriately to CDC, including during afterhours or on weekends/holidays.',
    'For more information on specimen collection see CDC Information for Laboratories.']

response9 = ['This is an emerging, rapidly evolving situation and CDC will continue to provide updated information as it becomes available. CDC works 24/7 to protect peoples health. It is CDCs job to be concerned and move quickly whenever there is a potential public health problem. More information about CDCs response to 2019-nCoV is available online.']

response10 = ['There is still a lot that is unknown about the newly emerged 2019 novel coronavirus (2019-nCoV) and how it spreads. Two other coronaviruses have emerged previously to cause severe illness in people (MERS and SARS). 2019-nCoV is more genetically related to SARS than MERS, but both are betacoronaviruses with their origins in bats. While we don nott know for sure that this virus will behave the same way as SARS and MERS, we can use the information from both of these earlier coronaviruses to guide us. In general, because of poor survivability of these coronaviruses on surfaces, there is likely very low risk of spread from products or packaging that are shipped over a period of days or weeks at ambient temperatures. Coronaviruses are generally thought to be spread most often by respiratory droplets. Currently there is no evidence to support transmission of 2019-nCoV associated with imported goods and there have not been any cases of 2019-nCoV in the United States associated with imported goods. Information will be provided on the 2019 Novel Coronavirus website as it becomes available.']


#responses
class_responses = [
    response0,
    response1,
    response2,
    response3,
    response4,
    response5,
    response6,
    response7,
    response8,
    response9,
    response10
    ]
class_names