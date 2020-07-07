%global packname  sft
%global packver   2.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          3%{?dist}
Summary:          Functions for Systems Factorial Technology Analysis of Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-SuppDists 
Requires:         R-methods 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-SuppDists 

%description
A series of tools for analyzing Systems Factorial Technology data.  This
includes functions for plotting and statistically testing capacity
coefficient functions and survivor interaction contrast functions.  Houpt,
Blaha, McIntire, Havig, and Townsend (2013)
<doi:10.3758/s13428-013-0377-3> provide a basic introduction to Systems
Factorial Technology along with examples using the sft R package.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
