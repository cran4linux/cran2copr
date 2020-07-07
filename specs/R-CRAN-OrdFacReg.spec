%global packname  OrdFacReg
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          3%{?dist}
Summary:          Least Squares, Logistic, and Cox-Regression with OrderedPredictors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-eha 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
Requires:         R-survival 
Requires:         R-CRAN-eha 
Requires:         R-MASS 
Requires:         R-stats 

%description
In biomedical studies, researchers are often interested in assessing the
association between one or more ordinal explanatory variables and an
outcome variable, at the same time adjusting for covariates of any type.
The outcome variable may be continuous, binary, or represent censored
survival times. In the absence of a precise knowledge of the response
function, using monotonicity constraints on the ordinal variables improves
efficiency in estimating parameters, especially when sample sizes are
small. This package implements an active set algorithm that efficiently
computes such estimators.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
