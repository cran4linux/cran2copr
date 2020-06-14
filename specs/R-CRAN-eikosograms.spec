%global packname  eikosograms
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          The Picture of Probability

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-grid 
Requires:         R-CRAN-plyr 
Requires:         R-grid 

%description
An eikosogram (ancient Greek for probability picture) divides the unit
square into rectangular regions whose areas, sides, and widths, represent
various probabilities associated with the values of one or more
categorical variates. Rectangle areas are joint probabilities, widths are
always marginal (though possibly joint margins, i.e. marginal joint
distributions of two or more variates), and heights of rectangles are
always conditional probabilities. Eikosograms embed the rules of
probability and are useful for introducing elementary probability theory,
including axioms, marginal, conditional, and joint probabilities, and
their relationships (including Bayes theorem as a completely trivial
consequence). They are markedly superior to Venn diagrams for this
purpose, especially in distinguishing probabilistic independence, mutually
exclusive events, coincident events, and associations. They also are
useful for identifying and understanding conditional independence
structure. As data analysis tools, eikosograms display categorical data in
a manner similar to Mosaic plots, especially when only two variates are
involved (the only case in which they are essentially identical, though
eikosograms purposely disallow spacing between rectangles). Unlike Mosaic
plots, eikosograms do not alternate axes as each new categorical variate
(beyond two) is introduced. Instead, only one categorical variate,
designated the "response", presents on the vertical axis and all others,
designated the "conditioning" variates, appear on the horizontal. In this
way, conditional probability appears only as height and marginal
probabilities as widths. The eikosogram is therefore much better suited to
a response model analysis (e.g. logistic model) than is a Mosaic plot.
Mosaic plots are better suited to log-linear style modelling as in
discrete multivariate analysis. Of course, eikosograms are also suited to
discrete multivariate analysis with each variate in turn appearing as the
response. This makes it better suited than Mosaic plots to discrete
graphical models based on conditional independence graphs (i.e. "Bayesian
Networks" or "BayesNets"). The eikosogram and its superiority to Venn
diagrams in teaching probability is described in W.H. Cherry and R.W.
Oldford (2003)
<https://math.uwaterloo.ca/~rwoldfor/papers/eikosograms/paper.pdf>, its
value in exploring conditional independence structure and relation to
graphical and log-linear models is described in R.W. Oldford (2003)
<https://math.uwaterloo.ca/~rwoldfor/papers/eikosograms/independence/paper.pdf>,
and a number of problems, puzzles, and paradoxes that are easily explained
with eikosograms are given in R.W. Oldford (2003)
<https://math.uwaterloo.ca/~rwoldfor/papers/eikosograms/examples/paper.pdf>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
