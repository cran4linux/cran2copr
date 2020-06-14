%global packname  FastKM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          A Fast Multiple-Kernel Method Based on a Low-Rank Approximation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-rARPACK 
Requires:         R-stats 
Requires:         R-methods 

%description
A computationally efficient and statistically rigorous fast Kernel Machine
method for multi-kernel analysis. The approach is based on a low-rank
approximation to the nuisance effect kernel matrices. The algorithm is
applicable to continuous, binary, and survival traits and is implemented
using the existing single-kernel analysis software 'SKAT' and 'coxKM'.
'coxKM' can be obtained from
http://www.hsph.harvard.edu/xlin/software.html.

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
