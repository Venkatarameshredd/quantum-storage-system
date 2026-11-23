========================================================================
IEEE CONFERENCE PAPER OVERLEAF SUBMISSION PACKAGE
========================================================================

Title: Adaptive Hybrid Post-Quantum Cloud Storage with Zero-Trust Key Splitting 
       and Network-Aware Handshake Optimization
Authors: Varsha Sambhaje (Corresponding Author) and Madhira Venkata Ramesh Reddy (Co-Author)
Affiliation: Department of Computer Science, SRM University, Amaravati, 52240, Andhra pradesh, India

FILES INCLUDED IN THIS ARCHIVE:
- IEEE_CONFERENCE_PAPER.tex : Main LaTeX manuscript in IEEEtran conference format
- IEEE_CONFERENCE_PAPER.bib : BibTeX reference database
- fig_roadmap.png           : Fig. 1 Roadmap diagram
- fig1.png                  : Fig. 4 High-Level System Architecture
- fig2.png                  : Fig. 2 AEDE Decision Engine Flowchart
- fig3.png                  : Fig. 5 Dual-Key Hybrid KEM & HKDF Expansion
- fig4.png                  : Fig. 3 Zero-Trust Shamir (2-of-3) Key Distribution
- fig5.png                  : Fig. 6 Secure Ingress/Egress Pipelines with Outer HMAC
- fig6.png                  : Fig. 7 Cryptographic Hash-Chain Audit Logging
- fig8.png                  : Fig. 8 Micro-architectural NTT and Energy Dynamics
- fig7.png                  : Fig. 9 Empirical Performance Benchmarks & DoS Mitigation
- fig9.png                  : Fig. 10 Transport-layer TCP Framing & Retransmissions

HOW TO COMPILE ON OVERLEAF:
1. Log in to Overleaf (https://www.overleaf.com).
2. Click 'New Project' -> 'Upload Project'.
3. Select this zip file ('IEEE_Conference_Paper_Overleaf.zip').
4. Set the compiler to 'pdfLaTeX' and main document to 'IEEE_CONFERENCE_PAPER.tex'.
5. Click 'Recompile'.

HOW TO COMPILE LOCALLY:
pdflatex IEEE_CONFERENCE_PAPER.tex
bibtex IEEE_CONFERENCE_PAPER
pdflatex IEEE_CONFERENCE_PAPER.tex
pdflatex IEEE_CONFERENCE_PAPER.tex
========================================================================
