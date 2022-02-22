%global __brp_check_rpaths %{nil}
%global packname  SPSP
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Selection by Partitioning the Solution Paths

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-lars 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-lars 

%description
An implementation of the feature Selection procedure by Partitioning the
entire Solution Paths (namely SPSP) to identify the relevant features
rather than using a single tuning parameter. By utilizing the entire
solution paths, this procedure can obtain better selection accuracy than
the commonly used approach of selecting only one tuning parameter based on
existing criteria, cross-validation (CV), generalized CV, AIC, BIC, and
extended BIC (Liu, Y., & Wang, P. (2018) <doi:10.1214/18-EJS1434>). It is
more stable and accurate (low false positive and false negative rates)
than other variable selection approaches. In addition, it can be flexibly
coupled with the solution paths of Lasso, adaptive Lasso, ridge
regression, and other penalized estimators.

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
