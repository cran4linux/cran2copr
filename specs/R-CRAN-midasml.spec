%global packname  midasml
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}
Summary:          Estimation and Prediction Methods for High-Dimensional MixedFrequency Time Series Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-quantreg >= 5.34
BuildRequires:    R-parallel >= 3.5.2
BuildRequires:    R-stats >= 3.5.2
BuildRequires:    R-CRAN-optimx >= 2020.4.2
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-doSNOW >= 1.0.18
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-quantreg >= 5.34
Requires:         R-parallel >= 3.5.2
Requires:         R-stats >= 3.5.2
Requires:         R-CRAN-optimx >= 2020.4.2
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-doSNOW >= 1.0.18

%description
The 'midasml' estimation and prediction methods for high dimensional time
series regression models under mixed data sampling data structures using
structured-sparsity penalties and orthogonal polynomials. For more
information on the 'midasml' approach see Babii, Ghysels, and Striaukas
(2020) <arXiv:2005.14057>. Functions that compute MIDAS data structures
were inspired by MIDAS 'Matlab' toolbox (v2.3) written by Eric Ghysels.

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
