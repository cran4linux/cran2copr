%global __brp_check_rpaths %{nil}
%global packname  dmbc
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model Based Clustering of Binary Dissimilarity Measurements

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-parallel >= 3.6.1
BuildRequires:    R-stats4 >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-pcaPP >= 1.9.73
BuildRequires:    R-CRAN-bayesplot >= 1.7.0
BuildRequires:    R-CRAN-MCMCpack >= 1.4.4
BuildRequires:    R-CRAN-robustbase >= 0.93.5
BuildRequires:    R-CRAN-ggrepel >= 0.8.1
BuildRequires:    R-CRAN-modeltools >= 0.2.22
BuildRequires:    R-CRAN-coda >= 0.19.3
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-graphics 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-parallel >= 3.6.1
Requires:         R-stats4 >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-pcaPP >= 1.9.73
Requires:         R-CRAN-bayesplot >= 1.7.0
Requires:         R-CRAN-MCMCpack >= 1.4.4
Requires:         R-CRAN-robustbase >= 0.93.5
Requires:         R-CRAN-ggrepel >= 0.8.1
Requires:         R-CRAN-modeltools >= 0.2.22
Requires:         R-CRAN-coda >= 0.19.3
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-abind 
Requires:         R-graphics 
Requires:         R-tools 

%description
Functions for fitting a Bayesian model for grouping binary dissimilarity
matrices in homogeneous clusters. Currently, it includes methods only for
binary data (<doi:10.18637/jss.v100.i16>).

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
