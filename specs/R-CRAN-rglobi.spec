%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rglobi
%global packver   0.2.28
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.28
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to Global Biotic Interactions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-RCurl >= 0.3.4
BuildRequires:    R-CRAN-curl >= 0.3.3
BuildRequires:    R-CRAN-rjson >= 0.2.13
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-RCurl >= 0.3.4
Requires:         R-CRAN-curl >= 0.3.3
Requires:         R-CRAN-rjson >= 0.2.13

%description
A programmatic interface to the web service methods provided by Global
Biotic Interactions (GloBI) (<https://www.globalbioticinteractions.org/>).
GloBI provides access to spatial-temporal species interaction records from
sources all over the world. rglobi provides methods to search species
interactions by location, interaction type, and taxonomic name. In
addition, it supports Cypher, a graph query language, to allow for
executing custom queries on the GloBI aggregate species interaction data
set.

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
