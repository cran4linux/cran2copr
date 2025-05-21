%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  olr
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Linear Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-plyr 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-htmltools 

%description
The olr function systematically evaluates multiple linear regression
models by exhaustively fitting all possible combinations of independent
variables against the specified dependent variable. It selects the model
that yields the highest adjusted R-squared (by default) or R-squared,
depending on user preference. In model evaluation, both R-squared and
adjusted R-squared are key metrics: R-squared measures the proportion of
variance explained but tends to increase with the addition of
predictors—regardless of relevance—potentially leading to overfitting.
Adjusted R-squared compensates for this by penalizing model complexity,
providing a more balanced view of fit quality. The goal of olr is to
identify the most suitable model that captures the underlying structure of
the data while avoiding unnecessary complexity. By comparing both metrics,
it offers a robust evaluation framework that balances predictive power
with model parsimony. Example Analogy: Imagine a gardener trying to
understand what influences plant growth (the dependent variable). They
might consider variables like sunlight, watering frequency, soil type, and
nutrients (independent variables). Instead of manually guessing which
combination works best, the olr function automatically tests every
possible combination of predictors and identifies the most effective
model—based on either the highest R-squared or adjusted R-squared value.
This saves the user from trial-and-error modeling and highlights only the
most meaningful variables for explaining the outcome. A Python version is
also available at <https://pypi.org/project/olr>.

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
