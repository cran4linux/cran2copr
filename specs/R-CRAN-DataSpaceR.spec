%global packname  DataSpaceR
%global packver   0.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
Release:          3%{?dist}
Summary:          Interface to 'the CAVD DataSpace'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rlabkey >= 2.2.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-Rlabkey >= 2.2.0
Requires:         R-utils 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-data.table 

%description
Provides a convenient API interface to access immunological data within
'the CAVD DataSpace'(<https://dataspace.cavd.org>), a data sharing and
discovery tool that facilitates exploration of HIV immunological data from
pre-clinical and clinical HIV vaccine studies.

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
