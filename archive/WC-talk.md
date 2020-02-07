Wendy Chun
"Facing Re-cognition: Algorithms and the New Politics of Recognition - Biometrics 2.0, or Regressing to eugenics - Repeating difference"

Tracing the historical move from pattern discrimination to pattern recognition
how we become figures in a drama called Big Data

# This talk is the last chapter of the book Discriminating Data
Book as a whole: Discriminating Data reveals how alhorithms encode legacies of segregation, eugenics and multiculturalism through proxies, latent factors, principal components, and network neighborhoods -- these legacy categories persist and mutate through systems that are allegedly blind to the, and seek to blind us to them. The goal is not just to uncover these legacy codes, but to transform them-- to prototype different types of networks

## The book makes 5 points
1. Being blind to race blindly promotes racism: ignoring difference amplifies discrimination. rewriting political problems as ones tech can and should sell has never worked
2. interrogate the default assumptions and axioms that ground algorithms and data structure, especially homophily: the idea that similarity breeds connection. Echo chambers and segregation are the goal, not an accident.
3. to apprehend the future machinelearning algorithms put in place, we have to understand when why and how their predictions work. Nothing ever simply stays the same: these programs try to predict the future by reducing it to the past; they are disruptive not because they make a new future, but because they forclose it 
4. To keep the future open and make it more just and democratic, we need to be a little perverse: read these results against the grain, as evidence of past discrimination, to diagnose current inequalities. Rather than discard Amazon program that discriminated against women, *use* it like global climate change models that give us the most probable future from out past actions NOT so we can continue those actions but so we can change. (Global climate change models have arguably been completely ineffective: what does documenting the obvious actually do? How can we use these diffrently?)
5. We need to make new algorithms. This is the goal of the Digital Democracies Group she works with (which needs Canadian legal scholars)

# Recognition

Why and how in cybernetics and in culture there has been a move  away from techniques of discrimination to techniques of recognition, which are arguably the same thing

## Face recognition

* Face recognition is sold as a way to do lots of things (especially authentication and crime tracking), but it notoriously error prone, especially when it comes to gender and race
* They are trained on celebrities and US undergraduates, "those well-known hotspots of diversity"
  * People of color are both over and under used: they train criminal
* The queston isn't "why is this happening now?" but "why is this still happening?"
  * Early examples, Shirley card and Lena
  * Shoshana Magnet, When Biometrics Fail: these technologies engage in corporeal fetishism, the belief that somehow things don't change and that they can be reduced
* San Francisco is the first city to ban face recognition technoogies, even though its a very white and asian city... but it IS a popular city for developers of face recognition software! An intriguing coalitio between startup bros and the ACLU
  * Not just banned due to evidence of bias or unprecendented power to track people, but for HYPOTHETICAL possible injustices,because it theatened to reveal intimate characteristicss
* Machine learning gaydar claimed to be better at identifying gay people than humans
   * People often like to skip the math when they critique things like this... but we're going to go through them, because if we skip them, we have to treat them as exceptional examples and miss the systemic norms. They use common off the shelf processes.
   * First, they scraped a US dating site for 130,000 self-portraits (which are considered to be public)
   * Used a program Face++ to read and clean data; removed all images with multiple faces, people not looking at the 
   * Used Mechanical Turk workers to verify that all faces were adult, Caucasian, fully visible, and of a gender that matched the one reported on the user's profile (i.e., HUMANS proofread the machine;s result)
   * This brought them down to 36k men and 38k women
   * Used off the shelf software VGG-Face, which they claimed would reduce overfitting -- but whereas Face++ was trained on Chinese faces, VGG was trained on Americans, esp George Bush
   * Evaluated 4,000 variables, selected those which were best at discriminatng between individuals -- features that discriminate the most are the most valuable. Reduced to 500 dimensions with SVD and PCA. "Features" aren't things like "a nose" but micro
   * They used most of the data for training, one for testing, but nothing for cross-validation
   * Got to 80% for men, 70% for women -- up from 50% random guess; better than Mechanical Turk human guesses
   * Ran it with some parts of the image masked to see which features can most accurately identify sexuality, and come up with "archetypal" gay and straight faces
      * Gay men have narrower faces, less facial hair; straight men wear baseball caps
      * Straight women wear more eye makeup; women smile more than men, but gay women smile less than straight women
   * Further tested based on facebook data that they had because 5 million people had filled out a personality quiz
   * They concluded that orientation is biologically inherent in faces due to hormones. And since people have to show their faces, and their faces tell their orientation, we need to be more tolerant in a "postprivacy world"
   * Because PHT is biological they assume that their findings will hold for all races even though they only studied white Americans
   * They assume that all photos are accurate because "why would people on dating sites lie"
   * But they overlook that sexuality is itself something that people signal intentionally through socially contingent signs
   * This study simultaneously repudiates and resuscitates physiognomy.
   
