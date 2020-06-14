%global packname  tfCox
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Fits Piecewise Polynomial with Data-Adaptive Knots in Cox Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-survival 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-survival 
Requires:         R-stats 

%description
In Cox's proportional hazard model, covariates are modeled as linear
function and may not be flexible. This package implements additive trend
filtering Cox proportional hazards model as proposed in Jiacheng Wu &
Daniela Witten (2019) "Flexible and Interpretable Models for Survival
Data", Journal of Computational and Graphical Statistics,
<DOI:10.1080/10618600.2019.1592758>. The fitted functions are piecewise
polynomial with adaptively chosen knots.

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
