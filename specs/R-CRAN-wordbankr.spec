%global packname  wordbankr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Accessing the Wordbank Database

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-dbplyr >= 1.1.0
BuildRequires:    R-CRAN-robustbase >= 0.92
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-tidyr >= 0.7.2
BuildRequires:    R-CRAN-DBI >= 0.7
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-RMySQL >= 0.10.13
BuildRequires:    R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-dbplyr >= 1.1.0
Requires:         R-CRAN-robustbase >= 0.92
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-tidyr >= 0.7.2
Requires:         R-CRAN-DBI >= 0.7
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-RMySQL >= 0.10.13
Requires:         R-CRAN-rlang >= 0.1.2

%description
Tools for connecting to Wordbank, an open repository for developmental
vocabulary data.

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
