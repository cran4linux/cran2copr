%global __brp_check_rpaths %{nil}
%global packname  PROscorerTools
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Score Patient-Reported Outcome (PRO) and Other Psychometric Measures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides a reliable and flexible toolbox to score patient-reported outcome
(PRO), Quality of Life (QOL), and other psychometric measures. The guiding
philosophy is that scoring errors can be eliminated by using a limited
number of well-tested, well-behaved functions to score PRO-like measures.
The workhorse of the package is the 'scoreScale' function, which can be
used to score most single-scale measures. It can reverse code items that
need to be reversed before scoring and pro-rate scores for missing item
data. Currently, three different types of scores can be output: summed
item scores, mean item scores, and scores scaled to range from 0 to 100.
The 'PROscorerTools' functions can be used to write new functions that
score more complex measures. In fact, 'PROscorerTools' functions are the
building blocks of the scoring functions in the 'PROscorer' package (which
is a repository of functions that score specific commonly-used
instruments). Users are encouraged to use 'PROscorerTools' to write
scoring functions for their favorite PRO-like instruments, and to submit
these functions for inclusion in 'PROscorer' (a tutorial vignette will be
added soon). The long-term vision for the 'PROscorerTools' and 'PROscorer'
packages is to provide an easy-to-use system to facilitate the
incorporation of PRO measures into research studies in a scientifically
rigorous and reproducible manner. These packages and their vignettes are
intended to help establish and promote "best practices" for scoring and
describing PRO-like measures in research.

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
