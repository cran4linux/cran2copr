%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MSmix
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Finite Mixtures of Mallows Models with Spearman Distance for Full and Partial Rankings

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-nnet >= 7.3.19
BuildRequires:    R-methods >= 4.3.1
BuildRequires:    R-stats >= 4.3.1
BuildRequires:    R-CRAN-ggplot2 >= 3.4.4
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-BayesMallows >= 2.0.1
BuildRequires:    R-CRAN-fields >= 15.2.0
BuildRequires:    R-CRAN-bmixture >= 1.7
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-scales >= 1.3.0
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.3
BuildRequires:    R-CRAN-rlang >= 1.1.3
BuildRequires:    R-CRAN-factoextra >= 1.0.7
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-Rankcluster >= 0.98.0
BuildRequires:    R-CRAN-reshape >= 0.8.9
BuildRequires:    R-CRAN-gmp >= 0.7.4
BuildRequires:    R-CRAN-spsUtil >= 0.2.2
BuildRequires:    R-CRAN-ggbump >= 0.1.0
Requires:         R-CRAN-nnet >= 7.3.19
Requires:         R-methods >= 4.3.1
Requires:         R-stats >= 4.3.1
Requires:         R-CRAN-ggplot2 >= 3.4.4
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-BayesMallows >= 2.0.1
Requires:         R-CRAN-fields >= 15.2.0
Requires:         R-CRAN-bmixture >= 1.7
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-scales >= 1.3.0
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-RColorBrewer >= 1.1.3
Requires:         R-CRAN-rlang >= 1.1.3
Requires:         R-CRAN-factoextra >= 1.0.7
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-Rankcluster >= 0.98.0
Requires:         R-CRAN-reshape >= 0.8.9
Requires:         R-CRAN-gmp >= 0.7.4
Requires:         R-CRAN-spsUtil >= 0.2.2
Requires:         R-CRAN-ggbump >= 0.1.0

%description
Fit and analysis of finite Mixtures of Mallows models with Spearman
Distance for full and partial rankings with arbitrary missing positions.
Inference is conducted within the maximum likelihood framework via
Expectation-Maximization algorithms. Estimation uncertainty is tackled via
diverse versions of bootstrapped and asymptotic confidence intervals. The
most relevant reference of the methods is Crispino, Mollica, Astuti and
Tardella (2023) <doi:10.1007/s11222-023-10266-8>.

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
