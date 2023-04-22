%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tripEstimation
%global packver   0.0-46
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.46
Release:          1%{?dist}%{?buildtag}
Summary:          Metropolis Sampler and Supporting Functions for Estimating Animal Movement from Archival Tags and Satellite Fixes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-reproj 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-reproj 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-zoo 

%description
Data handling and estimation functions for animal movement estimation from
archival or satellite tags. Helper functions are included for making image
summaries binned by time interval from Markov Chain Monte Carlo
simulations.

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
