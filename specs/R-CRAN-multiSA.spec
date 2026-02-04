%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multiSA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Stock Assessment

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RTMB >= 1.7
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tinyplot 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-utils 
Requires:         R-CRAN-RTMB >= 1.7
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gplots 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-snowfall 
Requires:         R-stats 
Requires:         R-CRAN-tinyplot 
Requires:         R-CRAN-TMB 
Requires:         R-utils 

%description
Implementation of a next-generation, multi-stock age-structured fisheries
assessment model. 'multiSA' is intended for use in mixed fisheries where
stock composition can not be readily identified in fishery data alone,
e.g., from catch and age/length composition. Models can be fitted to
genetic data, e.g., stock composition of catches and close-kin pairs, with
seasonal stock availability and movement.

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
