%global packname  hydroscoper
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to the Greek National Data Bank forHydrometeorological Information

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1
BuildRequires:    R-CRAN-pingr >= 2.0
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-stringi >= 1.4
BuildRequires:    R-CRAN-stringr >= 1.4
BuildRequires:    R-CRAN-readr >= 1.3
Requires:         R-CRAN-tibble >= 2.1
Requires:         R-CRAN-pingr >= 2.0
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-stringi >= 1.4
Requires:         R-CRAN-stringr >= 1.4
Requires:         R-CRAN-readr >= 1.3

%description
R interface to the Greek National Data Bank for Hydrological and
Meteorological Information <http://www.hydroscope.gr/>. It covers
Hydroscope's data sources and provides functions to transliterate,
translate and download them into tidy dataframes.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
