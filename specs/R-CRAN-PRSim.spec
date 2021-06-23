%global __brp_check_rpaths %{nil}
%global packname  PRSim
%global packver   1.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Simulation of Streamflow Time Series using Phase Randomization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-homtest 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-CRAN-wavScalogram 
BuildRequires:    R-CRAN-splus2R 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lmomco 
BuildRequires:    R-CRAN-mev 
Requires:         R-CRAN-homtest 
Requires:         R-CRAN-goftest 
Requires:         R-CRAN-wavScalogram 
Requires:         R-CRAN-splus2R 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-lmomco 
Requires:         R-CRAN-mev 

%description
Provides a simulation framework to simulate streamflow time series with
similar main characteristics as observed data. These characteristics
include the distribution of daily streamflow values and their temporal
correlation as expressed by short- and long-range dependence. The approach
is based on the randomization of the phases of the Fourier transform or
the phases of the wavelet transform. The function prsim() is applicable to
single site simulation and uses the Fourier transform. The function
prsim.wave() extends the approach to multiple sites and is based on the
complex wavelet transform. We further use the flexible four-parameter
Kappa distribution, which allows for the extrapolation to yet unobserved
low and high flows. Alternatively, the empirical or any other distribution
can be used. A detailed description of the simulation approach for single
sites and an application example can be found in
<https://hess.copernicus.org/articles/23/3175/2019/>. A detailed
description and evaluation of the wavelet-based multi-site approach can be
found in <https://hess.copernicus.org/articles/24/3967/2020/>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
