%global __brp_check_rpaths %{nil}
%global packname  transmdl
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semiparametric Transformation Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-CRAN-survival 

%description
To make the semiparametric transformation models easier to apply in real
studies, we introduce this R package, in which the MLE in transformation
models via an EM algorithm proposed by Zeng D, Lin DY(2007)
<doi:10.1111/j.1369-7412.2007.00606.x> and adaptive lasso method in
transformation models proposed by Liu XX, Zeng D(2013)
<doi:10.1093/biomet/ast029> are implemented. C++ functions are used to
compute complex loops. The coefficient vector and cumulative baseline
hazard function can be estimated, along with the corresponding standard
errors and P values.

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
