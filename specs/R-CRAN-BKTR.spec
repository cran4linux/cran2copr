%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BKTR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Kernelized Tensor Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-torch >= 0.13.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-R6P 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-torch >= 0.13.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-R6P 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-data.table 

%description
Facilitates scalable spatiotemporally varying coefficient modelling with
Bayesian kernelized tensor regression. The important features of this
package are: (a) Enabling local temporal and spatial modeling of the
relationship between the response variable and covariates. (b)
Implementing the model described by Lei et al. (2023)
<doi:10.48550/arXiv.2109.00046>. (c) Using a Bayesian Markov Chain Monte
Carlo (MCMC) algorithm to sample from the posterior distribution of the
model parameters. (d) Employing a tensor decomposition to reduce the
number of estimated parameters. (e) Accelerating tensor operations and
enabling graphics processing unit (GPU) acceleration with the 'torch'
package.

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
