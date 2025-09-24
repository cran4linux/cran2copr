%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiLevelOptimalBayes
%global packver   0.0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regularized Bayesian Estimator for Two-Level Latent Variable Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-pracma 

%description
Implements a regularized Bayesian estimator that optimizes the estimation
of between-group coefficients for multilevel latent variable models by
minimizing mean squared error (MSE) and balancing variance and bias. The
package provides more reliable estimates in scenarios with limited data,
offering a robust solution for accurate parameter estimation in two-level
latent variable models. It is designed for researchers in psychology,
education, and related fields who face challenges in estimating
between-group effects under small sample sizes and low intraclass
correlation coefficients. The package includes comprehensive S3 methods
for result objects: print(), summary(), coef(), se(), vcov(), confint(),
as.data.frame(), dim(), length(), names(), and update() for enhanced
usability and integration with standard R workflows. Dashuk et al. (2025a)
<doi:10.1017/psy.2025.10045> derived the optimal regularized Bayesian
estimator; Dashuk et al. (2025b) <doi:10.1007/s41237-025-00264-7> extended
it to the multivariate case; and Luedtke et al. (2008)
<doi:10.1037/a0012869> formalized the two-level latent variable framework.

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
