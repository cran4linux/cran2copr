%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  extraSuperpower
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Power Calculation for Two-Way Factorial Designs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.0
BuildRequires:    R-CRAN-afex >= 1.3.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-ARTool 
BuildRequires:    R-CRAN-permuco 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-MASS >= 7.3.0
Requires:         R-CRAN-afex >= 1.3.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-ARTool 
Requires:         R-CRAN-permuco 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
The basic use of this package is with 3 sequential functions. One to
generate expected cell means and standard deviations, along with
correlation and covariance matrices in the case of repeated measurements.
This is followed by experiment simulation i number of times. Finally,
power is calculated from the simulated data. Features that may be
considered in the model are interaction, measure correlation and
non-normal distributions.

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
