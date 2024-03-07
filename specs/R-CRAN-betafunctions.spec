%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  betafunctions
%global packver   1.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Working with Two- And Four-Parameter Beta Probability Distributions and Psychometric Analysis of Classifications

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Package providing a number of functions for working with Two- and
Four-parameter Beta and closely related distributions (i.e., the Gamma-
Binomial-, and Beta-Binomial distributions). Includes, among other things:
- d/p/q/r functions for Four-Parameter Beta distributions and Generalized
"Binomial" (continuous) distributions, and d/p/r- functions for Beta-
Binomial distributions. - d/p/q/r functions for Two- and Four-Parameter
Beta distributions parameterized in terms of their means and variances
rather than their shape-parameters. - Moment generating functions for
Binomial distributions, Beta-Binomial distributions, and observed value
distributions. - Functions for estimating classification accuracy and
consistency, making use of the Classical Test-Theory based 'Livingston and
Lewis' (L&L) and 'Hanson and Brennan' approaches. A shiny app is
available, providing a GUI for the L&L approach when used for binary
classifications. For url to the app, see documentation for the LL.CA()
function. Livingston and Lewis (1995)
<doi:10.1111/j.1745-3984.1995.tb00462.x>. Lord (1965)
<doi:10.1007/BF02289490>. Hanson (1991)
<https://files.eric.ed.gov/fulltext/ED344945.pdf>.

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
