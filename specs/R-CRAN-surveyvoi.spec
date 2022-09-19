%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  surveyvoi
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Survey Value of Information

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw3-devel
BuildRequires:    gmp-devel
BuildRequires:    mpfr-devel
BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-vegan >= 2.5.6
BuildRequires:    R-CRAN-RcppAlgos >= 2.3.6
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-withr >= 2.1.2
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-xgboost >= 1.5.2.1
BuildRequires:    R-CRAN-groupdata2 >= 1.3.0
BuildRequires:    R-CRAN-nloptr >= 1.2.2.2
BuildRequires:    R-CRAN-progress >= 1.2.2
BuildRequires:    R-CRAN-PoissonBinomial >= 1.1.1
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-sf >= 0.8.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.7.0
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-CRAN-Rsymphony >= 0.1.31
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-CRAN-vegan >= 2.5.6
Requires:         R-CRAN-RcppAlgos >= 2.3.6
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-withr >= 2.1.2
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-xgboost >= 1.5.2.1
Requires:         R-CRAN-groupdata2 >= 1.3.0
Requires:         R-CRAN-nloptr >= 1.2.2.2
Requires:         R-CRAN-progress >= 1.2.2
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-sf >= 0.8.0
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-CRAN-Rsymphony >= 0.1.31
Requires:         R-CRAN-Matrix 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-parallel 

%description
Decision support tool for prioritizing sites for ecological surveys based
on their potential to improve plans for conserving biodiversity (e.g.
plans for establishing protected areas). Given a set of sites that could
potentially be acquired for conservation management, it can be used to
generate and evaluate plans for surveying additional sites. Specifically,
plans for ecological surveys can be generated using various conventional
approaches (e.g. maximizing expected species richness, geographic
coverage, diversity of sampled environmental algorithms. After generating
such survey plans, they can be evaluated using conditions) and maximizing
value of information. Please note that several functions depend on the
'Gurobi' optimization software (available from <https://www.gurobi.com>).
Additionally, the 'JAGS' software (available from
<https://mcmc-jags.sourceforge.io/>) is required to fit hierarchical
generalized linear models.

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
