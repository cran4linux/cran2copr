%global __brp_check_rpaths %{nil}
%global packname  tidygeoRSS
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}%{?buildtag}
Summary:          Tidy GeoRSS

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyRSS >= 2.0.2
BuildRequires:    R-CRAN-jsonlite >= 1.6.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-xml2 >= 1.3.1
BuildRequires:    R-CRAN-strex >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-sf >= 0.9.1
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-anytime >= 0.3.7
BuildRequires:    R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-tidyRSS >= 2.0.2
Requires:         R-CRAN-jsonlite >= 1.6.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-xml2 >= 1.3.1
Requires:         R-CRAN-strex >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-sf >= 0.9.1
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-anytime >= 0.3.7
Requires:         R-CRAN-purrr >= 0.3.3

%description
In order to easily integrate geoRSS data into analysis, 'tidygeoRSS'
parses 'geo' feeds and returns tidy simple features data frames.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
