%global packname  parma
%global packver   1.5-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          3%{?dist}
Summary:          Portfolio Allocation and Risk Management Applications

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-methods 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-corpcor 
Requires:         R-parallel 
Requires:         R-CRAN-truncnorm 

%description
Provision of a set of models and methods for use in the allocation and
management of capital in financial portfolios.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/parma.tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
