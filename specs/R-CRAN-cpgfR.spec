%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cpgfR
%global packver   0.0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Consolidates Information from the Federal Government Payment Card

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-osfr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-deflateBR 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-osfr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-deflateBR 
Requires:         R-CRAN-curl 

%description
Provides access to consolidated information from the Brazilian Federal
Government Payment Card. Includes functions to retrieve, clean, and
organize data directly from the Transparency Portal
<https://portaldatransparencia.gov.br/download-de-dados/cpgf/> and a
curated dataset hosted on the Open Science Framework
<https://osf.io/z2mxc/>. Useful for public spending analysis, transparency
research, and reproducible workflows in auditing or investigative
journalism.

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
