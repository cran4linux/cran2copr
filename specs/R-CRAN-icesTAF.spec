%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  icesTAF
%global packver   4.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Support the ICES Transparent Assessment Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-TAF >= 4.3.0
BuildRequires:    R-CRAN-icesSAG >= 1.6.2
BuildRequires:    R-CRAN-icesVocab >= 1.3.1
BuildRequires:    R-CRAN-icesDatsu >= 1.2.1
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-icesConnect 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-TAF >= 4.3.0
Requires:         R-CRAN-icesSAG >= 1.6.2
Requires:         R-CRAN-icesVocab >= 1.3.1
Requires:         R-CRAN-icesDatsu >= 1.2.1
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-icesConnect 
Requires:         R-CRAN-httr 

%description
Functions to support the ICES Transparent Assessment Framework
<https://taf.ices.dk> to organize data, methods, and results used in ICES
assessments. ICES is an organization facilitating international
collaboration in marine science.

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
