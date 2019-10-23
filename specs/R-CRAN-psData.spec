%global packname  psData
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Download Regularly Maintained Political Science Data Sets

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-DataCombine 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-xlsx 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-DataCombine 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-xlsx 

%description
This R package includes functions for gathering commonly used and
regularly maintained data set in political science. It also includes
functions for combining components from these data sets into variables
that have been suggested in the literature, but are not regularly
maintained.

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
%{rlibdir}/%{packname}/INDEX
