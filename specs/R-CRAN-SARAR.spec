%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SARAR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Estimation of Spatial Autoregressive Models with Flexible Error Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-spdep 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-spdep 

%description
Provides Bayesian estimation and inference for spatial autoregressive
models with spatial dependence in both the response variable and the error
terms. The models accommodate Gaussian, Student-t, Laplace, skew-normal,
and skew-Student-t error distributions. Posterior inference is performed
using Markov chain Monte Carlo methods. The package also provides
posterior summaries, convergence diagnostics, residual analysis, and model
comparison criteria, including the Deviance Information Criterion (DIC)
and the Watanabe-Akaike Information Criterion (WAIC).  See LeSage and Pace
(2009, ISBN:9781420064247), "Introduction to Spatial Econometrics".

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
