%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dhmeasures
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Digital History Measures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidytext 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidytext 

%description
Provides statistical functions to aid in the analysis of contemporary and
historical corpora. These transparent functions may be useful to anyone,
and were designed with the social sciences and humanities in mind. JSD
(Jensen-Shannon Divergence) is a measure of the distance between two
probability distributions. The JSD and Original JSD functions expand on
existing functions, by calculating the JSD for distributions of words in
text groups for all pairwise groups provided (Drost (2018)
<doi:10.21105/joss.00765>). The Log Likelihood function is inspired by the
work of digital historian Jo Guldi (Guldi (2022)
<https://github.com/joguldi/digital-history>). Also includes helper
functions that can count word frequency in each text grouping, and remove
stop words.

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
