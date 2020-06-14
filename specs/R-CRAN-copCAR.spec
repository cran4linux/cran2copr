%global packname  copCAR
%global packver   2.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          2%{?dist}
Summary:          Fitting the copCAR Regression Model for Discrete Areal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-mcmcse 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-mcmcse 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-spam 

%description
Provides tools for fitting the copCAR (Hughes, 2015)
<DOI:10.1080/10618600.2014.948178> regression model for discrete areal
data. Three types of estimation are supported (continuous extension,
composite marginal likelihood, and distributional transform), for three
types of outcomes (Bernoulli, negative binomial, and Poisson).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
