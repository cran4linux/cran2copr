%global __brp_check_rpaths %{nil}
%global packname  eSIR
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extended State-Space SIR Models

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.2
Requires:         R-core >= 3.5.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.10
BuildRequires:    R-CRAN-gtools >= 3.8.1
BuildRequires:    R-grDevices >= 3.5.2
BuildRequires:    R-graphics >= 3.5.2
BuildRequires:    R-stats >= 3.5.2
BuildRequires:    R-utils >= 3.5.2
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-chron >= 2.3.54
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-coda >= 0.19.3
Requires:         R-CRAN-rjags >= 4.10
Requires:         R-CRAN-gtools >= 3.8.1
Requires:         R-grDevices >= 3.5.2
Requires:         R-graphics >= 3.5.2
Requires:         R-stats >= 3.5.2
Requires:         R-utils >= 3.5.2
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-chron >= 2.3.54
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-coda >= 0.19.3

%description
An implementation of extended state-space SIR models developed by Song Lab
at UM school of Public Health. There are several functions available by 1)
including a time-varying transmission modifier, 2) adding a time-dependent
quarantine compartment, 3) adding a time-dependent antibody-immunization
compartment. Wang L et al. (2020) <doi:10.6339/JDS.202007_18(3).0003>.

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
