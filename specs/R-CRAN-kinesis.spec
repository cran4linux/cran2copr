%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kinesis
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          'shiny' Applications for the 'tesselle' Packages

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-tabula >= 3.3.1
BuildRequires:    R-CRAN-kairos >= 2.3.0
BuildRequires:    R-CRAN-mirai >= 2.3.0
BuildRequires:    R-CRAN-folio >= 1.5.1
BuildRequires:    R-CRAN-aion >= 1.5.0
BuildRequires:    R-CRAN-isopleuros >= 1.4.0
BuildRequires:    R-CRAN-khroma >= 1.16.0
BuildRequires:    R-CRAN-arkhe >= 1.11.0
BuildRequires:    R-CRAN-shiny >= 1.10.0
BuildRequires:    R-CRAN-gt >= 1.0.0
BuildRequires:    R-CRAN-bslib >= 0.9.0
BuildRequires:    R-CRAN-nexus >= 0.6.0
BuildRequires:    R-CRAN-sass >= 0.4.10
BuildRequires:    R-CRAN-config >= 0.3.2
BuildRequires:    R-CRAN-dimensio >= 0.14.0
BuildRequires:    R-datasets 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-tabula >= 3.3.1
Requires:         R-CRAN-kairos >= 2.3.0
Requires:         R-CRAN-mirai >= 2.3.0
Requires:         R-CRAN-folio >= 1.5.1
Requires:         R-CRAN-aion >= 1.5.0
Requires:         R-CRAN-isopleuros >= 1.4.0
Requires:         R-CRAN-khroma >= 1.16.0
Requires:         R-CRAN-arkhe >= 1.11.0
Requires:         R-CRAN-shiny >= 1.10.0
Requires:         R-CRAN-gt >= 1.0.0
Requires:         R-CRAN-bslib >= 0.9.0
Requires:         R-CRAN-nexus >= 0.6.0
Requires:         R-CRAN-sass >= 0.4.10
Requires:         R-CRAN-config >= 0.3.2
Requires:         R-CRAN-dimensio >= 0.14.0
Requires:         R-datasets 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
A collection of 'shiny' applications for the 'tesselle' packages
<https://www.tesselle.org/>. This package provides applications for
archaeological data analysis and visualization. These mainly, but not
exclusively, include applications for chronological modelling (e.g. matrix
seriation, aoristic analysis) and count data analysis (e.g. diversity
measures, compositional data analysis).

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
