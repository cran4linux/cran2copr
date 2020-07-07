%global packname  macc
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Mediation Analysis of Causality under Confounding

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-lme4 
Requires:         R-nlme 
Requires:         R-CRAN-optimx 
Requires:         R-MASS 
Requires:         R-CRAN-car 

%description
Performs causal mediation analysis under confounding or correlated errors.
This package includes a single level mediation model, a two-level
mediation model, and a three-level mediation model for data with
hierarchical structures. Under the two/three-level mediation model, the
correlation parameter is identifiable and is estimated based on a
hierarchical-likelihood, a marginal-likelihood or a two-stage method. See
Zhao, Y., & Luo, X. (2014), Estimating Mediation Effects under Correlated
Errors with an Application to fMRI, <arXiv:1410.7217> for details.

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
