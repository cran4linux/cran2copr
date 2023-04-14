%global __brp_check_rpaths %{nil}
%global packname  ICcalib
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          3%{?dist}%{?buildtag}
Summary:          Cox Model with Interval-Censored Starting Time of a Covariate

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-icenReg 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-ICsurv 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-survival 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-icenReg 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-ICsurv 
Requires:         R-CRAN-msm 
Requires:         R-MASS 

%description
Calibration and risk-set calibration methods for fitting Cox proportional
hazard model when a binary covariate is measured intermittently. Methods
include functions to fit calibration models from interval-censored data
and modified partial likelihood for the proportional hazard model, Nevo et
al. (2018+) <arXiv:1801.01529>.

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
