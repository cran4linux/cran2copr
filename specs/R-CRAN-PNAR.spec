%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PNAR
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Poisson Network Autoregressive Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-stats 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-nloptr 
Requires:         R-parallel 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 
Requires:         R-stats 

%description
Quasi likelihood-based methods for estimating linear and log-linear
Poisson Network Autoregression models with p lags and covariates. Tools
for testing the linearity versus several non-linear alternatives. Tools
for simulation of multivariate count distributions, from linear and
non-linear PNAR models, by using a specific copula construction.
References include: Armillotta, M. and K. Fokianos (2023). "Nonlinear
network autoregression". Annals of Statistics, 51(6): 2526--2552.
<doi:10.1214/23-AOS2345>. Armillotta, M. and K. Fokianos (2024). "Count
network autoregression". Journal of Time Series Analysis, 45(4): 584--612.
<doi:10.1111/jtsa.12728>. Armillotta, M., Tsagris, M. and Fokianos, K.
(2024). "Inference for Network Count Time Series with the R Package PNAR".
The R Journal, 15/4: 255--269. <doi:10.32614/RJ-2023-094>.

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
