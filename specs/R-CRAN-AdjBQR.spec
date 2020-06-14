%global packname  AdjBQR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Adjusted Bayesian Quantile Regression Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-MHadaptive 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-survival 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-MHadaptive 
Requires:         R-CRAN-coda 
Requires:         R-survival 

%description
Adjusted inference for Bayesian quantile regression based on asymmetric
Laplace working likelihood, for details see Yang, Y., Wang, H. and He, X.
(2015), Posterior inference in Bayesian quantile regression with
asymmetric Laplace likelihood, International Statistical Review, 2015
<doi:10.1111/insr.12114>.

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
