%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Keng
%global packver   2025.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2025.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Knock Errors Off Nice Guesses

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Miscellaneous functions and data used in psychological research and
teaching. Keng currently has a built-in dataset depress, and could (1)
scale a vector; (2) compute the cut-off values of Pearson's r with known
sample size; (3) test the significance and compute the post-hoc power for
Pearson's r with known sample size; (4) conduct a priori power analysis
and plan the sample size for Pearson's r; (5) compare lm()'s fitted
outputs using R-squared, f_squared, post-hoc power, and PRE (Proportional
Reduction in Error, also called partial R-squared or partial Eta-squared);
(6) calculate PRE from partial correlation, Cohen's f, or f_squared; (7)
conduct a priori power analysis and plan the sample size for one or a set
of predictors in regression analysis; (8) conduct post-hoc power analysis
for one or a set of predictors in regression analysis with known sample
size; (9) randomly pick numbers for Chinese Super Lotto and Double Color
Balls; (10) assess course objective achievement in Outcome-Based
Education.

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
