%global packname  sociome
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Operationalizing Social Determinants of Health Data forResearchers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mice >= 3.7.0
BuildRequires:    R-CRAN-psych >= 1.9.12.31
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-tidycensus >= 0.9.2
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-censusapi >= 0.6.0
BuildRequires:    R-CRAN-rlang >= 0.4.3
BuildRequires:    R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-mice >= 3.7.0
Requires:         R-CRAN-psych >= 1.9.12.31
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-tidycensus >= 0.9.2
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-censusapi >= 0.6.0
Requires:         R-CRAN-rlang >= 0.4.3
Requires:         R-CRAN-purrr >= 0.3.3

%description
Accesses raw data via API and calculates social determinants of health
measures for user-specified locations in the US, returning them in
tidyverse- and sf-compatible data frames.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
