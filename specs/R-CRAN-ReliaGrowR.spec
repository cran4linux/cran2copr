%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ReliaGrowR
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Reliability Growth Analysis

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-plumber 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-plumber 
Requires:         R-CRAN-segmented 
Requires:         R-stats 

%description
Modeling and plotting functions for Reliability Growth Analysis (RGA).
Models include the Duane (1962) <doi:10.1109/TA.1964.4319640>,
Non-Homogeneous Poisson Process (NHPP) by Crow (1975)
<https://apps.dtic.mil/sti/citations/ADA020296>, Piecewise Weibull NHPP by
Guo et al. (2010) <doi:10.1109/RAMS.2010.5448029>, and Piecewise Weibull
NHPP with Change Point Detection based on the 'segmented' package by
Muggeo (2024) <https://cran.r-project.org/package=segmented>.

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
