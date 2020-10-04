%global packname  CANSIM2R
%global packver   1.14.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.14.1
Release:          3%{?dist}%{?buildtag}
Summary:          Directly Extracts Complete CANSIM Data Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-downloader 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-Hmisc 
Requires:         R-utils 
Requires:         R-CRAN-downloader 

%description
Extract CANSIM (Statistics Canada) tables and transform them into readily
usable data in panel (wide) format. It can also extract more than one
table at a time and produce the resulting merge by time period and
geographical region.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
