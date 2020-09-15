%global packname  pense
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Elastic Net S/MM-Estimator of Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.600
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-parallel 

%description
Robust penalized (adaptive) elastic net S and M estimators for linear
regression. The methods are proposed in Cohen Freue, G. V., Kepplinger,
D., Salibián-Barrera, M., and Smucler, E. (2019)
<https://projecteuclid.org/euclid.aoas/1574910036>. The package implements
the extensions and algorithms described in Kepplinger, D. (2020)
<doi:10.14288/1.0392915>.

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
