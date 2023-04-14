%global __brp_check_rpaths %{nil}
%global packname  glassdoor
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to 'Glassdoor' API

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-httr 

%description
Interacts with the 'Glassdoor' API
<https://www.glassdoor.com/developer/index.htm>. Allows the user to search
job statistics, employer statistics, and job progression, where
'Glassdoor' provides a breakdown of other jobs a person did after their
current one.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
