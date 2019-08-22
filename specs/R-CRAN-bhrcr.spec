%global packname  bhrcr
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Bayesian Hierarchical Regression on Clearance Rates in thePresence of Lag and Tail Phases

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-CRAN-MCMCpack 
Requires:         R-MASS 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-survival 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-Cairo 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
An implementation of the Bayesian Clearance Estimator (Fogarty et al.
(2015) <doi:10.1111/biom.12307>). It takes serial measurements of a
response on an individual (e.g., parasite load after treatment) that is
decaying over time and performs Bayesian hierarchical regression of the
clearance rates on the given covariates. This package provides tools to
calculate WWARN PCE (WorldWide Antimalarial Resistance Network's Parasite
Clearance Estimator) estimates of the clearance rates as well. A tutorial
appeared in Sharifi-Malvajerdi et al. (2019) <doi:
10.1186/s12936-018-2631-8>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
