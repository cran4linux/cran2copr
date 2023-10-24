%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  singleRcapture
%global packver   0.2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Single-Source Capture-Recapture Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lamW 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-lamW 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 

%description
Implementation of single-source capture-recapture methods for population
size estimation using zero-truncated, zero-one truncated and
zero-truncated one-inflated Poisson, Geometric and Negative Binomial
regression as well as Zelterman's and Chao's regression. Package includes
point and interval estimators for the population size with variances
estimated using analytical or bootstrap method. Details can be found in:
van der Heijden et all. (2003) <doi:10.1191/1471082X03st057oa>, Böhning
and van der Heijden (2019) <doi:10.1214/18-AOAS1232>, Böhning et al.
(2020) Capture-Recapture Methods for the Social and Medical Sciences or
Böhning and Friedl (2021) <doi:10.1007/s10260-021-00556-8>.

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
