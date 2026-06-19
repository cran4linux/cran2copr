%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesianDisaggregation
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Evidence-Based Bayesian Disaggregation of Aggregate Indices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-parallel 

%description
Disaggregates an observed aggregate price index into sectoral components
with a Bayesian state-space model in which the aggregate enters as a
genuine observation density rather than as a renormalization identity. A
random-walk-with-drift transition in log space (with partial pooling on
the drift and the innovation scale) and an estimable cross-sectional
concentration produce posterior draws of the sectoral indices with
credible intervals, suitable as multiple-imputation input for downstream
dynamic models. The Hamiltonian Monte Carlo engine follows Stan (Carpenter
et al., 2017) <doi:10.18637/jss.v076.i01>; model comparison uses Pareto
Smoothed Importance Sampling Leave-One-Out cross-validation (Vehtari,
Gelman and Gabry, 2017) <doi:10.1007/s11222-016-9696-4>. A closed-form
linear-Gaussian Kalman/RTS smoother provides an exact, MCMC-free Bayesian
alternative for the same aggregate evidence.

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
