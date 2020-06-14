%global packname  totalcensus
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          2%{?dist}
Summary:          Extract Decennial Census and American Community Survey Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-utils >= 3.3.2
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.10.1
BuildRequires:    R-CRAN-purrr >= 0.2.4
Requires:         R-utils >= 3.3.2
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-data.table >= 1.10.1
Requires:         R-CRAN-purrr >= 0.2.4

%description
Download summary files from Census Bureau <https://www2.census.gov/> and
extract data, in particular high resolution data at block, block group,
and tract level, from decennial census and American Community Survey
1-year and 5-year estimates.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
