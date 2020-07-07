%global packname  atmopt
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Analysis-of-Marginal-Tail-Means

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DoE.base 
BuildRequires:    R-CRAN-hierNet 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-DoE.base 
Requires:         R-CRAN-hierNet 
Requires:         R-CRAN-gtools 

%description
Provides functions for implementing the Analysis-of-marginal-Tail-Means
(ATM) method, a robust optimization method for discrete black-box
optimization. Technical details can be found in Mak and Wu (2018+)
<arXiv:1712.03589>. This work was supported by USARO grant
W911NF-17-1-0007.

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
