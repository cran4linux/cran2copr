%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  betafunctions
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Two- And Four-Parameter Beta Distributions and Classification Accuracy and Consistency

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
Functions for working with two- and four-parameter Beta distributions and
the closely related Beta-Binomial distribution, and for estimating the
accuracy and consistency of test-based classifications. Includes d/p/q/r
functions for four-parameter Beta distributions, including
parameterization by mean and variance; d/p/r functions for Beta-Binomial
distributions and for Lord's two-term approximation to the compound
Binomial distribution; moments of Beta, Binomial, Beta-Binomial, and
observed-score distributions; and method-of-moments fitting of two- and
four-parameter Beta true-score distributions. Classification accuracy and
consistency can be estimated with the 'Livingston and Lewis' approach
(Livingston and Lewis, 1995 <doi:10.1111/j.1745-3984.1995.tb00462.x>), the
'Hanson and Brennan' approach based on Lord's strong true-score theory
(Lord, 1965 <doi:10.1007/BF02289490>; Hanson, 1991
<https://files.eric.ed.gov/fulltext/ED344945.pdf>), and the multinomial
and compound multinomial approach (Lee, 2007
<doi:10.1177/0146621606294206>; Lee, Brennan, and Wan, 2009
<doi:10.1177/0146621608321759>), for two or more categories, with ROC
analysis, model-fit tests, and examinee- or score-level results.

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
