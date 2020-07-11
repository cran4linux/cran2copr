%global packname  SLOPE
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Sorted L1 Penalized Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.850.1.0
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-lattice 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-foreach 
Requires:         R-lattice 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Efficient implementations for Sorted L-One Penalized Estimation (SLOPE):
generalized linear models regularized with the sorted L1-norm (Bogdan et
al. (2015) <doi:10/gfgwzt>). Supported models include ordinary
least-squares regression, binomial regression, multinomial regression, and
Poisson regression. Both dense and sparse predictor matrices are
supported. In addition, the package features predictor screening rules
that enable fast and efficient solutions to high-dimensional problems.

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
