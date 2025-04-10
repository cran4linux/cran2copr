%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rice
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Radiocarbon Equations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-maps >= 3.4.2.1
BuildRequires:    R-CRAN-rintcal >= 1.1.3
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-maps >= 3.4.2.1
Requires:         R-CRAN-rintcal >= 1.1.3
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 

%description
Provides functions for the calibration of radiocarbon dates, as well as
options to calculate different radiocarbon realms (C14 age, F14C, pMC,
D14C) and estimating the effects of contamination or local reservoir
offsets (Reimer and Reimer 2001 <doi:10.1017/S0033822200038339>). The
methods follow long-established recommendations such as Stuiver and Polach
(1977) <doi:10.1017/S0033822200003672> and Reimer et al. (2004)
<doi:10.1017/S0033822200033154>. This package complements the data package
'rintcal'.

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
