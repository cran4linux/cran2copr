%global packname  decon
%global packver   1.2-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          3%{?dist}%{?buildtag}
Summary:          Deconvolution Estimation in Measurement Error Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
This package contains a collection of functions to deal with nonparametric
measurement error problems using deconvolution kernel methods. We focus
two measurement error models in the package: (1) an additive measurement
error model, where the goal is to estimate the density or distribution
function from contaminated data; (2) nonparametric regression model with
errors-in-variables. The R functions allow the measurement errors to be
either homoscedastic or heteroscedastic. To make the deconvolution
estimators computationally more efficient in R, we adapt the "Fast Fourier
Transform" (FFT) algorithm for density estimation with error-free data to
the deconvolution kernel estimation. Several methods for the selection of
the data-driven smoothing parameter are also provided in the package. See
details in: Wang, X.F. and Wang, B. (2011). Deconvolution estimation in
measurement error models: The R package decon. Journal of Statistical
Software, 39(10), 1-24.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/script
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
