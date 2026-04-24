%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DownBallotR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access Federal, State, and Local Election Data

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rlang 

%description
Provides an 'R' interface for downloading and standardizing election data
to support research workflows. Election results are published by states
through heterogeneous and often dynamic web interfaces that are not
consistently accessible through existing 'R' packages or APIs. To address
this, the package wraps state-specific 'Python' web scrapers through the
'reticulate' package, enabling access to dynamic content while exposing
consistent 'R' functions for querying election availability and results
across jurisdictions. The package is intended for responsible use and
relies on publicly accessible election result pages.

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
