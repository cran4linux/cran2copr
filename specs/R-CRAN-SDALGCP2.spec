%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SDALGCP2
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Spatially Discrete Approximation to Log-Gaussian Cox Processes for Aggregated Disease Count Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-progress 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits a spatially discrete approximation to a log-Gaussian Cox process
model for spatially aggregated disease count data, estimated by Monte
Carlo Maximum Likelihood as in Christensen (2004)
<doi:10.1198/106186004X2525> and Johnson, Diggle and Giorgi (2019)
<doi:10.1002/sim.8339>. Performance-critical steps (aggregated correlation
assembly, 'MALA' sampling, the Monte Carlo likelihood, and the
Kronecker-structured space-time likelihood) are implemented in C++ via
'RcppArmadillo'. Provides a one-line, 'glm'-like interface and statistical
extensions including a nugget term, general 'Matern' smoothness, raster
and misaligned covariates, restricted spatial regression,
importance-sampling diagnostics and re-anchored 'MCML'.

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
