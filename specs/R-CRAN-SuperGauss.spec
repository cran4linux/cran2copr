%global packname  SuperGauss
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Superfast Likelihood Inference for Stationary Gaussian TimeSeries

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel >= 3.1.2
Requires:         fftw
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fftw 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-stats 
Requires:         R-methods 
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


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
