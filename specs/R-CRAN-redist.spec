%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  redist
%global packver   4.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation Methods for Legislative Redistricting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel
BuildRequires:    libxml2-devel
Recommends:       python3
BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-cli >= 3.1.0
BuildRequires:    R-CRAN-redistmetrics >= 1.0.2
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-servr 
BuildRequires:    R-CRAN-sys 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-cli >= 3.1.0
Requires:         R-CRAN-redistmetrics >= 1.0.2
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-servr 
Requires:         R-CRAN-sys 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 

%description
Enables researchers to sample redistricting plans from a pre-specified
target distribution using Sequential Monte Carlo and Markov Chain Monte
Carlo algorithms. The package allows for the implementation of various
constraints in the redistricting process such as geographic compactness
and population parity requirements. Tools for analysis such as computation
of various summary statistics and plotting functionality are also
included. The package implements the SMC algorithm of McCartan and Imai
(2023) <doi:10.1214/23-AOAS1763>, the enumeration algorithm of Fifield,
Imai, Kawahara, and Kenny (2020) <doi:10.1080/2330443X.2020.1791773>, the
Flip MCMC algorithm of Fifield, Higgins, Imai and Tarr (2020)
<doi:10.1080/10618600.2020.1739532>, the Merge-split/Recombination
algorithms of Carter et al. (2019) <doi:10.48550/arXiv.1911.01503> and
DeFord et al. (2021) <doi:10.1162/99608f92.eb30390f>, and the Short-burst
optimization algorithm of Cannon et al. (2020)
<doi:10.48550/arXiv.2011.02288>.

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
