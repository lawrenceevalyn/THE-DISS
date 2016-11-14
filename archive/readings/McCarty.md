# Modeling: A Study in Words and Meaning

## Introduction

practice varies from person to person, from project to project, and ways of construing it perhaps vary even more. In this chapter I argue for modeling as a model of such a practice.

I have three confluent goals: to identify humanities computing with an intellectual ground shared by the older disciplines, so that we may say how and to what extent our field is of as well as in the humanities, how it draws from and adds to them; at the same time to reflect experience with computers "in the wild"; and to aim at the most challenging problems, and so the most intellectually rewarding future now imaginable.

My primary concern here is, as Confucius almost said, that we *use the correct word* for the activity we share lest our practice go awry for want of understanding 

## Background

By "modeling" I mean the heuristic process of constructing and manipulating models', a "model" I take to be either a representation of something for purposes of study, or a design for realizing something new. These two senses follow Clifford Geertz's analytic distinction between a denotative "model of" such as a grammar describing the features of a language, and an exemplary "model for" such as an architectural plan

Since modeling is fundamentally relational, the same object may in different contexts play either role: thus, e.g., the grammar may function prescriptively, as a model for correct usage, the architectural plan descriptively, as a model of an existing style. The distinction also reaches its vanishing point in the convergent purposes of modeling: the model of exists to tell us that we do not know, the model for to give us what we do not yet have. Models realize.

"To an observer B, an object A* is a model of an object A to the extent that B can use A* to answer questions that interest him about A" (Minsky 1995). ... A strong temptation for us here is to dismiss the residual alienness of Minsky's formulation and to accept, as we have accepted computing, the reified, explicit "model" of Minsky's definition as what we really have been doing all along. This would, however, be a serious error. 

Two effects of computing make the distinction between "idea" or other sort of mental construct on the one hand, and on the other "model" in the sense we require: first, the demand for computational tractability, i.e., for complete explicitness and absolute consistency; second, the manipulability that a computational representation provides.

The first effects a sea-change by forcing us to confront the radical difference between what we know and what we can specify computationally, leading to the epistemological question of how we know what we know. Computational form, which accepts only that which can be told explicitly and precisely, is thus radically inadequate for representing the full range of knowledge – hence useful for isolating the tacit or inchoate kinds. On the other hand, we need to trust what we somehow know, at least provisionally, in order not to lose all that goes without saying or cannot be said in computational form.

Gradually, however, **through perfective iteration trivial error is replaced by meaningful surprise**. There are in general two ways in which a model may violate expectations and so surprise us: either by a success we cannot explain, e.g., finding an occurrence where it should not be; or by a likewise inexplicable failure, e.g., not finding one where it is otherwise clearly present. In both cases modeling problematizes. **As a tool of research, then, modeling succeeds intellectually when it results in failure**, either directly within the model itself or indirectly through ideas it shows to be inadequate.

The second quality of "model" that distinguishes it from "idea" is manipulability... In other words, computational models, however finely perfected, are better understood as temporary states in a process of coming to know rather than fixed structures of knowledge.

For the moment and the foreseeable future, then, computers are essentially modeling machines, not knowledge jukeboxes. To think of them as the latter is profoundly to misunderstand human knowledge – and so to constrict it to the narrow scope of the achievably mechanical.

## Learned Complaints

We require a close and careful look at the semantic fields of all major alternatives, including "map", for their disjunctions and overlaps. We need to scrutinize each of these, asking what does it denote and connote that the others do not, and vice versa? What do all have in common? What are their individual tendencies of mind, and which of these best suits computing as we are learning to conceive it?

## Philological Analysis of Related Terms

To answer the learned criticisms and further clarify our topic, however, I propose to question it by comparison against the major alternatives: "analogy", "representation", "diagram", "map", "simulation", and "experiment." As we have seen, the two decisive criteria are that the thing named by the chosen term be computationally tractable and manipulable. Tractability in turn requires complete explicitness and absolute consistency; manipulability resolves into mechanical action and interactivity. Hence the term must denote a continual process of coming to know, not an achievement but an approximation.

