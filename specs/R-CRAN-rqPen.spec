%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rqPen
%global packver   4.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Quantile Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-hqreg 
BuildRequires:    R-CRAN-hrqglas 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-hqreg 
Requires:         R-CRAN-hrqglas 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 

%description
Performs penalized quantile regression with LASSO, elastic net, SCAD and
MCP penalty functions including group penalties. In addition, offers a
group penalty that provides consistent variable selection across
quantiles. Provides a function that automatically generates lambdas and
evaluates different models with cross validation or BIC, including a large
p version of BIC. Below URL provides a link to a work in progress
vignette.

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
