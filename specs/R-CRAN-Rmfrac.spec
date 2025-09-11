%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rmfrac
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation and Statistical Analysis of Multifractional Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-parallel 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shiny 
Requires:         R-graphics 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-fields 
Requires:         R-utils 

%description
Simulation of several fractional and multifractional processes. Includes
Brownian and fractional Brownian motions, bridges and Gaussian Haar-based
multifractional processes (GHBMP). Implements the methods from Ayache,
Olenko and Samarakoon (2025) <doi:10.48550/arXiv.2503.07286> for
simulation of GHBMP. Estimation of Hurst functions and local fractal
dimension. Clustering realisations based on the Hurst functions. Several
functions to estimate and plot geometric statistics of the processes and
time series. Provides a 'shiny' application for interactive use of the
functions from the package.

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
