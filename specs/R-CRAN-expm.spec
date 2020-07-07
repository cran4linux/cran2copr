%global packname  expm
%global packver   0.999-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.999.4
Release:          3%{?dist}
Summary:          Matrix Exponential, Log, 'etc'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-Matrix 
Requires:         R-methods 

%description
Computation of the matrix exponential, logarithm, sqrt, and related
quantities.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/po
%doc %{rlibdir}/%{packname}/test-tools.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
