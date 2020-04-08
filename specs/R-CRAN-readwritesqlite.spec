%global packname  readwritesqlite
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Enhanced Reading and Writing for 'SQLite' Databases

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-tibble 

%description
Reads and writes data frames to 'SQLite' databases while preserving time
zones (for POSIXct columns), projections (for 'sfc' columns), units (for
'units' columns), levels (for factors and ordered factors) and classes for
logical, Date and 'hms' columns.  It also logs changes to tables and
provides more informative error messages.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
