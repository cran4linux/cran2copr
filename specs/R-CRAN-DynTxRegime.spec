%global packname  DynTxRegime
%global packver   4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3
Release:          1%{?dist}
Summary:          Methods for Estimating Optimal Dynamic Treatment Regimes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-modelObj 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-dfoptim 
Requires:         R-methods 
Requires:         R-CRAN-modelObj 
Requires:         R-stats 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-dfoptim 

%description
Methods to estimate dynamic treatment regimes using Interactive
Q-Learning, Q-Learning, weighted learning, and value-search methods based
on Augmented Inverse Probability Weighted Estimators and Inverse
Probability Weighted Estimators.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
