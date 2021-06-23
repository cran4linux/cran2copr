%global __brp_check_rpaths %{nil}
%global packname  qoma.smuggler
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Transport Data and Commands Across the 'FAME' / 'R' Border

License:          AGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-rhli >= 0.0.2
BuildRequires:    R-methods 
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-rhli >= 0.0.2
Requires:         R-methods 

%description
Transport data and commands across the 'FAME'
<https://fame.sungard.com/support.html> / 'R' border. A set of utilities
for: reading 'FAME' databases into 'R'; writing 'R' data into 'FAME'
databases; executing 'FAME' commands in 'R' environment; and, executing
'R' commands from the 'FAME' environment.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
