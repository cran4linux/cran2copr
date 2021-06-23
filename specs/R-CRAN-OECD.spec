%global __brp_check_rpaths %{nil}
%global packname  OECD
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          3%{?dist}%{?buildtag}
Summary:          Search and Extract Data from the OECD

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods >= 3.2.2
BuildRequires:    R-CRAN-httr >= 0.6.1
BuildRequires:    R-CRAN-rsdmx >= 0.4.7
BuildRequires:    R-CRAN-xml2 >= 0.1.2
Requires:         R-methods >= 3.2.2
Requires:         R-CRAN-httr >= 0.6.1
Requires:         R-CRAN-rsdmx >= 0.4.7
Requires:         R-CRAN-xml2 >= 0.1.2

%description
Search and extract data from the Organization for Economic Cooperation and
Development (OECD).

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
