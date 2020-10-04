%global packname  childesr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Accessing the 'CHILDES' Database

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-dbplyr >= 1.2.1
BuildRequires:    R-CRAN-DBI >= 0.8
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-RMySQL >= 0.10.14
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-dbplyr >= 1.2.1
Requires:         R-CRAN-DBI >= 0.8
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-RMySQL >= 0.10.14

%description
Tools for connecting to 'CHILDES', an open repository for transcripts of
parent-child interaction. For more information on the underlying data, see
<http://childes-db.stanford.edu>.

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
