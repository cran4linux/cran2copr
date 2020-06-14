%global packname  XKCDdata
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Get XKCD Comic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.3.4
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-glue >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-htmltools >= 0.3.6
BuildRequires:    R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-tibble >= 1.3.4
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-glue >= 1.1.1
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-assertthat >= 0.2.0

%description
Download data from individual XKCD comics, written by Randall Munroe
<https://xkcd.com/>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
