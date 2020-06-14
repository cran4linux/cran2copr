%global packname  popsom
%global packver   4.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.1
Release:          2%{?dist}
Summary:          Functions for Constructing and Evaluating Self-Organizing Maps

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-som 
BuildRequires:    R-class 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-som 
Requires:         R-class 
Requires:         R-CRAN-fields 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 

%description
State of the art functions for constructing and evaluating self-organizing
maps.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
