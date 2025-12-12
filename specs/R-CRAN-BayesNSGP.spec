%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesNSGP
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Analysis of Non-Stationary Gaussian Process Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nimble 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-StatMatch 
Requires:         R-CRAN-nimble 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-StatMatch 

%description
Enables off-the-shelf functionality for fully Bayesian, nonstationary
Gaussian process modeling. The approach to nonstationary modeling involves
a closed-form, convolution-based covariance function with
spatially-varying parameters; these parameter processes can be specified
either deterministically (using covariates or basis functions) or
stochastically (using approximate Gaussian processes). Stationary Gaussian
processes are a special case of our methodology, and we furthermore
implement approximate Gaussian process inference to account for very large
spatial data sets (Finley, et al (2017) <doi:10.48550/arXiv.1702.00434>).
Bayesian inference is carried out using Markov chain Monte Carlo methods
via the "nimble" package, and posterior prediction for the Gaussian
process at unobserved locations is provided as a post-processing step.

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
