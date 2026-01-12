%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eikosograms
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing Probabilities, Frequencies, and Conditional Independence for Categorical Variates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-stats 
Requires:         R-grid 
Requires:         R-stats 

%description
An eikosogram (ancient Greek for probability picture) divides the unit
square into rectangular regions whose areas, sides, and widths represent
various probabilities associated with the values of one or more
categorical variates. Rectangle areas are joint probabilities, widths are
always marginal (though possibly joint margins, i.e. marginal joint
distributions of two or more variates), and heights of rectangles are
always conditional probabilities. Eikosograms embed the rules of
probability and are useful for introducing elementary probability theory,
including axioms, marginal, conditional, and joint probabilities, and
their relationships (including Bayes' theorem as a completely trivial
consequence). They provide advantages over Venn diagrams for this purpose,
particularly in distinguishing probabilistic independence, mutually
exclusive events, coincident events, and associations. They also are
useful for identifying and understanding conditional independence
structure. Eikosograms can be thought of as mosaic plots when only two
categorical variates are involved; the layout is quite different when
there are more than two variates. Only one categorical variate, designated
the "response", presents on the vertical axis and all others, designated
the "conditioning" variates, appear on the horizontal. In this way,
conditional probability appears only as height and marginal probabilities
as widths. The eikosogram is ideal for response models (e.g. logistic
models) but equally useful when no variate is distinguished as the
response. In such cases, each variate can appear in turn as the response,
which is handy for assessing conditional independence in discrete
graphical models (i.e. "Bayesian networks" or "BayesNets"). The eikosogram
and its value over Venn diagrams in teaching probability is described in
W.H. Cherry and R.W. Oldford (2003)
<https://math.uwaterloo.ca/~rwoldfor/papers/eikosograms/paper.pdf>, its
value in exploring conditional independence structure and relation to
graphical and log-linear models is described in R.W. Oldford (2003)
<https://math.uwaterloo.ca/~rwoldfor/papers/eikosograms/independence/paper.pdf>,
and a number of problems, puzzles, and paradoxes that are easily explained
with eikosograms are given in R.W. Oldford (2003)
<https://math.uwaterloo.ca/~rwoldfor/papers/eikosograms/examples/paper.pdf>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
