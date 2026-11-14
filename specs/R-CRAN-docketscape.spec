%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  docketscape
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Legal Network and Congestion-Aware Delay Modeling for Court Dockets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-survival 

%description
Splits court delay into two parts: (1) what a case is, represented through
the statutory Acts and Sections invoked by the case, and (2) where it
sits, represented by time-varying court docket load. Builds a weighted
similarity graph of cases from legal provisions using 'igraph' and
'Matrix', estimates censoring-aware expected resolution timelines using
legally similar neighbours, calculates relative lateness, and models delay
in relation to filing-time court docket load using 'survival'. Designed
for case-level judicial records such as the Development Data Lab (DDL)
extract of Indian lower courts
(<https://www.devdatalab.org/judicial-data>). Observational and
non-causal; does not rank judges, evaluate judicial performance, or claim
causal delay effects.

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
