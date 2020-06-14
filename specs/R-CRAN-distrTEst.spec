%global packname  distrTEst
%global packver   2.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.0
Release:          2%{?dist}
Summary:          Estimation and Testing Classes Based on Package 'distr'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-setRNG >= 2006.2.1
BuildRequires:    R-CRAN-distrSim >= 2.2
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-startupmsg 
BuildRequires:    R-utils 
Requires:         R-CRAN-setRNG >= 2006.2.1
Requires:         R-CRAN-distrSim >= 2.2
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-startupmsg 
Requires:         R-utils 

%description
Evaluation (S4-)classes based on package distr for evaluating procedures
(estimators/tests) at data/simulation in a unified way.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/TOBEDONE
%{rlibdir}/%{packname}/INDEX