For each of the alternative terms I ask whether and to what degree the word normally denotes a dynamic process and whether it refers to a concrete, i.e. manipulable, form – the requirements of anything whose function is fulfilled through being changed.

(This section is quite long!)

## Conclusion

Why do we need an answer to this question? Because, I have argued, ours is an experimental practice, using equipment and instantiating definite methods, for the skilled application of which we need to know what we are doing as well as it can be known. I have labeled the core of this practice "modeling", and suggested how, properly understood, modeling points the way to a computing that is of as well as in the humanities: a continual process of coming to know by manipulating representations. We are, I have suggested, in good epistemological company. But this only sharpens the epistemological question. The signified of modeling vanishes into the murk because we lack a disciplined way of talking about it. Methods are explicit, actions definite, results forthcoming, yet we have been unable fully and persuasively to articulate the intellectual case for the means by which these results are produced. Hence the just-a-tool status of computing, the not-a-discipline slur, the tradesman's entrance or other back door into the academy. No one doubts the usefulness of the practice. Rather it's the intellection of praxis to which the next stage in the argument I have begun here must turn.

# ‘Knowing true things by what their mockeries be’: Modelling in the Humanities

## Introduction
Gardin refers to “simulation”, Frye to “modelling”. Both of these rather ill-defined terms share a common epistemological sense: use of a likeness to gain knowledge of its original. We can see immediately why computing should be spoken of in these terms, as it represents knowledge of things in manipulable form, and thus allows us to simulate or model these things. Beyond the commonsense understanding, however, we run into serious problems of definition and so must seek help.

My intention here is to summarize the available help, chiefly from the history and philosophy of the natural sciences, especially physics, where much of the relevant work is to be found.[1] I concentrate on the term “modelling” because that is the predominate term in scientific practice -- but it is also, perhaps even by nature, the term around which meanings I find the most useful tend to cluster. I will then give an extended example from humanities computing and discuss the epistemological implications. Finally I will return to Jean-Claude Gardin's very different agenda, what he calls “the logicist programme”, and to closely allied questions of knowledge representation in artificial intelligence.


## Modelling

The most basic distinction is, in Clifford Geertz's terms, between “an ‘of’ sense and a ‘for’ sense” of modelling (1973: 93). A model of something is an exploratory device, a more or less “poor substitute” for the real thing (Groenewold 1960: 98). We build such models-of because the object of study is inaccessible or intractable, like poetry or subatomic whatever-they-are. In contrast a model for something is a design, exemplary ideal, archetype or other guiding preconception. Thus we construct a model of an airplane in order to see how it works; we design a model for an airplane to guide its construction. A crucial point is that both kinds are imagined, the former out of a pre-existing reality, the latter into a world that doesn't yet exist, as a plan for its realization.

A fundamental principle for modelling-of is the exact correspondence between model and object with respect to the webs of relationships among the selected elements in each. Nevertheless, such isomorphism (as it is called) may be violated deliberately in order to study the consequences.

Theoretical modelling, constrained only by language, is apt to slip from a consciously makeshift, heuristic approximation to hypothesized reality. Black notes that in such “existential use of modelling” the researcher works “through and by means of” a model to produce a formulation of the world as it actually is (1962: 228f). In other words, a theoretical model can blur into a theory. But our thinking will be muddled unless we keep “theory” and “model” distinct as concepts. Shanin notes that modelling may be useful, appropriate, stimulating and significant -- but by definition never true (1972: 11).

Since modelling is pragmatic, the worth of a model must be judged by its fruitfulness. The principle of isomorphism means, however, that for a model-of, this fruitfulness is meaningful in proportion to the “goodness of the fit” between model and original

a good model can be fruitful in two ways: either by fulfilling our expectations, and so strengthening its theoretical basis, or by violating them, and so bringing that basis into question. I argue that from the research perspective of the model, in the context of the humanities, failure to give us what we expect is by far the more important result, however unwelcome surprises may be to granting agencies.

 Driven as we are by the epistemological imperative, to know; constrained (as in Plato's cave or before St Paul's enigmatic mirror) to know only poor simulacra of an unreachable reality -- but aware somehow that they are shadows of something -- our faith is that as the shadowing (or call it modelling) gets better, it approaches the metaphorical discourse of the poets. If we are on the right track, as Max Black says at the end of his essay, “some interesting consequences follow for the relations between the sciences and the humanities”, namely their convergence (1962: 242f). ... I would argue that the humanities really must meet the sciences half-way, on this commons, and that we have in humanities computing a means to do so.

