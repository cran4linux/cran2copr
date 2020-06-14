%global packname  searchable
%global packver   0.3.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3.1
Release:          2%{?dist}
Summary:          Tools for Custom Searches / Subsets / Slices of Named R Objects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringi >= 0.4.1
BuildRequires:    R-methods 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringi >= 0.4.1
Requires:         R-methods 

%description
Provides functionality for searching / subsetting and slicing named
objects using 'stringr/i'-style modifiers by case (in)sensitivity, regular
expressions or fixed expressions; searches uses the standard '[' operator
and allows specification of default search behavior to either the search
target (named object) and/or the search pattern.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
