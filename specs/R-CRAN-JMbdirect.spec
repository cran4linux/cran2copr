%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  JMbdirect
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Model for Longitudinal and Multiple Time to Events Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-JMbayes2 
BuildRequires:    R-CRAN-joineRML 
BuildRequires:    R-CRAN-FastJM 
BuildRequires:    R-CRAN-rstanarm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jmBIG 
Requires:         R-CRAN-JMbayes2 
Requires:         R-CRAN-joineRML 
Requires:         R-CRAN-FastJM 
Requires:         R-CRAN-rstanarm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jmBIG 

%description
Provides model fitting, prediction, and plotting for joint models of
longitudinal and multiple time-to-event data, including methods from
Rizopoulos (2012) <doi:10.1201/b12208>. Useful for handling complex
survival and longitudinal data in clinical research.

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
