%global packname  datamart
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          Unified access to your data sources

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-base64 
BuildRequires:    R-CRAN-gsubfn 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-markdown 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-base64 
Requires:         R-CRAN-gsubfn 
Requires:         R-methods 
Requires:         R-CRAN-markdown 

%description
Provides an S4 infrastructure for unified handling of internal datasets
and web based data sources. The package is currently in beta; things may
break, change or go away without warning.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
