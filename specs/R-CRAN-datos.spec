%global packname  datos
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          2%{?dist}
Summary:          Traduce al Español Varios Conjuntos de Datos de Práctica

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-babynames 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-fueleconomy 
BuildRequires:    R-CRAN-gapminder 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Lahman 
BuildRequires:    R-CRAN-nasaweather 
BuildRequires:    R-CRAN-nycflights13 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-babynames 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-fueleconomy 
Requires:         R-CRAN-gapminder 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Lahman 
Requires:         R-CRAN-nasaweather 
Requires:         R-CRAN-nycflights13 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-yaml 

%description
Provee una versión traducida de los siguientes conjuntos de datos:
'airlines', 'airports', 'AwardsManagers', 'babynames', 'Batting',
'diamonds', 'faithful', 'fueleconomy', 'Fielding', 'flights', 'gapminder',
'gss_cat', 'iris', 'Managers', 'mpg', 'mtcars', 'atmos', 'People,
'Pitching', 'planes', 'presidential', 'table1', 'table2', 'table3',
'table4a', 'table4b', 'table5', 'vehicles', 'weather', 'who'.  English: It
provides a Spanish translated version of the datasets listed above.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/specs
%{rlibdir}/%{packname}/INDEX
