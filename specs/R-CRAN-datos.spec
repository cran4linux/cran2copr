%global packname  datos
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Traduce al Español Varios Conjuntos de Datos de Práctica

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-tibble 

%description
Provee una versión traducida de los siguientes conjuntos de datos:
'airlines', 'airports', 'babynames', 'Batting', 'diamonds', 'faithful',
'flights', 'gapminder', 'gss_cat', 'iris', 'mpg', 'mtcars', 'atmos',
'planes', 'presidential', 'table1', 'table2', 'table3', 'table4a',
'table4b', 'table5', 'vehicles','weather', 'who'. English: It provides a
Spanish translated version of the datasets listed above.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/specs
%{rlibdir}/%{packname}/INDEX
