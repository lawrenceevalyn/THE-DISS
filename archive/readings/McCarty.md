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