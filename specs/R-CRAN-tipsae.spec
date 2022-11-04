%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tipsae
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Handling Indices and Proportions in Small Area Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-nlme >= 3.1.152
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-shiny >= 1.0.3
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-nlme >= 3.1.152
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-shiny >= 1.0.3
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-broom 
Requires:         R-stats 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rstantools

%description
It allows for mapping proportions and indicators defined on the unit
interval. It implements Beta-based small area methods comprising the
classical Beta regression models, the Flexible Beta model and Zero and/or
One Inflated extensions (Janicki 2020
<doi:10.1080/03610926.2019.1570266>). Such methods, developed within a
Bayesian framework through Stan <https://mc-stan.org/>, come equipped with
a set of diagnostics and complementary tools, visualizing and exporting
functions. A Shiny application with a user-friendly interface can be
launched to further simplify the process.

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
