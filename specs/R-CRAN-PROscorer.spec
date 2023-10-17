%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PROscorer
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Score Commonly-Used Patient-Reported Outcome (PRO) Measures and Other Psychometric Instruments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-PROscorerTools 
Requires:         R-CRAN-PROscorerTools 

%description
An extensible repository of accurate, up-to-date functions to score
commonly used patient-reported outcome (PRO), quality of life (QOL), and
other psychometric and psychological measures. 'PROscorer', together with
the 'PROscorerTools' package, is a system to facilitate the incorporation
of PRO measures into research studies and clinical settings in a
scientifically rigorous and reproducible manner.  These packages and their
vignettes are intended to help establish and promote best practices for
scoring PRO and PRO-like measures in research.  The 'PROscorer' Instrument
Descriptions vignette contains descriptions of each instrument scored by
'PROscorer', complete with references.  These instrument descriptions are
suitable for inclusion in formal study protocol documents, grant
proposals, and manuscript Method sections.  Each 'PROscorer' function is
composed of helper functions from the 'PROscorerTools' package, and users
are encouraged to contribute new functions to 'PROscorer'.  More scoring
functions are currently in development and will be added in future
updates.

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
