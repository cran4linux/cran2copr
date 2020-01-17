%global packname  cdata
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Fluid Data Transformations

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-wrapr >= 1.9.3
BuildRequires:    R-CRAN-rquery >= 1.4.0
BuildRequires:    R-CRAN-rqdatatable >= 1.2.4
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-wrapr >= 1.9.3
Requires:         R-CRAN-rquery >= 1.4.0
Requires:         R-CRAN-rqdatatable >= 1.2.4
Requires:         R-methods 
Requires:         R-stats 

%description
Supplies higher-order coordinatized data specification and fluid transform
operators that include pivot and anti-pivot as special cases. The
methodology is describe in 'Zumel', 2018, "Fluid data reshaping with
'cdata'",
<http://winvector.github.io/FluidData/FluidDataReshapingWithCdata.html> ,
doi:10.5281/zenodo.1173299 . This package introduces the idea of explicit
control table specification of data transforms. Works on in-memory data or
on remote data using 'rquery' and 'SQL' database interfaces.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/unit_tests
%{rlibdir}/%{packname}/INDEX
