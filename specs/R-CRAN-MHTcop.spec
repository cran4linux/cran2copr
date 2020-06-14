%global packname  MHTcop
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Tests Controlling the FDR / FWER under Certain Copula Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-stabledist 
BuildRequires:    R-CRAN-MCMCpack 
Requires:         R-stats 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-stabledist 
Requires:         R-CRAN-MCMCpack 

%description
Implements tests controlling the false discovery rate (FDR) / family-wise
error rate (FWER) for some copula models.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
