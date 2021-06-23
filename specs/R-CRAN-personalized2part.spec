%global __brp_check_rpaths %{nil}
%global packname  personalized2part
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Two-Part Estimation of Treatment Rules for Semi-Continuous Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-personalized 
BuildRequires:    R-CRAN-HDtweedie 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-personalized 
Requires:         R-CRAN-HDtweedie 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-foreach 
Requires:         R-methods 

%description
Implements the methodology of Huling, Smith, and Chen (2020)
<doi:10.1080/01621459.2020.1801449>, which allows for subgroup
identification for semi-continuous outcomes by estimating individualized
treatment rules. It uses a two-part modeling framework to handle
semi-continuous data by separately modeling the positive part of the
outcome and an indicator of whether each outcome is positive, but still
results in a single treatment rule. High dimensional data is handled with
a cooperative lasso penalty, which encourages the coefficients in the two
models to have the same sign.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
