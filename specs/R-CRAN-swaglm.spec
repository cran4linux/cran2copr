%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  swaglm
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Sparse Wrapper Algorithm for Generalized Linear Models and Testing Procedures for Network of Highly Predictive Variables

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-fastglm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-fastglm 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-fields 

%description
Provides a fast implementation of the SWAG algorithm for Generalized
Linear Models which allows to perform a meta-learning procedure that
combines screening and wrapper methods to find a set of extremely
low-dimensional attribute combinations. The package then performs test on
the network of selected models to identify the variables that are highly
predictive by using entropy-based network measures.

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
