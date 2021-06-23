%global __brp_check_rpaths %{nil}
%global packname  skpr
%global packver   0.66.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.66.5
Release:          1%{?dist}%{?buildtag}
Summary:          Design of Experiments Suite: Generate and Evaluate Optimal Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-rintrojs 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-shiny 
Requires:         R-utils 
Requires:         R-CRAN-iterators 
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-rintrojs 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-future 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-car 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lmerTest 
Requires:         R-methods 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-scales 

%description
Generates and evaluates D, I, A, Alias, E, T, and G optimal designs.
Supports generation and evaluation of blocked and
split/split-split/.../N-split plot designs. Includes parametric and Monte
Carlo power evaluation functions, and supports calculating power for
censored responses. Provides a framework to evaluate power using functions
provided in other packages or written by the user. Includes a Shiny
graphical user interface that displays the underlying code used to create
and evaluate the design to improve ease-of-use and make analyses more
reproducible.

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
