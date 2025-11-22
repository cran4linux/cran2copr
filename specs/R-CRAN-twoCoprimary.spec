%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  twoCoprimary
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Size and Power Calculation for Two Co-Primary Endpoints

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-fpCompare 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-fpCompare 
Requires:         R-stats 

%description
Comprehensive functions to calculate sample size and power for clinical
trials with two co-primary endpoints. The package supports five endpoint
combinations: two continuous endpoints (Sozu et al. 2011
<doi:10.1080/10543406.2011.551329>), two binary endpoints using asymptotic
methods (Sozu et al. 2010 <doi:10.1002/sim.3972>) and exact methods (Homma
and Yoshida 2025 <doi:10.1177/09622802251368697>), mixed continuous and
binary endpoints (Sozu et al. 2012 <doi:10.1002/bimj.201100221>), and
mixed count and continuous endpoints (Homma and Yoshida 2024
<doi:10.1002/pst.2337>). All methods appropriately account for correlation
between endpoints and provide both sample size and power calculation
capabilities.

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
