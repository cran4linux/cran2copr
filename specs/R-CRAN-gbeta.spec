%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gbeta
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Beta and Beta Prime Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-Runuran 
BuildRequires:    R-CRAN-RcppNumerical 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-Runuran 

%description
Density, distribution function, quantile function, and random generation
for the generalized Beta and Beta prime distributions. The family of
generalized Beta distributions is conjugate for the Bayesian binomial
model, and the generalized Beta prime distribution is the posterior
distribution of the relative risk in the Bayesian 'two Poisson samples'
model when a Gamma prior is assigned to the Poisson rate of the reference
group and a Beta prime prior is assigned to the relative risk. References:
Laurent (2012) <doi:10.1214/11-BJPS139>, Hamza & Vallois (2016)
<doi:10.1016/j.spl.2016.03.014>, Chen & Novick (1984)
<doi:10.3102/10769986009002163>.

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
