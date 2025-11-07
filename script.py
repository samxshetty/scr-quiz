# Extract all 91 UHV questions from the PDF content
uhv_questions = [
    # Unit I Questions 1-91
    {"id": 1, "question": "What is invariant and universal among all human beings", "options": ["Natural Acceptance", "Understanding", "Expectations", "None of these"], "correct": 0},
    {"id": 2, "question": "Value education helps to", "options": ["Remove our confusions", "Bring harmony in all levels of human living", "Removes our contradictions", "All of these"], "correct": 3},
    {"id": 3, "question": "Holistic development of human beings", "options": ["Living only with Physical facility", "Living with Relationships", "Living for all the three – right understanding, relationship and physical facility (Human Consciousness)", "None of these"], "correct": 2},
    {"id": 4, "question": "Experiential validation of proposal means", "options": ["Living according to our desires", "Living according to proposal after verifying it by natural acceptance", "Living according to our expectations", "Living according to our thoughts"], "correct": 1},
    {"id": 5, "question": "Ensuring justice in relationship on the basis of values leads to --------- in the society.", "options": ["Trust", "Fearlessness", "Respect", "None of these"], "correct": 1},
    {"id": 6, "question": "Which of the following is more pronounced in animal consciousness?", "options": ["Right understanding", "Physical facility", "Relationship", "None of these"], "correct": 1},
    {"id": 7, "question": "Identify the correct order.", "options": ["Physical facility, right understanding, relationship", "Physical facility, relationship, right understanding", "Relationship, right understanding, physical facility", "Right understanding, relationship, physical facility"], "correct": 3},
    {"id": 8, "question": "Self-explorations means", "options": ["Dialogue between what you are and what you what to be", "It is the process of self-evaluation through self-investigation", "It is the process of knowing the human conduct", "All theses"], "correct": 3},
    {"id": 9, "question": "Which of the following fact is not true about profession, if ethics is followed in professional life?", "options": ["Able to earn a livelihood of the family", "Evaluated by the wealth it generates", "Requires certain skills", "Profession is also a service"], "correct": 1},
    {"id": 10, "question": "Need for value education:", "options": ["Correct identification of our aspirations", "To fulfill our aspirations in continuity", "Evaluation of our beliefs", "All of these"], "correct": 3},
    {"id": 11, "question": "Universal human aspirations means:", "options": ["Happiness and Prosperity", "Continuity of Happiness and Prosperity", "Happiness", "Prosperity"], "correct": 1},
    {"id": 12, "question": "What is happiness?", "options": ["A harmony state in which you want to be", "A state getting through sensations", "A state of preconditioning", "All of these"], "correct": 0},
    {"id": 13, "question": "The basic guideline for value education:", "options": ["Cannot be defined for the present system", "Cannot be universal", "Universal, Natural, Rational and Verifiable", "None of these"], "correct": 2},
    {"id": 14, "question": "Which one of the following is NOT the part of basic guidelines prepared for Value Education?", "options": ["Universal", "Rational", "Leading to disharmony", "Verifiable"], "correct": 2},
    {"id": 15, "question": "Which of the following is the attitude of ethical human conduct?", "options": ["Values", "Wealth", "Storage", "None of these"], "correct": 0},
    {"id": 16, "question": "Imagination includes", "options": ["Desires and Thoughts", "Thoughts and Expectations", "Desire and Expectations", "Desires, Thoughts and Expectations (DTE)"], "correct": 3},
    {"id": 17, "question": "Which of the options given below is one of the dimensions of human endeavour?", "options": ["Education", "Corruption", "Competition", "None of these"], "correct": 0},
    {"id": 18, "question": "The basic desire of the human being is always", "options": ["Happy", "Prosperous", "Happy and Prosperous", "None of these"], "correct": 2},
    {"id": 19, "question": "Human life is lived at four levels: Individual, Family, ...................., and Nature.", "options": ["Community", "Imaging", "Society", "Analyzing"], "correct": 2},
    {"id": 20, "question": "The definitiveness of human conduct in terms of values, policies and character is termed as .....................", "options": ["Responsibilities", "Values", "Profession", "None of these"], "correct": 1},
    {"id": 21, "question": "Developing the ethical competence in the profession is the only effective way to ensure ........................", "options": ["Responsibilities", "Ethics", "Professionalism", "Success"], "correct": 1},
    {"id": 22, "question": ".................. are considered the moral standards by which people judge the behaviour.", "options": ["Responsibilities", "Ethics", "Professionalism", "Success"], "correct": 1},
    {"id": 23, "question": ".............. is the implications of right understanding in profession.", "options": ["Responsibilities", "Ethics", "Professionalism", "Success"], "correct": 1},
    {"id": 24, "question": "Holistic production systems are", "options": ["Eco-friendly", "People friendly", "Both Eco- friendly and People friendly", "None of these"], "correct": 2},
    {"id": 25, "question": "Lot of physical facilities can provide us", "options": ["Happiness", "Prosperity", "Both Prosperity and Happiness", "None of these"], "correct": 3},
    {"id": 26, "question": "The basic capacity of analyzing is known as", "options": ["Desire", "Expectation", "Thought", "Behaviour"], "correct": 2},
    {"id": 27, "question": "The process of education and right living leads to...............", "options": ["Labour", "Right understanding", "Existence", "Co-existence"], "correct": 3},
    {"id": 28, "question": "The definiteness of behaviour and work of human being is termed as", "options": ["Human Behaviour", "Human Character", "Human Constitution", "Human Efforts"], "correct": 1},
    {"id": 29, "question": "Understanding of human values leads to the practice of", "options": ["Responsibility", "Professional Behaviour", "Ethics", "None of these"], "correct": 2},
    {"id": 30, "question": "The second dimension of human being is", "options": ["Thought", "Work", "Behaviour", "Realization"], "correct": 3},
    {"id": 31, "question": "When we set our goals in right direction with the help of right understanding, it is called as .............", "options": ["Skill Domain", "Development", "Value Domain", "Prosperity"], "correct": 2},
    {"id": 32, "question": "Our participation in different levels in the larger order is known as .................", "options": ["Behaviour", "Efforts", "Values", "None of these"], "correct": 2},
    {"id": 33, "question": "Attention and Appreciation from others", "options": ["Can't be continuous", "Can't ensure continuous happiness", "Create dependency on others", "All of these"], "correct": 3},
    {"id": 34, "question": "The programme for health and samyam leads to feeling of ............in family.", "options": ["Prosperity", "Happiness", "Both the Happiness and Prosperity", "None of these"], "correct": 2},
    {"id": 35, "question": "Production and work for physical facilities leads to ............ in family and ............. with nature.", "options": ["Prosperity, Existence", "Happiness, Existence", "Prosperity, Co-existence", "Happiness, Co-existence"], "correct": 2},
    {"id": 36, "question": "Education has two domains- Value Domain and Skill Domain. Which of the following is true?", "options": ["Value domain is the part of the skill domain", "Value domain is in conflict with skill domain", "The value domain deals with the understanding part, while the skill domain deals with the learning part.", "The value domain deals with the learning part, while the skill domain deals with the understanding part."], "correct": 2},
    {"id": 37, "question": "Value Education leads human being to", "options": ["Conflicts", "Confusion", "Harmony", "All of these"], "correct": 2},
    {"id": 38, "question": "It is the second level of living", "options": ["Individual", "Society", "Nature", "Family"], "correct": 3},
    {"id": 39, "question": "One of the undesirable common habits with us is that we have a tendency to suspect others ................", "options": ["Intention", "Competence", "Both intention and competence", "None of these"], "correct": 2},
    {"id": 40, "question": "Which of the following is not a dimension of human being?", "options": ["Society", "Thought", "Behaviour", "Realization"], "correct": 0},
    {"id": 41, "question": "In the process of self-exploration we will not verify on the basis of ................", "options": ["Others perception", "Scriptures", "Reading from instruments", "All of these"], "correct": 3},
    {"id": 42, "question": "It is the fourth level of living", "options": ["Society", "Nature", "Individual", "Family"], "correct": 1},
    {"id": 43, "question": "The result of self-exploration is............", "options": ["Realization", "Right understanding", "Both Realization and Right understanding", "None of these"], "correct": 2},
    {"id": 44, "question": "The process of verification of any proposal can be useful when verified", "options": ["At One's own right", "On the basis of reading from the instruments", "On the basis of readings from the books", "On the basis of others' perception and understanding"], "correct": 0},
    {"id": 45, "question": "Self-exploration is the dialogue between 'what you are' and", "options": ["'what you want to be'", "'what others want you to be'", "'what society wants you to be'", "All of these"], "correct": 0},
    {"id": 46, "question": "Continuous happiness and prosperity are the .................", "options": ["Impractical thought", "Impossible desires", "Basic human aspirations", "None of these"], "correct": 2},
    {"id": 47, "question": "To be wealthy is .................. condition in the modern world to be happy.", "options": ["The most important", "The true", "Not essential", "Fake"], "correct": 3},
    {"id": 48, "question": "Being happy ............ good-luck and lot of external circumstances.", "options": ["Means", "Depends on", "Does not depend on", "None of these"], "correct": 2},
    {"id": 49, "question": "Which one of the following is true?", "options": ["A human being needs both, relationship as well as physical facilities. One cannot replace the other.", "If a human being has abundant (plentiful) of physical facilities, her/his prosperity is ensured.", "If a human being has abundant (plentiful) of physical facilities, his/her happiness is ensured.", "If a human being is happy in continuity, she/he does not need physical facilities anymore."], "correct": 1},
    {"id": 50, "question": "Living with Physical Comforts only means ...........", "options": ["Animal Consciousness", "God Consciousness", "Human Consciousness", "Real Consciousness"], "correct": 0},
    {"id": 51, "question": "The feeling of producing/having more than required physical facility is", "options": ["Prosperity", "Happiness", "Success", "Satisfaction"], "correct": 0},
    {"id": 52, "question": "To verify the proposal or assumption through self exploration leads to", "options": ["Assuming", "Knowing", "Realizing", "Preconditioning"], "correct": 1},
    {"id": 53, "question": "Which are the four levels of living?", "options": ["Individual, family, society, nature", "Thought, behaviour, work, realization", "Material, pranic, animal, human", "None of these"], "correct": 0},
    {"id": 54, "question": "If something is .................. to us, without any force or compulsion, then it is often correct, and does not change with people and time.", "options": ["Not acceptable", "Less acceptable", "Completely acceptable", "Naturally acceptable"], "correct": 3},
    {"id": 55, "question": "The value of any unit in this existence is in its ........................ in the larger order of which it is a part.", "options": ["Participation", "Existence", "Performance", "Appearance"], "correct": 0},
    {"id": 56, "question": "The four dimensions of human being are thought, ..................., work and realization", "options": ["Action", "Speaking", "Behaviour", "Performance"], "correct": 2},
    {"id": 57, "question": "On continued basis we should examine our ..............", "options": ["Thought system", "Performance system", "Belief system", "None of these"], "correct": 2},
    {"id": 58, "question": "Two basic things in the content of self-exploration are to know my basic desires in may life and the second is to know how to .......................", "options": ["Perform these", "Remove these", "Fulfill these", "None of these"], "correct": 2},
    {"id": 59, "question": "Expression of thought is in the form of ............................", "options": ["Behaviour", "Work", "Realization", "Behaviour and Work"], "correct": 3},
    {"id": 60, "question": "Universal, rational, and verifiable are the ................... of value education.", "options": ["Needs", "Outcomes", "Basic guidelines", "None of these"], "correct": 1},
    {"id": 61, "question": "The value of entity is decided on the basis of ......................", "options": ["Participation in the larger order", "MRP", "Cost", "Physical properties"], "correct": 0},
    {"id": 62, "question": "Value education helps us to correctly identify our ................", "options": ["Goals", "Aspirations", "Desires", "All of these"], "correct": 3},
    {"id": 63, "question": "The purpose of the value education is to ..................", "options": ["Foster universal values", "Make the syllabus easy for the students to learn", "Develop values in individuals", "Both foster universal values and develop values in individuals"], "correct": 3},
    {"id": 64, "question": "A harmonious world is created by values at 4 levels. These are...................", "options": ["Home, Family, Society, Nation", "Individual, Family, Society, Existence", "School, Home, Office, Temple", "None of these"], "correct": 1},
    {"id": 65, "question": "The content of self-exploration is to understand the desire and ............. of human being.", "options": ["Potential", "Programme", "Purpose", "None of these"], "correct": 1},
    {"id": 66, "question": "Human-Rest of the nature interaction is called as ............", "options": ["Behaviour", "Production", "Work", "Realization"], "correct": 2},
    {"id": 67, "question": "Clarity and Identification of comprehensive human goals in the light of right understanding is called ........................", "options": ["Science", "Work", "Wisdom", "Behaviour"], "correct": 2},
    {"id": 68, "question": "Comprehensive human goals are fulfilled with the help of ............", "options": ["Wisdom", "Science", "Precondition and sensation", "All of these"], "correct": 1},
    {"id": 69, "question": "To ensure justice from family to world family is called ..................", "options": ["Production", "Science", "Wisdom", "Undivided human society"], "correct": 3},
    {"id": 70, "question": "Ensuring mutual fulfilment and mutual prosperity from family to world family is .........", "options": ["Science", "Wisdom", "Undivided human society", "Universal human order"], "correct": 3},
    {"id": 71, "question": "Which among the following is not a comprehensive human goal?", "options": ["Right understanding in every individual", "Mastery and complete control over nature", "Fearlessness in society", "Harmony in nature"], "correct": 1},
    {"id": 72, "question": "Ensuring the concept of undivided society and universal human order from generation to generation is called .............", "options": ["Wisdom", "Undivided human society", "Universal human order", "Human Tradition"], "correct": 3},
    {"id": 73, "question": "Transformation through Human Education includes", "options": ["Personal Transformation", "Societal Transformation", "Both Personal as well as societal transformation", "Materialistic transformation"], "correct": 2},
    {"id": 74, "question": "In society, obsession for consumption, profit and sensory pleasure is more due to", "options": ["Knowledge", "Assumption", "Recognition", "Fulfilment"], "correct": 1},
    {"id": 75, "question": "Sound, Touch, Taste, Smell, and Form are ..............", "options": ["Traps", "Innate faculty", "Sensations", "Preconditioning"], "correct": 2},
    {"id": 76, "question": "Definite completion point of feelings is ................", "options": ["Outside", "Within", "Nowhere", "Others"], "correct": 1},
    {"id": 77, "question": "An individual aspiring for the universal human order will be ..............", "options": ["More responsible socially and ecologically", "More rich", "More powerful", "None of these"], "correct": 0},
    {"id": 78, "question": "\"All are our own, all are interconnected and inter dependent\" means ............", "options": ["Oneness", "Worship", "Ease", "None of these"], "correct": 0},
    {"id": 79, "question": "............... and ....................... are the basis of undivided society", "options": ["Love and Oneness", "Care and guidance", "Affection and Respect", "None of these"], "correct": 0},
    {"id": 80, "question": "In Teacher – Student relationship, the teacher should have the feeling of ........... for the students.", "options": ["Love", "Guidance", "Care", "Gratitude"], "correct": 1},
    {"id": 81, "question": "In Teacher – Student relationship, the students should have the feeling of ........... for the Teachers.", "options": ["Love", "Guidance", "Care", "Gratitude"], "correct": 3},
    {"id": 82, "question": "For relationship among siblings, there is a need for the feelings of .........", "options": ["Love and Trust", "Care and affection", "Respect", "All of these"], "correct": 3},
    {"id": 83, "question": "What are the feelings that remain as base of all relationships?", "options": ["Reverence, Glory, Gratitude", "Trust, Respect, Affection", "Care, Guidance, Affection", "Trust, Reverence, Glory"], "correct": 1},
    {"id": 84, "question": "Moral value is combination of ...............", "options": ["Right Speech, Right Action", "Right Vision, Right Resolve", "Right Livelihood, Right Effort", "Right Awareness, Right Concentration"], "correct": 0},
    {"id": 85, "question": "Meditation includes .........................", "options": ["Right Speech, Right Action", "Right Vision, Right Resolve", "Right Livelihood, Right Effort", "Right Awareness, Right Concentration"], "correct": 3},
    {"id": 86, "question": "Belief centric wisdom is ..................", "options": ["Knowledge based on listening", "Knowledge based on self realization of existential reality", "Reasoning based knowledge", "None of these"], "correct": 0},
    {"id": 87, "question": "Logic centric wisdom is ....................", "options": ["Knowledge based on listening", "Knowledge based on self realization of existential reality", "Reasoning based knowledge", "None of these"], "correct": 2},
    {"id": 88, "question": "Realization centric wisdom is ................", "options": ["Knowledge based on listening", "Knowledge based on self realization of existential reality", "Reasoning based knowledge", "None of these"], "correct": 1},
    {"id": 89, "question": "Non-violence means not hurting anyone by ..............", "options": ["Body", "Mind", "Speech and words", "All of these"], "correct": 3},
    {"id": 90, "question": "Liberation means ...........", "options": ["To see the existence clearly", "To see the reality as it is", "To be rid of all types of misunderstanding, confusions", "All of these"], "correct": 3},
    {"id": 91, "question": "It is natural for ................... to slowly deteriorate", "options": ["Physical things/Physical facilities", "Happiness", "Feelings", "Relationship"], "correct": 0}
]

print(f"Total UHV questions extracted: {len(uhv_questions)}")
print("Sample questions:")
for i in range(3):
    q = uhv_questions[i]
    print(f"Q{q['id']}: {q['question']}")
    print(f"Options: {q['options']}")
    print(f"Correct: {q['correct']} ({q['options'][q['correct']]})")
    print()

# Verify all questions have correct structure
all_valid = all(
    len(q['options']) == 4 and 
    0 <= q['correct'] <= 3 and
    q['id'] == i + 1
    for i, q in enumerate(uhv_questions)
)

print(f"All questions valid: {all_valid}")
print(f"Question IDs range from {min(q['id'] for q in uhv_questions)} to {max(q['id'] for q in uhv_questions)}")