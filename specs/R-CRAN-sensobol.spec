%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sensobol
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Variance-Based Sensitivity Indices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-Rdpack >= 2.1
BuildRequires:    R-CRAN-Rfast >= 2.0.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-boot >= 1.3.20
BuildRequires:    R-CRAN-deSolve >= 1.27
BuildRequires:    R-CRAN-randtoolbox >= 1.17.1
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-lhs >= 1.0.2
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-matrixStats >= 0.54.0
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-Rdpack >= 2.1
Requires:         R-CRAN-Rfast >= 2.0.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-boot >= 1.3.20
Requires:         R-CRAN-deSolve >= 1.27
Requires:         R-CRAN-randtoolbox >= 1.17.1
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-lhs >= 1.0.2
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-matrixStats >= 0.54.0
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
It allows to rapidly compute, bootstrap and plot up to fourth-order
Sobol'-based sensitivity indices using several state-of-the-art first and
total-order estimators. Sobol' indices can be computed either for models
that yield a scalar as a model output or for systems of differential
equations. The package also provides a suit of benchmark tests functions
and several options to obtain publication-ready figures of the model
output uncertainty and sensitivity-related analysis. An overview of the
package can be found in Puy et al. (2022) <doi:10.18637/jss.v102.i05>.

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
