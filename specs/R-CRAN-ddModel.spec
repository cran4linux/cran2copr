%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ddModel
%global packver   0.2.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Decision Diffusion Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.7.5.0
BuildRequires:    R-CRAN-ggdmcPrior 
BuildRequires:    R-CRAN-ggdmcModel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggdmcHeaders 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-ggdmcPrior 
Requires:         R-CRAN-ggdmcModel 
Requires:         R-methods 

%description
Provides functions for computing the density, distribution, and random
generation of the Decision Diffusion model (DDM), a widely used cognitive
model for analysing choice and response time data. The package allows
model specification, including the ability to fix, constrain, or vary
parameters across experimental conditions. While it does not include a
built-in optimiser, it supports likelihood evaluation and can be
integrated with external tools for parameter estimation. Functions for
simulating synthetic datasets are also provided. This package is intended
for researchers modelling speeded decision-making in behavioural and
cognitive experiments. For more information, see Voss, Rothermund, and
Voss (2004) <doi:10.3758/BF03196893>, Voss and Voss (2007)
<doi:10.3758/BF03192967>, and Ratcliff and McKoon (2008)
<doi:10.1162/neco.2008.12-06-420>.

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
