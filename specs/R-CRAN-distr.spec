%global packname  distr
%global packver   2.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.0
Release:          2%{?dist}
Summary:          Object Oriented Implementation of Distributions

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-startupmsg 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-startupmsg 
Requires:         R-CRAN-sfsmisc 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-MASS 

%description
S4-classes and methods for distributions.

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
%doc %{rlibdir}/%{packname}/ARITHMETICS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/MASKING
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/TOBEDONE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
