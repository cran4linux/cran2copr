%global packname  gfilinreg
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Fiducial Inference for Low-Dimensional Robust Linear Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-spatstat >= 2.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-EigenR 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-memuse 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-spatstat >= 2.0.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-lazyeval 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-EigenR 
Requires:         R-CRAN-data.table 
Requires:         R-parallel 
Requires:         R-CRAN-memuse 

%description
Fiducial framework for linear regression models allowing normal, Student,
Cauchy, or logistic error terms. Only low-dimensional models are possible,
such as the simple linear regression model, or the one-way ANOVA model
with two factor levels. Reference: Hannig, Lai & Lee (2014)
<doi:10.1016/j.csda.2013.03.003>.

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
