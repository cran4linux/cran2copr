%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TwoTimeScales
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Event Data with Two Time Scales

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-Epi 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-JOPS 
BuildRequires:    R-CRAN-LMMsolver 
BuildRequires:    R-CRAN-popEpi 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-Epi 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-JOPS 
Requires:         R-CRAN-LMMsolver 
Requires:         R-CRAN-popEpi 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-viridis 

%description
Analyse time to event data with two time scales by estimating a smooth
hazard that varies over two time scales and also, if covariates are
available, to estimate a proportional hazards model with such a
two-dimensional baseline hazard. Functions are provided to prepare the raw
data for estimation, to estimate and to plot the two-dimensional smooth
hazard. Extension to a competing risks model are implemented. For details
about the method please refer to Carollo et al. (2024)
<doi:10.1002/sim.10297>.

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
