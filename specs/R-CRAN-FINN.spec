%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FINN
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Forest Informed Neural Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-cli 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-coro 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-torch 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 

%description
A hybrid dynamic forest (gap) model (FINN) that can be configured as a
fully mechanistic, process-based model, like classic forest gap models, or
with its demographic processes (growth, mortality, regeneration) replaced
by deep neural networks (DNNs), or any combination of the two. Provides
functions to define a model and its mechanistic or empirical components,
calibrate it to forest inventory data, and interpret the calibrated
processes. FINN is implemented with the 'torch' package, which supplies
GPU support and the automatic differentiation used to calibrate the model
by stochastic gradient descent; no knowledge of 'torch' is required. The
hybrid modeling approach is described in Pichler and Käber (2026)
<doi:10.1111/2041-210x.70347>.

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
