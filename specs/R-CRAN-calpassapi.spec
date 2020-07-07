%global packname  calpassapi
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          3%{?dist}
Summary:          R Interface to Access CalPASS API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-stringr 

%description
Implements methods for querying data from CalPASS using its API. CalPASS
Plus.  MMAP API V1. <https://mmap.calpassplus.org/docs/index.html>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
