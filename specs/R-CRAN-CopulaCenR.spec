%global packname  CopulaCenR
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}
Summary:          Copula-Based Regression Models for Bivariate Censored Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-icenReg 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-survival 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-icenReg 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-pracma 
Requires:         R-survival 

%description
Copula-based regression models for bivariate censored data, including
bivariate right-censored data and bivariate interval-censored data.
Currently supports Clayton, Gumbel, Frank, Joe, AMH and Copula2 copula
models. For marginal models, it supports parametric (Weibull, Loglogistic,
Gompertz) and semiparametric (Cox and transformation) models. Includes
methods for convenient prediction and plotting. Also provides a bivariate
time-to-event simulation function. Method details can be found in Sun
et.al. (2018) < doi:10.1007/s10985-018-09459-5> and Sun et.al (2019)
<arXiv:1901.01918>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