# Biometric Eugenics, Regressing to the Future
* It's no accident that this article starts by citing physiognomy. The links are not just conceptual, but methodological.
   * EG use of composite images to show "typical" faces -- repeats both the form and the purpose of Galton's images of "the Jewish type"
* Allan Sekula, "The Body and the Archive"
   * Bertillon was obsessed with criminal recidivism, and with false documents; came up with measurements to identify any indivisual
   * Galton and Bertillon both try to link past images to future subjects
* Galton also came up with a notion of correlation which is the basis of current anaytics, in response to Berillon's too-detailed measures
* Big Data privileges correlation rather than causation.
* In link prediction algorithsm, missing past data are filled in the exact same way as future data is predicted
* They can also only be verified as correct if they make discriminatory assessment
   * There can be no disruption; recognition = repetition
* All boils down to dorrelation, regression, and recognition
   * Pearson correlation coefficient and other things are all toold developed to support eugenics.
   * Galton was a biometrician 
   * Galton developed linear regression to understand inheritance of trait
* Galton's argument was that deviations over time regress back to an ancient mean, so unless exceptions are carefully "bred" they would degenerate to the mean
* At the heart of all arguments for eugenics was correlation: anything correlation measured was nature rather than nurture. It measures what remains the same across time and place. (In their eye)
   * So training, education, social programs are useless -- these can't create ntelligence -- it must be bred
* SVM is based on linear discrimance
   * Also based on measuring skulls and jaws to predict racial differences, caste mixing, and intelligence
* The point isn;t that any use of these methods and statistics is eugenicist. My point rather is that if the world seems closed now, it's becaue these methods were designed to predict a world based onthe past--in this world there is no uture, only nature.
* It's perverse that a system that refuses to believe in learning is now the basis of machine learning. It's also perverse that a system designed for discrimination is not used for recognition.
* Before there was pattern recognition, there was pattern dscrimination, which stems from studies on animal vision, seeing how animal vision differs from human in terms of color hue, etc; place animals in "discrimination boxes". Experimented with torturing and feeding rats to see which worked better..
   * Uncovering these populations which had been studied is fascinating and allows reinterpretation of the effects seen
* The move is due to cybernetics' emphasis that the **pattern** was the thing

# 3: Authenticating difference
* Nancy Fraser and Axel Honneth: Redistribution and Recognition -- misrecognition isn't personal, it's istitutional
* Misrecognition is keyed to indigenous rights to land, Coulton (???) says misrecognition is used to deny redistribution of land
   * Beth Povinelli -- insiting indigenous people repeat a past for ""multiculturalism"" to survive; some people must be  "authentic" aka unchanging from past in order to be recognizes
* The only group now insistng on recognition without redistribution is the reactionary right.
   * Also making their claims based on their own invented physiognomy, self-diagnosed phrenology
* Authenticity doesn't equal authentication
* What if we took seriously our role as characters in a drama that we call Big Data? What would happen if we made gender and media studies the grounds from which new inventions could emerge?
   * Beth Coleman Race as Technoogy
   * Recognition can be a way of denying respect
   * Combahee River Collective Statement
   * How can we make these experiences the ground truth for our models?
   
# Q&A

