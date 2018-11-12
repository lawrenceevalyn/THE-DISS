Title: DISSERTATION  
Author: Lawrence Evalyn

# ch 2 - archives #



Chapter two takes up contemporary digital archives directly, examining corpora of eighteenth-century literature through the same critical lens by which anthologies and classroom teaching are often scrutinized. It makes the case that digital archives can implicitly shape scholarly research, and begins the process of revealing and interrogating their invisible assumptions. The chapter begins with a task somewhere between a literature review and a scientific meta-analysis. My first goal will be to survey as broadly as possible the accessible mass holdings of eighteenth-century texts (all those containing at least 100 works from the 1790s): simply putting all of this information in one place will be a useful way to review it. Adding a discussion of each archive’s selection criteria will bring it into the realm of a meta-analysis. I expect to find systematic exclusions where archives are investing more labour in their holdings, with narrower selections as they move from bibliographic data to facsimiles to scholarly transcripts. To contextualize these decisions about inclusion, I will research the history of how each corpus was formed. I will discuss and theorize the difficulties involved in researching these histories: drawing on, for example, my experience with HathiTrust’s codebase, I will critique the assumption that digital resources make all information transparent and accessible. Returning to the actual contents of each archive, I will discuss the nature of their exclusions, and consider paths to greater inclusivity. Then I will synthesize these disparate sources of texts and metadata, a substantial technical challenge, to see how the task may be accomplished, and to see what correlations between archives might illuminate the decade. I am particularly curious whether even one text will appear in all corpora, and, if so, which one it will be. Whichever texts appear most persistently will form the basis of my “case study” in this chapter. The second chapter thus establishes the corpora which will drive my argument in chapter three, and will shape the later phases of my research in chapters four and five.



## research Qs ##



	•	What’s in all these, anyway?

	⁃	What does ECCO-TCP leave out compared to ECCO? Compared to ESTC? (Can I come up with adjustment factors?)

	⁃	How do digital vs physical holdings compare?

	•	Can I identify how often texts are reprinted?? i.e., the most popular texts

	•	Can I identify male/female ratios?

	•	Can I identify the prevalence of various genres? (Topic modelling of titles) i.e., the most popular genres



## lit review ##



I plan to read secondary criticism for two major kinds of information, both of which will form the “lit review” section of chapter two. For each work I read, I will record the following:



Numbers against which I can compare my findings:

- Titles per year

- Authors, signed vs unsigned

- Authors, female vs male vs unknown

- Publication location



Assumptions against which I can compare my methodology:

- Treatment of reprints

- Circulation assumptions

- Excluded categories

- Genre ontology



### How do people determine popularity? ###



	1.	Simon Bainbridge: best-selling, most-reprinted, most-adapted

	2.	George Taylor: simply asserts that some things are popular

	3.	Emmet Kennedy, Marie-Laurence Netter, et al.: number of performances per play (Theatre, Opera, and Audience in Revolutionary Paris: Analysis and Repertory)



### Numbers to compare to ###



Comedies vs tragedies performed: the ratio of comedies to tragedies performed was an astonishing 14 to 1 in Paris (Theatre, Opera, and Audience in Revolutionary Paris: Analysis and Repertory by Emmet Kennedy, Marie-Laurence Netter, James P. McGregor, and Mark V. Olsen)



## corpora principles ##



### selection criteria ###



The full scope of my project is to grapple with every online database which contains at least 100 texts meeting my criteria: printed, in the United Kingdom, between the years 1789-99. [Or England??]

I exclude databases of diaries or correspondence, since they are not printed. This has the effect of excluding single-author databases.



### excluded corpora ###



Chawton House - too few novels

Gentleman’s Magazine resources - can’t filter by date

Lewis Walpole images digital collection at Yale - can’t filter by date

The Oxford Text Archive seems to be synonymous with ECCO-TCP; where it’s not, it’s not filterable by date/origin



U Sydney SETIS texts (paywalled) - http://setis.library.usyd.edu.au/setweb/uslsetistexts.html#english



### these are all databases ###



