%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LBDiscover
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Literature-Based Discovery Tools for Biomedical Research

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-xml2 >= 1.3.0
BuildRequires:    R-CRAN-Matrix >= 1.3.0
BuildRequires:    R-CRAN-igraph >= 1.2.0
BuildRequires:    R-CRAN-rentrez >= 1.2.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-tools 
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-xml2 >= 1.3.0
Requires:         R-CRAN-Matrix >= 1.3.0
Requires:         R-CRAN-igraph >= 1.2.0
Requires:         R-CRAN-rentrez >= 1.2.0
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-tools 

%description
A suite of tools for literature-based discovery in biomedical research.
Provides functions for retrieving scientific articles from 'PubMed' and
other NCBI databases, extracting biomedical entities (diseases, drugs,
genes, etc.), building co-occurrence networks, and applying various
discovery models including 'ABC', 'AnC', 'LSI', and 'BITOLA'. The package
also includes visualization tools for exploring discovered connections.

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
