%global packname  expectreg
%global packver   0.51
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.51
Release:          1%{?dist}%{?buildtag}
Summary:          Expectile and Quantile Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-mboost >= 2.1.0
BuildRequires:    R-CRAN-colorspace >= 0.97
BuildRequires:    R-CRAN-BayesX >= 0.2.4
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-mboost >= 2.1.0
Requires:         R-CRAN-colorspace >= 0.97
Requires:         R-CRAN-BayesX >= 0.2.4
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-Matrix 
Requires:         R-splines 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-fields 

%description
Expectile and quantile regression of models with nonlinear effects e.g.
spatial, random, ridge using least asymmetric weighed squares / absolutes
as well as boosting; also supplies expectiles for common distributions.

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