The primary methodological challenge to the questions I would like to pose is the standard makeup of these academic resources: self-contained databases, which are searchable for individual materials but not queryable for overall statistics. (I'd love to know the distribution-by-year of everything in the databases as a whole, but that may be beyond my scope.)



What I'm trying to do, essentially, is to forcibly "join" all of those databases -- the ESTC is my best bet so far, it looks like, for unique keys.

A true "standard" is probably both unfeasible and undesirable. So what can be usefully done with things that follow different standards? I think the answer might be OpenRefine, which I haven't seen extolled enough.



## OpenRefine ##



Having heard about OpenRefine by, essentially, eavesdropping on librarians at a conference, I adopted it for the task often called “data cleaning.”



### data cleaning ###



The metaphor of “data cleaning,” which seeks to purge inconsistencies in order to produce homogenized “tidy data” is at odds with the process that it actually describes.

[Messy, subjective judgments]

Though, you are in the end attempting to impose some kind of order



## topic modelling ##



I turn to topic modelling as a way to move “laterally”: if I can only query attributes which every archive records, I can’t query anything at all.



# THE DISS #



## proposal intro ##



 The Digital Archive and Print Politics, 1789–99



My dissertation seeks to determine, in as minute detail as possible, what the print landscape[ TK: Books only, or also serials, periodicals, newspapers, print ephemera (for the 1790s, there are a lot of things like handbills and broadsides in ECCO)? A fairly restrictive definition might be wise …  ] in England 1789-99 was actually like  — in contrast to the version that is presented in filtered and interpreted literary histories, built up by scholars or later generations of writers — and how this print landscape is represented now, in current digital archives[ TK: This will be very valuable, but of course you’re dealing here with a moving target and one subject to sudden transformations as well as gradual / incremental changes. Not sure what the solution is here but it’s something to thing about. Presumably you can’t make this chapter the last thing you do if you need the data for later chapters – or can you?]. My first chapter establishes the vocabulary and theoretical frameworks of the dissertation. Chapter two turns a critical eye on existing digital archives that feature material printed in the 1790s. Chapter three uses these corpora of 1790s literature to examine the idea of “popularity” as it is manifested by print culture. Chapter four introduces a second substantial experiment, a comprehensive mapping of the social networks underlying print production during the decade. Chapter five uses these networks to compare mainstream and non-mainstream printing practices[ TK: NB that you tend to use printing and publishing a bit too interchangeably. Presumably this one should be publishing practices? Print technologies are also changing in this era but that’s a whole different story, not part of yours I would imagine.]. A possible afterword or coda may discuss the role of the Gothic across the textual landscape.



## ch 1 - intro ##



My first chapter sets out the vocabulary and theoretical frameworks of the dissertation, with an explanation of why I have chosen to focus on the 1790s. As this chapter will discuss, I follow the work of scholars like T.L. Cowan and Jasmine Rault in understanding my research as a kind of reparative work on archives. I hope to locate my project alongside others in the DH field, led by scholars who are seeking to develop less “extractive” and more anti-oppressive[ Is there a better term? (why did TK think I wanted “anti-interpretive”?)] digital humanities methodologies. My first chapter will present a humanistic critique of the essentialist tendencies of some work in the field of DH, and discuss the pitfalls I have attempted to avoid in my own methodology. In discussing my methods, I will take up Johanna Drucker’s vocabulary of “capta,” rather than “data,” to emphasize that records are created, shaped by choices and by constraints, rather than neutrally “given.” I will apply insights from the emerging field of critical algorithm studies to reflect on the code I have written for the project, and the importance of engaging with digital projects at the level of code. I will also discuss my own preferred vocabulary around experiment design (modelling, sensitivity, fruitfulness), and its debts to Willard McCarty. Turning, then, from my tools to my materials, this chapter will also set out the limits to the project — material printed in Great Britain between January 1, 1789 and December 31, 1799 (inclusive). I will describe the importance of my selection of this this eleven-year “decade” to test my methods. A brief literature review of the literary output of the 1790s[ TK: Can you clarify this? Are you talking about the focus of the recent scholarship, or the focus of the writers at the time? As you rightly indicate elsewhere, these two things may not match -- your project might show the preoccupations of modern scholarship to be projections of our own rather than an accurate reflection of what dominated at the time. But “decade-long focus” makes it sound as though you’re talking about the 1790s writers themselves, i.e. accepting that “our” 1790s (dominated by, say, Thelwall and Wollstonecraft) is the same as the “real” one (though that might turn out to have been dominated by, say, Edmund Burke and Hannah More).] will highlight a decade-long focus on politics, the Gothic, and women writers.[ Although all of these elements interest me, and I anticipate that attention to this decade will reveal their prominence, I seek to avoid framing my inquiry explicitly around them and thus begging the question of their importance.] Finally, this chapter will bring together modern theories of the archive and my eighteenth century materials, by discussing the 1790s as a literary moment in which some significant literary canons begin to take form. When eighteenth century editors began to collect an English vernacular tradition posited against a Classical past and a French present, the “archive” of literary history was filtered into “canons” of texts, with connotations of merit and implications for national identity. The divergence between archive and canon motivates my return to the archive.



### vocabulary ###



#### queer DH ####



I follow the work of scholars like T.L. Cowan and Jasmine Rault in understanding my research as a kind of reparative work on archives. I hope to locate my project alongside others in the DH field, led by scholars who are seeking to develop less “extractive” and more anti-oppressive digital humanities methodologies



#### critique of DH essentialism ####



 a humanistic critique of the essentialist tendencies of some work in the field of DH



#### "capta" ####



Johanna Drucker’s vocabulary of “capta,” rather than “data,” to emphasize that records are created, shaped by choices and by constraints, rather than neutrally “given.”



#### Alberto Cairo ####



Data visualization vocabulary: framework; visual encoding (content); annotations



#### modelling, sensitivity, fruitfulness ####



my own preferred vocabulary around experiment design (modelling, sensitivity, fruitfulness), and its debts to Willard McCarty



##### editing #####



Is there someone better to cite than Leah Price, for the idea that all attempts to work with a text must involve editing/modelling it?



#### close-read my own code ####



I will apply insights from the emerging field of critical algorithm studies to reflect on the code I have written for the project, and the importance of engaging with digital projects at the level of code.



#### why 1789-99? ####



A brief literature review of the literary output of the 1790s will highlight decade-long focus on politics, the Gothic, and women writers[^cf1] 



#### lit review ####



A brief literature review of the literary output of the 1790s will highlight a decade-long focus on politics, the Gothic, and women writers.[^cf2]



#### 18th canon building ####



this chapter will bring together modern theories of the archive and my eighteenth century materials, by discussing the 1790s as a literary moment in which some significant literary canons begin to take form. When eighteenth century editors began to collect an English vernacular tradition posited against a Classical past and a French present, the “archive” of literary history began to be interpreted into “canons” of texts, with connotations of merit and implications for national identity. The divergence between archive and canon motivates my return to the archive.



#### "schools of thought" ####



my own understanding of eighteenth century politics as “schools of thought” governed by memetic natural selection.

Because politics occurs between individual people, not political parties, I argue that political affiliation, like literary genre, is not amenable to simple taxonomic classification.



## ch 3 - archive popularity ##



Chapter three expands upon the findings of the experiment carried out in chapter two, to examine popularity as it manifests in print culture. Influenced by Lesser and Farmer’s articulation of “structures of popularity,” I will consider popularity[ TK: Another tricky one. Might be best to avoid “popularity” unless you’re also going to factor in (as would be very hard) questions like print-runs (a nightmare imponderable), circulation (something aimed at libraries might have many more readers per copy than a book for home), unauthorized newspaper serializations, anthologization (is that a word?), false title pages (where a self-proclaimed 2nd or 10th edition might actually be just a new tp on remaindered sheets of a first edn that hasn’t sold. You could imagine (and this may have happened in practice) a novel published just once in 2,000 copies being more popular than one claiming five editions, none of which may have been more than 500 copies, and some of which may not have been true new editions at all. But which would come up as more popular give your metrics? This is all really tricky stuff and I think you’ll need a thorough discussion of the issues and assumptions.] in terms of total number of editions, frequency of reprinting, and market share.[ Lesser and Farmer also include profitability as one of the four measurements relevant to popularity in the book trade, but profitability is beyond the current scope of this project.] After determining how to calculate each of these metrics, I will ask: what was most popular during the decade, according to my corpora? How do the corpora differ in their answers, and why? I am particularly curious to see the place that chapbooks and religious tracts have in each corpus. My preliminary research suggests that many of the most reprinted works will substantially pre-date the 1790s in their composition. Accordingly, taking up David Brewer’s challenge to account for the increased “footprint” of some texts beyond the moment of their original publication, I will also pay attention to works originally written before the 1790s which nonetheless can be considered important “1790s literature” due to prominent reprinting. This inquiry’s first question is one of discovery: what works resurface in the 1790s? Its next question is one of close-reading and historical context: what makes them seem newly relevant? Restricting my inquiry only to the 1790s rather than nineteenth-century legacies, I will use my corpora to compare the publication output of various literary celebrities over the course of the decade. In addition to looking at the raw publication counts in the corpora defined in chapter two, I am currently exploring ways to use mentions in reviews and news articles to track prominence and reputation. The chapter as a whole, then, presents a sustained study of the relative popularity of the most prominent works printed during the 1790s, and seeks to answer how these prominent works might affect what we define as “popular literature”.



### consult Reading Experience Database? ###



The Reading Experience Database contains over 30,000 searchable records documenting the history of reading in Britain from 1450 to 1945. Evidence comes from published and unpublished sources such as diaries, commonplace books, memoirs, sociological surveys, and criminal court and prison records.



Combine with Novels Reviewed Database



Also https://vls.english.qmul.ac.uk/ Dissenting Libraries Online

To find out more about the reading habits of individual borrowers, click on Browse borrowers. Explore the borrowing records of tutors, such as the Baptist Frederick W. Gotch, ministerial students, including Robert Cotton Mather (later a Congregational missionary), and their lay counterparts, such as William Rayner Wood (who became a prominent Unitarian businessman). 

The most frequently borrowed books include periodicals, theological textbooks, and historical works. Click on the links to see lists of the most popular titles at Manchester College, Homerton Academy, or Bristol Baptist Academy.



## ch 4 - networks ##



Chapter four introduces my second major experiment, a mapping of the social world of print production 1789-99. As in chapter two, it will be a substantial technical and research project simply to recover contemporary printing practices; this time, rather than asking what was printed, I will ask who it was printed by. A great deal of scholarly work[ TK: Jon Mee, Kevin Gilmartin and Paul Keen are others who would be important here. Plus scholars who focus more on conservatism, perhaps M. O. Grenby for example? Or even much earlier work by Marilyn Butler?] already exists on printing circles, coterie publishing, and individual publishing houses.[^cf3] My project will consult this scholarship to extract and encode connections between authors, printers, and publishers (but not patrons, readers, or other persons not immediately involved in the production of texts) in order to synthesize the implicit social networks underlying 1790s print production. I will begin my research for this chapter by encoding only a few existing studies, in order to evaluate the feasibility of my method at scale. It is possible that, rather than directly consulting the more richly historically-informed work of other scholars, I will instead fall back on inferring networks from the author and publisher metadata included with the corpora examined in chapters two and three. The resulting chapter will explain my methodology and its assumptions, and will provide a rich description of my resulting network graph. The graph I create may reveal one large interconnected network, or several separate networks of varying sizes; these networks may consist of highly distinct clusters, or evenly interconnected webs. Drawing on mathematical graph theory, the chapter will explain the implications of whichever shape the network ultimately displays. It will also present an overview of the people I identify as the “major players” in the publishing world of the 1790s, both mathematically (looking for nodes with various kinds of centrality) and in the scholarship.



### British Book Trade Index ###



OBVIOUSLY this work should be built on the back of the British Book Trade Index, I can’t BELIEVE nobody told me about it!!



http://bbti.bodleian.ox.ac.uk/#

https://www.nls.uk/catalogues/scottish-book-trade-index



## ch 5 - networks popularity ##



Having recaptured these complex networks in some depth, I can then examine them, in chapter five, for their relation to our current understanding of mainstream and radical — or as I am terming them “mainstream” and “non-mainstream” — printing circles. My network graphs will model individual political affiliation as a complex, socially defined practice rather than a taxonomy of concrete and unchanging ideological stances.[ TK: Excellent point, especially in these fast-changing years. But again, this looks like potentially very daunting. Stable binaries are so much more convenient for scholars to work with! I’m excited to see what you come up with here.] This chapter will look for traces of affiliation in the print practices of publishers and of authors. I will consider individual printers with political allegiances, as in Dissenting societies, radical publishers, correspondence societies. This will then enable me to consider authors’ strategic choices as they publish with different printers[ TK: Again presumably you mean publishers not printers? NB too that the choice could work the other way round: authors for hire being commissioned by publishers to write something suitable for a list. I don’t know much about the Minerva Press, but I imagine that’s the way this kind of publisher would have operated, at least in part.]. Having identified radical elements in the publishing world, I will interrogate the radicals’ claims to marginalization. I suspect that I might find that they were not as socially estranged from the mainstream as they describe themselves, and that their printed works may accordingly have been less marginal. I will discuss alternative print markets and alternative circulation, and what kind of “alternatives” they offer to the mainstream. The circulation of works in manuscript presents me two challenges which will be discussed here. The first challenge is methodological: the circulation of manuscripts clearly occurred, and may have constituted “publication” within social circles, but manuscripts fall outside my purview[ TK: Yes, goodness, yes! You can deal with this via a brief discussion of recent scholarship on the persistence of manuscript culture and association practices e.g. Betty Schellenberg, Aileen Douglas, Michelle Levy, I would have thought.]. This chapter will therefore discuss the nature and rough shape of the gap which the exclusion of manuscript works leaves in my study. The second task of this chapter is more theoretical: as queer and decolonial DH scholars note, there is an ethical choice implicated in the decision to systematically discover, collect, and expose communities which intentionally operated below the notice of state observation. Historical distance prevents me from worrying about causing direct harm through my work, but nonetheless I will critically interrogate my own research practices and contextualize my choices within the horizon of expectations of the radical circles I (and other scholars) expose. Finally, having discussed the networks of radical and mainstream publishing in the 1790s, I will also compare the position of radical publishers in the 1790s with their status in the corpora discussed in chapters two and three (where they may in fact be marginalized; I expect to find conservative works overrepresented in the corpora). Together, these approaches will further complicate the story of popularity which the dissertation challenges elsewhere, by suggesting ways to reassess of the popularity of radical works.



## coda? - gothic ##



A potential coda or afterword could build on the work of Robert Miles and others to describe the role of the Gothic as a trans-generic mode which can appear across all print production (assuming that turns out to be true, of course.) Some of my earlier work suggests that Gothic modes of writing, unlike most literary content, can be “spotted” computationally. Since the Gothic operates by means of distinctive tropes and sensory appeals, the Gothic parts of a history and the Gothic parts of a picaresque can be distinguished from the non-Gothic parts of each by computational methods that could not distinguish a history from a picaresque. (Importantly, stylometric methods are not able to distinguish a parody of the Gothic from a “real” Gothic; as I theorize and interpret my findings, then, I would take up Horner and Zlosnik’s work on Gothic humour to discuss the problem of parody in taxonomy.) This final section could use a stylometric approach to identify and then search for “Gothic vocabularies” in full texts, computationally, in order to quantify the reach of the Gothic across my corpora. How many works can be identified as having Gothic influences? What kinds of literary production are most resistant to the Gothic? Does the Gothic appear differently in mainstream vs radical presses? This afterword would sketch out a preliminary map of the Gothic in the print world of the 1790s. This closing section would thus cite and build upon my prior work with the Gothic, in the context of the 1790s as a period when the penetration of Gothic modes into mainstream print had particularly complex political stakes.



## Works Cited ##



But wait, I want to use LaTeX or some other citation manager for this.

Command-shift-C will call up the Papers citation tool.

\cite{Scheuermann:2001tc}

How can I use this to cite specific page numbers?



# Acknowledgements #



SSHRC (OGS?)

ESTC, HathiTrust, U Toronto Libraries (for ECCO metadata)

Alex G, Terry, Tom

Cai, Ashley

Alex + Austin, Alyssa, Jakob, and all the other “civilians”/“innocent bystanders”

Alex StrickVL?? Beeminder? 

OBNS



# Experimental methods #



## ECCO MARC records ##



001 stores ESTC number, though without leading numbers

i.e., =001  N836 (MARC) correlates to ESTC Number:N000836 (online)



260 c stores publication year

i.e., =260 […] $c (MARC) correlates to Imprint:[…] 1733 (online)



## Early Novels Database ##



So while the full.tsv contains records for works published as early as 1660 and as late as 1853, you can choose the 18c-full.tsv to look only at records published from 1700-1799, and the 19c-full.tsv for records with publication dates from 1800-1853.



About the Dataset

The Early Novels Dataset contains bibliographic metadata for early works of fiction held in the Collection of British and American Fiction, 1660-1830 (CBAF) at the University of Pennsylvania’s Kislak Center for Special Collections, Rare Books and Manuscripts, as well as other regional repositories. It consists of MARC catalog records enriched with custom subfields designed to offer new kinds of structured data about early fiction in English.



The END dataset is comprised of high-quality, human-generated metadata that captures a much fuller range of edition- and copy-specific information about early novels than traditional library catalog records. The END metadata schema builds on library-standard MARC records with custom-designed subfields that use both controlled and discursive vocabularies to describe a range of bibliographic features outside the scope of traditional cataloging. These include important bibliographic details such as authority statements, full and half title, accurate and controlled place of publication, and edition statement. They capture both copy-specific information about marginalia, inscriptions, and bookplates as well as title-level data on narrative form. And finally, they record the presence of important paratextual features like authors’ notes, epigraphs, footnotes, and indices, which can be found in many works of early fiction but have never been cataloged in a systematic way that would enable faceted search across a corpus.



As of September 2017, the complete Early Novels Dataset totals 2,041 records. The core eighteenth-century subset consists of 1,325 records, which represent all of Penn Libraries’ Collection of British and American Fiction holdings published from 1700-1794 and a sampling of holdings published from 1795-1799. A sample comparison of the CBAF holdings from the decade of the 1760s with all known fiction in English published during this period suggests that Penn's collection represents approximately 14% of this total corpus. In the core eighteenth-century subset, Penn's holdings are supplemented with selected holdings from other Philadelphia-area and regional repositories, including the Library Company of Philadelphia, the Rosenbach, the Swarthmore Libraries Rare Book Room, Bryn Mawr College Special Collections, and New York University's Fales Library.



Pair END Data with Fulltext for Topic Modeling

While END’s primary focus is metadata, we are also in the preliminary stages of a fulltext initiative for the CBAF novels digitized by Penn Libraries and available through Print at Penn. We have created fulltext files for each of these texts using OCR; cleanup work is ongoing, both computationally and through hand-correcting. The fulltext is available in our digital-collection repostiory. We have also worked with Penn Libraries' Digital Humanities Specialist Scott Enderle to experiment with topic modeling of this fulltext combined with END metadata. Work-in-progress can be found in our earlynovels-topic-model repository, and Scott's enhanced Topic Modeling Tool, which enables pairing fulltext with metadata, can be found here.

[^cf1]: Although all of these elements interest me, and I anticipate that attention to this decade will reveal their prominence, I seek to avoid framing my inquiry explicitly around them and thus begging the question of their importance.

[^cf2]: Although all of these elements interest me, and I anticipate that attention to this decade will reveal their prominence, I seek to avoid framing my inquiry explicitly around them and thus begging the question of their importance.

[^cf3]: Per Terry’s suggestions, I would likely begin here with Jon Klancher, The Making of English Reading Audiences, 1790-1832; Marcus Wood, Radical Satire and Print Culture, 1790-1822; and David Worrall, Radical Culture: Discourse, Resistance, and Surveillance, 1790-1820. Other promising titles include Social networks in the long eighteenth century : clubs, literary salons, textual coteries, ed. Ileana Baird; and The enlightenment & the book : Scottish authors & their publishers in eighteenth-century Britain, Ireland & America, by Richard B. Sher, to capture different parts of the publishing landscape.