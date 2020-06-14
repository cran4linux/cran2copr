%global packname  COVID19
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          2%{?dist}
Summary:          R Interface to COVID-19 Data Hub

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-wbstats 
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-wbstats 

%description
Unified datasets for a better understanding of COVID-19. The package
collects COVID-19 data across governmental sources, includes policy
measures from 'Oxford COVID-19 Government Response Tracker'
<https://www.bsg.ox.ac.uk/covidtracker>, and extends the dataset via an
interface to 'World Bank Open Data' <https://data.worldbank.org/>, 'Google
Mobility Reports' <https://www.google.com/covid19/mobility/>, 'Apple
Mobility Reports' <https://www.apple.com/covid19/mobility>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
