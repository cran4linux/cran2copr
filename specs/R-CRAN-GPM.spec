%global __brp_check_rpaths %{nil}
%global packname  GPM
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Gaussian Process Modeling of Multi-Response and Possibly NoisyDatasets

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-stats >= 3.5
BuildRequires:    R-parallel >= 3.5
BuildRequires:    R-CRAN-pracma >= 2.1.8
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-randtoolbox >= 1.17
BuildRequires:    R-CRAN-doParallel >= 1.0.14
BuildRequires:    R-CRAN-iterators >= 1.0.10
BuildRequires:    R-lattice >= 0.20.34
BuildRequires:    R-CRAN-lhs >= 0.14
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats >= 3.5
Requires:         R-parallel >= 3.5
Requires:         R-CRAN-pracma >= 2.1.8
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-randtoolbox >= 1.17
Requires:         R-CRAN-doParallel >= 1.0.14
Requires:         R-CRAN-iterators >= 1.0.10
Requires:         R-lattice >= 0.20.34
Requires:         R-CRAN-lhs >= 0.14
Requires:         R-CRAN-Rcpp >= 0.12.19

%description
Provides a general and efficient tool for fitting a response surface to a
dataset via Gaussian processes. The dataset can have multiple responses
and be noisy (with stationary variance). The fitted GP model can predict
the gradient as well. The package is based on the work of Bostanabad, R.,
Kearney, T., Tao, S. Y., Apley, D. W. & Chen, W. (2018) Leveraging the
nugget parameter for efficient Gaussian process modeling. International
Journal for Numerical Methods in Engineering, 114, 501-516.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
