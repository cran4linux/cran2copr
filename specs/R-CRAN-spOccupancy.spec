%global __brp_check_rpaths %{nil}
%global packname  spOccupancy
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Single-Species, Multi-Species, and Integrated Spatial Occupancy Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-spBayes 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-spBayes 
Requires:         R-methods 

%description
Fits single-species, multi-species, and integrated non-spatial and spatial
occupancy models using Markov Chain Monte Carlo (MCMC). Models are fit
using Polya-Gamma data augmentation detailed in Polson, Scott, and Windle
(2013) <doi:10.1080/01621459.2013.829001>. Spatial models are fit using
either Gaussian processes or Nearest Neighbor Gaussian Processes (NNGP)
for large spatial datasets. Details on NNGP models are given in Datta,
Banerjee, Finley, and Gelfand (2016) <doi:10.1080/01621459.2015.1044091>
and Finley, Datta, and Banerjee (2020) <arXiv:2001.09111>. Provides
functionality for data integration of multiple single-species occupancy
data sets using a joint likelihood framework. Details on data integration
are given in Miller, Pacifici, Sanderlin, and Reich (2019)
<doi:10.1111/2041-210X.13110>. Details on single-species and multi-species
models are found in MacKenzie, Nichols, Lachman, Droege, Royle, and
Langtimm (2002) <doi:10.1890/0012-9658(2002)083[2248:ESORWD]2.0.CO;2> and
Dorazio and Royle <doi:10.1198/016214505000000015>, respectively.

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
