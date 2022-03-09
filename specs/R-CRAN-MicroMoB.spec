%global __brp_check_rpaths %{nil}
%global packname  MicroMoB
%global packver   0.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Time Simulation of Mosquito-Borne Pathogen Transmission

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-plumber 
BuildRequires:    R-CRAN-httpuv 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-plumber 
Requires:         R-CRAN-httpuv 

%description
Provides a framework based on S3 dispatch for constructing models of
mosquito-borne pathogen transmission which are constructed from submodels
of various components (i.e. immature and adult mosquitoes, human
populations). A consistent mathematical expression for the distribution of
bites on hosts means that different models (stochastic, deterministic,
etc.) can be coherently incorporated and updated over a discrete time
step.

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
