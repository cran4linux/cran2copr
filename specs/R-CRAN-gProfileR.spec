%global packname  gProfileR
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}
Summary:          Interface to the 'g:Profiler' Toolkit

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-plyr 
Requires:         R-utils 

%description
This package has been deprecated and will not be updated. New users should
use the package 'gprofiler2'
(<https://CRAN.R-project.org/package=gprofiler2>) for up-to-date data and
improved functionality. Functional enrichment analysis, gene identifier
conversion and mapping homologous genes across related organisms via the
'g:Profiler' toolkit (<https://biit.cs.ut.ee/gprofiler/>).

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
