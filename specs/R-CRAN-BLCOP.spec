%global packname  BLCOP
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Black-Litterman and Copula Opinion Pooling Frameworks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fPortfolio >= 3011.81
BuildRequires:    R-CRAN-RUnit >= 0.4.22
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-fMultivar 
Requires:         R-CRAN-fPortfolio >= 3011.81
Requires:         R-CRAN-RUnit >= 0.4.22
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-fMultivar 

%description
An implementation of the Black-Litterman Model and Atilio Meucci's copula
opinion pooling framework.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/RUnit
%{rlibdir}/%{packname}/INDEX
