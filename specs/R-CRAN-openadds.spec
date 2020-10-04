%global packname  openadds
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Client to Access 'Openaddresses' Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.2
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-readr >= 1.0.0
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-maptools >= 0.8.40
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
BuildRequires:    R-CRAN-crul >= 0.1.6
Requires:         R-CRAN-jsonlite >= 1.2
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-readr >= 1.0.0
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-maptools >= 0.8.40
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-rappdirs >= 0.3.1
Requires:         R-CRAN-crul >= 0.1.6

%description
'Openaddresses' (<https://openaddresses.io/>) client. Search, fetch data,
and combine 'datasets'. Outputs are easy to visualize with base plots,
'ggplot2', or 'leaflet'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/INDEX