* There's a technical definition of discrimination; social science makes discrimination a bad word, but it's very useful to have a metric that discriminates. Seeing faces and saying someone looks gay, we do the same thing as the machine, but the machine does it more efficiently and more accurately. [A truly stunning exemplification of everything she discusses as the history of this work]
* Why do this? What can be possible from this?
   * You can say that these algorithms can actually be really good at showing historical trends, and the future most probably based on the past. So how do we use these to open the future?
   * With climate change models, modellers don't **want** to be right. They want us to act in such a way that we won't know.
   * Raises a question of **verificability**, and what new forms of verifiability we can introduce.
   * Doing collabs, "what is the question you can't answer on your own?" -- biostats guy asked, if I can show any correlation can exist, what's true, what matters the most?
* How do you deal with the onslaught of digital humanities?
   * What's exciting about the DH turn... for us to gain technical expertise not so we can all program and get better jobs, but because it's whe you engage with tech that you actually see the **limitations**.
   * Questions and problems that can't be answers by one discipline alone
* Classification systems
   * Trying to understand different forms of connection, not just the standard "similarity breeds connection"
   * What if we used indifference? Instead of responding to mixed borders as a problem to solve with better discrimination, but its own psace
   * Think about ecerything you need NOT to care abbout in order to ride the TTC
* What's the law's immediate role? Lowest hanging fruit?
   * Really interesting that in these algorithsm, esp learning ones which don't store data but do change the algorithm -- the separation between data and algorithm is NOT clear. So the right to be deleted could give a way to open up these proprietary algorithms
* To what extent are these thigs classed?
* Wondering about ageism, esp the facebook 10 year challenge as data mining
   * Yes, absolutely -- ageism in dating analysis too. Interesting assumption they made that people over 45 don't date.
   * If we take gaydar as a cultural phenomenon seriously, or other ways people signal -- Irving Goffman's notion of play and performance and interpreting character
* Back to the depression question: In Canada we can rely on Charter of Rights and Freedoms and protection from descrimination on certain grounds... how easy is it to reproduce this work, to understand whether the government is using any of these kinds of algorithms for discriminatory selection processes?
   * I know that the ACLU in particular is working on with, with AI Now, organizations that are suing algorithms... the question is the uptake, but she's just now looking at the uptake within Canadian authorities
* Matching mistakes, like her identity being mergd with somebody else so her work is atrtibuted to them -- from a computing perspective, address artificial stupidity, algorithmic error?
   * A lot of work on that, esp in terms of user verification... something fruitful, argument could be made via correlation that when you act you're never alone; a possibility of understandinggroup dynamics and solidarity through this. Example is Wu Tang Clan fans -- one of the correlated likes for male heterosexuality. If we start with Wu Tang Clan, as the core of understanding male heterosexuality itself, we can see male heterosexuality as a fascinating combination of elements
* Regarding digital doppelganders, and how facial recognition can impact doppelganger work predicting what people will do
   * We're trying to come up with a richer notion of authenticity, so it's not just replicability.
   * With fake news detection, people focus on wehter something is correct or incorrect -- but a lot of people expriencing it don't care, and corecting a story can actually spread the story. The more a certain poltiicial lies the more authentic he is viewed to be. So what else can we use as out definition. Under what conditions do people find information to be true? Eg people read novels, and they're not correct but they're true
* History of social engineering, seemed to underly the things she saw -- worrying about how people's behaviour is (un?)intentionally shaped by recognition without their knowing. What do you see as the future of social engineering, how can we react to it?
   * Work on homophily was unapologetically social engineering. The question to ask ourselves, if we look at a corporation like facebook, they're doing constant A/B testing for behaviour modification -- now will it happen but how is it being engaged? Think through how influence operates. People freaked out about cambridge analytica. Can we be clearer about how we understand effects? Clickbait is important because of the larger economic model.
   
Something fascinating about real name policies, and the assumption of a single authentic self which actually falls apart -- and the assumption that due to homophily everyone one knows belongs in the same social network, that you are always the same self. Connection to facebook as the defacto sign-in for all websites?