## In humanities computing: an example

markup comes into focus as a kind of epistemological modelling -- not merely the industrial matter of preparing a text for scholarship, or whatever, but itself a new form of scholarship

Before the encoding begins (at least logically before) we have a theoretical model of personification -- let us call it T -- suitable to the poem. T assumes a conventional scala naturae, or what Lovejoy taught us to call “the great chain of being”, in small steps or links from inanimate matter to humanity. In response to the demands of the Metamorphoses personification is defined within T as any shift up the chain to or toward the human state. Thus T focuses, unusually, on ontological change per se, not achievement of a recognizable human form. T incorporates the Bloomfield hypothesis but says nothing more specific about how any such shift is marked. With T in mind, then, we build a model by tagging personifications according to the linguistic factors that affect their poetic ontology.

Heuristic modelling rationalizes the ill-defined notion of context into a set of provisional but exactly specified factors through a recursive cycle.  It goes like this. Entity X seems to be personified; we identify factors A, B and C provisionally; we then encounter entity Y, which seems not to qualify even though it has A, B and C; we return to X to find previously overlooked factor D; elsewhere entity Z is personified but has only factors B and D, so A and C are provisionally downgraded or set aside; and so on. The process thus gradually converges on a more or less stable grammar or phenomenology of personification. This grammar is a model according to the classical criteria: it is representational, fictional, tractable and pragmatic. It is a computational model because the encoding that comprises it obeys two fundamental rules: total explicitness and absolute consistency. Thus everything to be modelled must be explicitly represented, and it must be represented in exactly the same way every time.

With such a model we can then engage in the second-order modelling of these data by adjusting the factors and their weightings, producing different results and raising new questions. The model can be exported to other texts, tried out on them in a new round of recursive modelling, with the aim of producing a more inclusive model, or a better questions about personification from which a better model may be constructed. This is really the normal course of modelling in the sciences as well: the working model begins to converge on the theoretical model.

The failures of the model -- the anomalous cases only special pleading would admit -- are the leaks that reflect questioningly back on the theoretical model of the Metamorphoses and so challenge fundamental research.

## Experimental practice

1) experiment is an epistemological practice of its own, related to but not dependent on theory; and (2) experiment is not simply heuristic but, in the words the literary critic Jerome McGann borrowed famously from Lisa Samuels, is directed to “imagining what we don't know” (2001: 105ff), i.e. to making new knowledge. This is the face that modelling turns to the future, that which I have called the “model-for”, but which must be understood in Hacking's interventionist sense.

Hacking argues that we make hypothetical things real by learning how to manipulate them; thus we model-for them existentially 

in what sense are the hypothetical things of the humanities realized? ... Ontologically where do such entities fit between the reality of the object on the one hand and the fiction of the theoretical model on the other?

Models-for do not have to be such conscious things. They can be the serendipitous outcome of play or of accident.

## Knowledge representation & the logicist programme

The conception of modelling I have developed here on the basis of practice in the physical sciences gives us a crude but useful machine with its crude but useful tools and a robust if theoretically unattached epistemology. It assumes a transcendent, imperfectly accessible reality for the artefacts we study, recognizes the central role of tacit knowledge in humanistic ways of knowing them and, while giving us unprecedented means for systematizing these ways, is pragmatically anti-realist about them. Its fruits are manipulatory control of the modelled data and, by reducing the reducible to mechanical form, identification of new horizons for research.

But dangerous to us only if we miss the lesson of modelling and mistake the artificial for the real. ... We must beware that we do not pervert our wheels of logic into “symbols of objective mastery” over ourselves but use them to identify what they cannot compute. Their failures and every other well-crafted error we make are exactly the point, so that (now to quote the Bard precisely) we indeed are “Minding true things by what their mock'ries be” (Henry V iv.53).