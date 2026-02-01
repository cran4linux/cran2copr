%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RSTr
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Gibbs Samplers for Discrete Bayesian Spatiotemporal Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-RcppArmadillo >= 15.2.2.1
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-RcppDist >= 0.1.1.1
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-spdep 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-spdep 

%description
Takes Poisson or Binomial discrete spatial data and runs a Gibbs sampler
for a variety of Spatiotemporal Conditional Autoregressive (CAR) models.
Includes measures to prevent estimate over-smoothing through a restriction
of model informativeness for select models. Also provides tools to load
output and get median estimates. Implements methods from Besag, York, and
Mollié (1991) "Bayesian image restoration, with two applications in
spatial statistics" <doi:10.1007/BF00116466>, Gelfand and Vounatsou (2003)
"Proper multivariate conditional autoregressive models for spatial data
analysis" <doi:10.1093/biostatistics/4.1.11>, Quick et al. (2017)
"Multivariate spatiotemporal modeling of age-specific stroke mortality"
<doi:10.1214/17-AOAS1068>, and Quick et al. (2021) "Evaluating the
informativeness of the Besag-York-Mollié CAR model"
<doi:10.1016/j.sste.2021.100420>.

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
