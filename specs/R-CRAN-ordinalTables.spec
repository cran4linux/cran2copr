%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ordinalTables
%global packver   1.0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Models to Two-Way Tables with Correlated Ordered Response Categories

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
Fit a variety of models to two-way tables with ordered categories. Most of
the models are appropriate to apply to tables of that have correlated
ordered response categories.  There is a particular interest in rater data
and models for rescore tables. Some utility functions (e.g., Cohen's kappa
and weighted kappa) support more general work on rater agreement. Because
the names of the models are very similar, the functions that implement
them are organized by last name of the primary author of the article or
book that suggested the model, with the name of the function beginning
with that author's name and an underscore.  This may make some models more
difficult to locate if one doesn't have the original sources.  The
vignettes and tests can help to locate models of interest.  For more
dertaiils see the following references: Agresti, A. (1983)
<doi:10.1016/0167-7152(83)90051-2> "A Simple Diagonals-Parameter Symmetry
And Quasi-Symmetry Model", Agrestim A. (1983) <doi:10.2307/2531022>
"Testing Marginal Homogeneity for Ordinal Categorical Variables", Agresti,
A. (1988) <doi:10.2307/2531866> "A Model For Agreement Between Ratings On
An Ordinal Scale", Agresti, A. (1989) <doi:10.1016/0167-7152(89)90104-1>
"An Agreement Model With Kappa As Parameter", Agresti, A. (2010
ISBN:978-0470082898) "Analysis Of Ordinal Categorical Data", Bhapkar, V.
P. (1966) <doi:10.1080/01621459.1966.10502021> "A Note On The Equivalence
Of Two Test Criteria For Hypotheses In Categorical Data", Bhapkar, V. P.
(1979) <doi:10.2307/2530344> "On Tests Of Marginal Symmetry And
Quasi-Symmetry In Two And Three-Dimensional Contingency Tables", Bowker,
A. H. (1948) <doi:10.2307/2280710> "A Test For Symmetry In Contingency
Tables", Clayton, D. G. (1974) <doi:10.2307/2335638> "Some Odds Ratio
Statistics For The Analysis Of Ordered Categorical Data", Cliff, N. (1993)
<doi:10.1037/0033-2909.114.3.494> "Dominance Statistics: Ordinal Analyses
To Answer Ordinal Questions", Cliff, N. (1996 ISBN:978-0805813333)
"Ordinal Methods For Behavioral Data Analysis", Goodman, L. A. (1979)
<doi:10.1080/01621459.1979.10481650> "Simple Models For The Analysis Of
Association In Cross-Classifications Having Ordered Categories", Goodman,
L. A. (1979) <doi:10.2307/2335159> "Multiplicative Models For Square
Contingency Tables With Ordered Categories", Ireland, C. T., Ku, H. H., &
Kullback, S. (1969) <doi:10.2307/2286071> "Symmetry And Marginal
Homogeneity Of An r × r Contingency Table", Ishi-kuntz, M. (1994
ISBN:978-0803943766) "Ordinal Log-linear Models", McCullah, P. (1977)
<doi:10.2307/2345320> "A Logistic Model For Paired Comparisons With
Ordered Categorical Data", McCullagh, P. (1978) <doi:10.2307/2335224> A
Class Of Parametric Models For The Analysis Of Square Contingency Tables
With Ordered Categories", McCullagh, P. (1980)
<doi:10.1111/j.2517-6161.1980.tb01109.x> "Regression Models For Ordinal
Data", Penn State: Eberly College of Science (undated)
<https://online.stat.psu.edu/stat504/lesson/11> "Stat 504: Analysis of
Discrete Data, 11. Advanced Topics I", Schuster, C. (2001)
<doi:10.3102/10769986026003331> "Kappa As A Parameter Of A Symmetry Model
For Rater Agreement", Shoukri, M. M. (2004 ISBN:978-1584883210). "Measures
Of Interobserver Agreement", Stuart, A. (1953) <doi:10.2307/2333101> "The
Estimation Of And Comparison Of Strengths Of Association In Contingency
Tables", Stuart, A. (1955) <doi:10.2307/2333387> "A Test For Homogeneity
Of The Marginal Distributions In A Two-Way Classification", von Eye, A., &
Mun, E. Y. (2005 ISBN:978-0805849677) "Analyzing Rater Agreement: Manifest
Variable Methods".

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
