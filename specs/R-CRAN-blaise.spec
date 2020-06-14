%global packname  blaise
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          2%{?dist}
Summary:          Read and Write FWF Files in the Blaise Format

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils >= 3.4.1
BuildRequires:    R-tools >= 3.4.1
BuildRequires:    R-methods >= 3.4.1
BuildRequires:    R-stats >= 3.4.1
BuildRequires:    R-CRAN-tibble >= 1.3.3
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 0.7.2
Requires:         R-utils >= 3.4.1
Requires:         R-tools >= 3.4.1
Requires:         R-methods >= 3.4.1
Requires:         R-stats >= 3.4.1
Requires:         R-CRAN-tibble >= 1.3.3
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-dplyr >= 0.7.2

%description
Can be used to read and write a fwf with an accompanying blaise datamodel.
When supplying a datamodel for writing, the dataframe will be
automatically converted to that format and checked for compatibility.
Supports dataframes, tibbles and LaF objects.

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
%{rlibdir}/%{packname}/INDEX
