%global packname  hutils
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Miscellaneous R Functions and Aliases

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats < 4.0.0
BuildRequires:    R-utils < 4.0.0
BuildRequires:    R-grDevices < 4.0.0
BuildRequires:    R-CRAN-data.table < 2.0.0
BuildRequires:    R-CRAN-magrittr < 2.0.0
BuildRequires:    R-CRAN-fastmatch < 2.0.0
Requires:         R-stats < 4.0.0
Requires:         R-utils < 4.0.0
Requires:         R-grDevices < 4.0.0
Requires:         R-CRAN-data.table < 2.0.0
Requires:         R-CRAN-magrittr < 2.0.0
Requires:         R-CRAN-fastmatch < 2.0.0

%description
Provides utility functions for, and drawing on, the 'data.table' package.
The package also collates useful miscellaneous functions extending base R
not available elsewhere. The name is a portmanteau of 'utils' and the
author.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
