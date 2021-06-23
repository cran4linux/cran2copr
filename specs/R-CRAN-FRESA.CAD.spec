%global __brp_check_rpaths %{nil}
%global packname  FRESA.CAD
%global packver   3.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Selection Algorithms for Computer Aided Diagnosis

License:          LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.10.0
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-miscTools 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.10.0
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-miscTools 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-pROC 

%description
Contains a set of utilities for building and testing statistical models
(linear, logistic,ordinal or COX) for Computer Aided Diagnosis/Prognosis
applications. Utilities include data adjustment, univariate analysis,
model building, model-validation, longitudinal analysis, reporting and
visualization.

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
