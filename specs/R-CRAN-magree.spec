%global packname  magree
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Implements the O'Connell-Dobson-Schouten Estimators of Agreementfor Multiple Observers

License:          GPL-3 | GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
Requires:         R-graphics 

%description
Implements an interface to the legacy Fortran code from O'Connell and
Dobson (1984) <DOI:10.2307/2531148>. Implements Fortran 77 code for the
methods developed by Schouten (1982)
<DOI:10.1111/j.1467-9574.1982.tb00774.x>. Includes estimates of average
agreement for each observer and average agreement for each subject.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
