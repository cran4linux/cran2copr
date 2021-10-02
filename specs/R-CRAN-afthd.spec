%global __brp_check_rpaths %{nil}
%global packname  afthd
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Accelerated Failure Time for High Dimensional Data with MCMC

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-photobiology 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-rstpm2 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-photobiology 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-rstpm2 
Requires:         R-CRAN-survival 

%description
Functions for Posterior estimates of Accelerated Failure Time(AFT) model
with MCMC and Maximum likelihood estimates of AFT model without MCMC for
univariate and multivariate analysis in high dimensional gene expression
data are available in this 'afthd' package. AFT model with Bayesian
framework for multivariate in high dimensional data has been proposed by
Prabhash et al.(2016) <doi:10.21307/stattrans-2016-046>.

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
