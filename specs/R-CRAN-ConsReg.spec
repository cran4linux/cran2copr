%global packname  ConsReg
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Fits Regression & ARMA Models Subject to Constraints to theCoefficient

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-forecast >= 8.0
BuildRequires:    R-CRAN-GA >= 3.0
BuildRequires:    R-CRAN-DEoptim >= 2.2
BuildRequires:    R-CRAN-MCMCpack >= 1.4
BuildRequires:    R-CRAN-FME >= 1.3
BuildRequires:    R-CRAN-nloptr >= 1.2
BuildRequires:    R-CRAN-Rsolnp >= 1.15
BuildRequires:    R-CRAN-data.table >= 1.10
BuildRequires:    R-CRAN-GenSA >= 1.1
BuildRequires:    R-CRAN-rlang >= 0.4
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-adaptMCMC 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-forecast >= 8.0
Requires:         R-CRAN-GA >= 3.0
Requires:         R-CRAN-DEoptim >= 2.2
Requires:         R-CRAN-MCMCpack >= 1.4
Requires:         R-CRAN-FME >= 1.3
Requires:         R-CRAN-nloptr >= 1.2
Requires:         R-CRAN-Rsolnp >= 1.15
Requires:         R-CRAN-data.table >= 1.10
Requires:         R-CRAN-GenSA >= 1.1
Requires:         R-CRAN-rlang >= 0.4
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-adaptMCMC 
Requires:         R-CRAN-Rcpp 

%description
Fits or generalized linear models either a regression with Autoregressive
moving-average (ARMA) errors for time series data. The package makes it
easy to incorporate constraints into the model's coefficients. The model
is specified by an objective function (Gaussian, Binomial or Poisson) or
an ARMA order (p,q), a vector of bound constraints for the coefficients
(i.e beta1 > 0) and the possibility to incorporate restrictions among
coefficients (i.e beta1 > beta2). The references of this packages are the
same as 'stats' package for glm() and arima() functions. See Brockwell, P.
J. and Davis, R. A. (1996, ISBN-10: 9783319298528). For the different
optimizers implemented, it is recommended to consult the documentation of
the corresponding packages.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
