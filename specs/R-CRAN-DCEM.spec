%global __brp_check_rpaths %{nil}
%global packname  DCEM
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering Big Data using Expectation Maximization Star (EM*)Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-MASS >= 7.3.49
BuildRequires:    R-CRAN-mvtnorm >= 1.0.7
BuildRequires:    R-CRAN-matrixcalc >= 1.0.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
Requires:         R-MASS >= 7.3.49
Requires:         R-CRAN-mvtnorm >= 1.0.7
Requires:         R-CRAN-matrixcalc >= 1.0.3
Requires:         R-CRAN-Rcpp >= 1.0.2

%description
Implements the Improved Expectation Maximisation EM* and the traditional
EM algorithm for clustering big data (gaussian mixture models for both
multivariate and univariate datasets). This version implements the faster
alternative EM* that avoids revisiting data by leveraging the heap
structure. The implementation supports both random and K-means++ based
initialization. Reference: Hasan Kurban, Mark Jenne, Mehmet M. Dalkilic
(2016) <doi:10.1007/s41060-017-0062-1>. This work is partially supported
by NCI Grant 1R01CA213466-01.

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
