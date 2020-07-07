%global packname  TTR
%global packver   0.23-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.23.6
Release:          3%{?dist}
Summary:          Technical Trading Rules

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-xts >= 0.10.0
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-xts >= 0.10.0
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-curl 

%description
Functions and data to construct technical trading rules with R.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
