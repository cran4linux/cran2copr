%global packname  SuperGauss
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Superfast Likelihood Inference for Stationary Gaussian Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel >= 3.1.2
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-fftw 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-fftw 

%description
Likelihood evaluations for stationary Gaussian time series are typically
obtained via the Durbin-Levinson algorithm, which scales as O(n^2) in the
number of time series observations.  This package provides a "superfast"
O(n log^2 n) algorithm written in C++, crossing over with Durbin-Levinson
around n = 300.  Efficient implementations of the score and Hessian
functions are also provided, leading to superfast versions of inference
algorithms such as Newton-Raphson and Hamiltonian Monte Carlo.  The C++
code provides a Toeplitz matrix class packaged as a header-only library,
to simplify low-level usage in other packages and outside of R.

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
