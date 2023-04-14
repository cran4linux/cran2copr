%global __brp_check_rpaths %{nil}
%global packname  dina
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Estimation of DINA Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.200
BuildRequires:    R-CRAN-simcdm >= 0.1.0
BuildRequires:    R-CRAN-rgen 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-simcdm >= 0.1.0

%description
Estimate the Deterministic Input, Noisy "And" Gate (DINA) cognitive
diagnostic model parameters using the Gibbs sampler described by Culpepper
(2015) <doi:10.3102/1076998615595403>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
