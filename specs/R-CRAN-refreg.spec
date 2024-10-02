%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  refreg
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Multivariate Reference Regions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-misc3d 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-mbend 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-methods 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-misc3d 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-mbend 
Requires:         R-CRAN-matrixcalc 
Requires:         R-methods 

%description
An R package for estimating conditional multivariate reference regions.
The reference region is non parametrically estimated using a kernel
density estimator. Covariates effects on the multivariate response means
vector and variance-covariance matrix, thus on the region shape, are
estimated by flexible additive predictors. Continuous covariates non
linear effects might be estimated using penalized splines smoothers.
Confidence intervals for the covariates estimated effects might be derived
from bootstrap resampling. Kernel density bandwidth can be estimated with
different methods, including a method that optimize the region coverage.
Numerical, and graphical, summaries can be obtained by the user in order
to evaluate reference region performance with real data. Full mathematical
details can be found in <doi:10.1002/sim.9163> and
<doi:10.1007/s00477-020-01901-1>.

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
