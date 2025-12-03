Title: The Quantum You Want
Slug: quantum-you-want
Category: Thoughts
Date: 2025-09-17
Summary: A clear, accessible explanation of why quantum computing represents a fundamentally different approach to computation and where its most significant early impacts are likely to occur.

{% newthought "Throughout our history, humanity has striven to predict the future." %} From astrology and crystal balls to modern science, we look for an edge in what is to come. Consider the weather, something we often discuss even with strangers. Your smartphone likely has one or more apps that will tell you whether it will be cloudy or sunny today, or if storms are coming. While we often focus on the veracity—or lack thereof—of these predictions, perhaps a more important observation is the power of the device itself.

We rarely dwell on it, but your smartphone would rival the top supercomputers in the world from the turn of the century. And while few predicted the incredible power we now carry in a pocket or purse, both smartphones and supercomputers function in a similar manner. Data from the world around us—whether temperature measurements, texts, music playlists, or YouTube videos—are converted into long streams of zeros and ones, then processed by computer chips that follow deterministic rules.

This highlights an important point. Despite the historical obsession, humanity is still bad at making predictions. A good summary of this state of affairs comes from Bill Gates, who in 1996 wrote:{% sidenote "sn-gates" "Bill Gates, *The Road Ahead*, Afterword, p. 316, Penguin Books, 1996" %}

> People often overestimate what will happen in the next two years and underestimate what will happen in ten. I'm guilty of this myself.

Of course, this prediction paradox applies perfectly to computing. Today's top supercomputers are roughly a million times more powerful than your smartphone. Yet even these behemoths are often unable to predict the weather a few days out. As Mick Jagger eloquently sang, "You can't always get what you want."{% sidenote "sn-stones" "But as the song continues, [you get what you need](https://music.apple.com/us/song/you-cant-always-get-what-you-want-remastered-2019/1500643065)." %}

## The Computing You Want

While some might argue for better algorithms or new hardware designs, we may simply need an entirely different approach—one first postulated by Nobel prize-winning physicist Richard Feynman. At a conference on computers in physics in 1981, he introduced the concept of using quantum mechanical systems for computation, famously stating:{% sidenote "sn-feynman" "For more information, you can [read the paper](https://link.springer.com/article/10.1007/BF02650179) he submitted following the conference." %}

> Nature isn't classical, dammit, and if you want to make a simulation of nature, you'd better make it quantum mechanical.

Now Feynman was generally referring to simulations of molecules and materials that involve fundamental physics or chemistry, rather than the weather. But this charge helped spur others to explore this new idea. And now, over four decades later, we are at the cusp of a new revolution in computing, one based on the principles of quantum mechanics. For many, any exposure to the quantum world and the probabilistic nature it embodies can end in confusion. For example, in the classical world, you can know both where a car is located and how fast it is traveling. But in the quantum realm, knowing one of these, either position or velocity, means we can't precisely know the other. This isn't due to any fault in how we measure them, but is instead a fundamental property of nature described by the Heisenberg Uncertainty Principle.{% sidenote "sn-heisenberg" "[A remarkably simple yet profound result](https://en.wikipedia.org/wiki/Uncertainty_principle), first shown in 1927 by the Nobel prize-winning physicist Werner Heisenberg. More formally, there is an inherent limitation in how well we can know the product of the position and momentum of a particle. This uncertainty becomes important when dealing with fundamental particles of nature like the electron or proton." %}

Thus, it is unsurprising that quantum computers are not as easy to build, use, or understand as your smartphone. Classical computers work with bits that are either zero or one—on or off. Quantum computers are based on quantum bits, or qubits, which, being quantum mechanical, have some surprising behaviors. The two most relevant for our discussion are superposition and entanglement.

**Superposition** means that a qubit can be in multiple states at once, like a coin that is simultaneously both heads and tails, until you observe it. In contrast, a classical bit is like a coin that has already landed: it's either heads or tails, but never both. While this phenomenon may seem abstract, combining multiple qubits causes the power of superposition to grow exponentially: two qubits can exist in four possible states, ten qubits in over a thousand, and twenty qubits in over a million. Through superposition, quantum computers can encode and manipulate many possible states simultaneously within the same system.

On its own, this provides unique avenues to reinvent computation. However, that's only part of the story. The second quantum property—**entanglement**—means that qubits can become deeply linked, such that knowing something about one instantly reveals information about the other, even if they're far apart.{% sidenote "sn-einstein" "If this seems troubling, you are in good company. [Einstein referred to this process](https://www.technologyreview.com/2012/03/08/20152/einsteins-spooky-action-at-a-distance-paradox-older-than-thought/) as spooky action at a distance." %} Imagine we each flip a pair of entangled coins. If I look at mine, we instantly know what yours shows without having to look. This idea, combined with sufficiently clever algorithms, allows many entangled qubits to be processed simultaneously. As a result, we can navigate what was once an intractably complex landscape to reach the desired endpoint with incredible speed.

## The Quantum You Find

This promise has driven large companies like IBM, Microsoft, and Google, as well as smaller players such as D-Wave, IonQ, and PsiQuantum, to explore different qubit architectures and to construct and deploy multi-qubit systems. Yet the physical challenges of building and operating quantum systems, especially at the scales needed for real-world problems, remain an unsolved challenge. Simply put, quantum systems lack the commodity approach of classical systems that rely on semiconductors—each company building in this space seems to have a different approach.

Despite these challenges, the development of quantum algorithms has not stopped, allowing us to predict where quantum computers will have the biggest initial impact. And, spoiler alert, it won't be running Excel or watching YouTube. Instead, quantum systems should excel at these four tasks:

**Finding needles in a haystack:** Quantum computers can quickly search through large data sets to find targets, which can be useful for database searching and pattern matching.

**Solving optimization problems:** Quantum computers can identify the optimal solution out of a very large number of possibilities, which is useful in supply chain logistics and financial modeling.

**Cryptography:** Quantum computers can quickly break traditional encryption standards, which threatens global communication and financial transactions. Fortunately, quantum computing also offers new approaches that are immune to these threats.

**Simulating Nature:** At its core, nature follows the rules of quantum mechanics, thus quantum computing, as envisioned by Feynman, can naturally simulate molecules, chemical reactions, and material properties. This could lead to the development of personalized medicines and tailored materials that outperform existing options.

## When Will Quantum Arrive?

So the million-dollar question is when will a quantum computer be available? Many industry experts predict the first working, general-purpose quantum computer—known as Q-Day—will arrive within five or ten years.{% sidenote "sn-qday" "After raising the difficulty in making predictions I hesitate to do so here. So I simply leverage AI to [company](https://www.ibm.com/quantum/blog/large-scale-ftqc), [expert](https://globalriskinstitute.org/publication/briefing-note-recent-updates-on-quantum-timeline/), and [consultancy](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-year-of-quantum-from-concept-to-reality-in-2025) predictions." %} While that may seem optimistic, it is also prudent to recall Gates's quote. Maybe you will soon know unambiguously whether to pack that umbrella or not!

---

Originally published by the [Gies College of Business](https://giesbusiness.illinois.edu/news/2025/10/16/the-quantum-you-want--qubits--forecasts--and-the-next-tech-revolution) on October 16, 2025.
