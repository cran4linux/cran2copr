%global __brp_check_rpaths %{nil}
%global packname  GDINA
%global packver   2.8.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.8
Release:          1%{?dist}%{?buildtag}
Summary:          The Generalized DINA Model Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-CRAN-alabama 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Rsolnp 
Requires:         R-stats 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-utils 

%description
A set of psychometric tools for cognitive diagnosis modeling based on the
generalized deterministic inputs, noisy and gate (G-DINA) model by de la
Torre (2011) <DOI:10.1007/s11336-011-9207-7> and its extensions, including
the sequential G-DINA model by Ma and de la Torre (2016)
<DOI:10.1111/bmsp.12070> for polytomous responses, and the polytomous
G-DINA model by Chen and de la Torre <DOI:10.1177/0146621613479818> for
polytomous attributes. Joint attribute distribution can be independent,
saturated, higher-order, loglinear smoothed or structured. Q-matrix
validation, item and model fit statistics, model comparison at test and
item level and differential item functioning can also be conducted. A
graphical user interface is also provided. For tutorials, please check Ma
and de la Torre (2020) <DOI:10.18637/jss.v093.i14>, Ma and de la Torre
(2019) <DOI:10.1111/emip.12262>, Ma (2019)
<DOI:10.1007/978-3-030-05584-4_29> and de la Torre and Akbay (2019).

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
