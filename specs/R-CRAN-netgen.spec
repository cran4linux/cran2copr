%global packname  netgen
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Network Generator for Combinatorial Graph Problems

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-BBmisc >= 1.6
BuildRequires:    R-CRAN-checkmate >= 1.5.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.2
BuildRequires:    R-CRAN-igraph >= 0.7.1
BuildRequires:    R-CRAN-stringr >= 0.6.2
BuildRequires:    R-CRAN-lhs >= 0.10
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-CRAN-BBmisc >= 1.6
Requires:         R-CRAN-checkmate >= 1.5.1
Requires:         R-CRAN-mvtnorm >= 1.0.2
Requires:         R-CRAN-igraph >= 0.7.1
Requires:         R-CRAN-stringr >= 0.6.2
Requires:         R-CRAN-lhs >= 0.10
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lpSolve 

%description
Methods for the generation of a wide range of network geographies, e.g.,
grid networks or clustered networks. Useful for the generation of
benchmarking instances for the investigation of, e.g.,
Vehicle-Routing-Problems or Travelling Salesperson Problems.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
