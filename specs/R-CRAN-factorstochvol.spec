%global __brp_check_rpaths %{nil}
%global packname  factorstochvol
%global packver   0.10.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Estimation of (Sparse) Latent Factor Stochastic Volatility Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-stochvol >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.900
BuildRequires:    R-CRAN-GIGrvg >= 0.4
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-stochvol >= 3.0.2
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-GIGrvg >= 0.4
Requires:         R-CRAN-corrplot 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Markov chain Monte Carlo (MCMC) sampler for fully Bayesian estimation of
latent factor stochastic volatility models with interweaving
<doi:10.1080/10618600.2017.1322091>. Sparsity can be achieved through the
usage of Normal-Gamma priors on the factor loading matrix
<doi:10.1016/j.jeconom.2018.11.007>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
