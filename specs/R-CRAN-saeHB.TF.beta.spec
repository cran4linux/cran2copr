%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  saeHB.TF.beta
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          SAE using HB Twofold Subarea Model under Beta Distribution

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.4.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.4.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rstantools

%description
Estimates area and subarea level proportions using the Small Area
Estimation (SAE) Twofold Subarea Model with a hierarchical Bayesian (HB)
approach under Beta distribution. A number of simulated datasets generated
for illustration purposes are also included. The 'rstan' package is
employed to estimate parameters via the Hamiltonian Monte Carlo and No
U-Turn Sampler algorithm. The model-based estimators include the HB mean,
the variation of the mean, and quantiles. For references, see Rao and
Molina (2015) <doi:10.1002/9781118735855>, Torabi and Rao (2014)
<doi:10.1016/j.jmva.2014.02.001>, Leyla Mohadjer et al.(2007)
<http://www.asasrms.org/Proceedings/y2007/Files/JSM2007-000559.pdf>,
Erciulescu et al.(2019) <doi:10.1111/rssa.12390>, and Yudasena (2024).

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
