%global packname  dataonderivatives
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}
Summary:          Easily Source Publicly Available Data on Derivatives

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-utils >= 3.3.0
BuildRequires:    R-CRAN-lubridate >= 1.3.3
BuildRequires:    R-CRAN-tibble >= 1.3.0
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-readr >= 1.1.0
BuildRequires:    R-CRAN-assertthat >= 0.1
Requires:         R-utils >= 3.3.0
Requires:         R-CRAN-lubridate >= 1.3.3
Requires:         R-CRAN-tibble >= 1.3.0
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-readr >= 1.1.0
Requires:         R-CRAN-assertthat >= 0.1

%description
Post Global Financial Crisis derivatives reforms have lifted the veil off
over-the-counter (OTC) derivative markets. Swap Execution Facilities
(SEFs) and Swap Data Repositories (SDRs) now publish data on swaps that
are traded on or reported to those facilities (respectively). This package
provides you the ability to get this data from supported sources.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/INDEX
