%global __brp_check_rpaths %{nil}
%global packname  sharp
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stability-enHanced Approaches using Resampling Procedures

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 2.4.0
BuildRequires:    R-CRAN-glassoFast >= 1.0
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-huge 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-withr >= 2.4.0
Requires:         R-CRAN-glassoFast >= 1.0
Requires:         R-CRAN-glmnet 
Requires:         R-grDevices 
Requires:         R-CRAN-huge 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-parallel 
Requires:         R-CRAN-Rdpack 

%description
Implementation of stability selection for graphical modelling and variable
selection in regression and dimensionality reduction. These models use on
resampling approaches to estimate selection probabilities (N Meinshausen,
P Bühlmann (2010) <doi:10.1111/j.1467-9868.2010.00740.x>). Calibration of
the hyper-parameters is done via maximisation of a stability score
measuring the likelihood of informative (non-uniform) selection (B
Bodinier, S Filippi, TH Nost, J Chiquet, M Chadeau-Hyam (2021)
<arXiv:2106.02521>). This package also includes tools to simulate
multivariate Normal data with different (partial) correlation structures.

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
