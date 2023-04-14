%global __brp_check_rpaths %{nil}
%global packname  lest
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Vectorised Nested if-else Statements Similar to CASE WHEN in'SQL'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Functions for vectorised conditional recoding of variables. case_when()
enables you to vectorise multiple if and else statements (like 'CASE WHEN'
in 'SQL'). if_else() is a stricter and more predictable version of
ifelse() in 'base' that preserves attributes. These functions are forked
from 'dplyr' with all package dependencies removed and behave identically
to the originals.

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
