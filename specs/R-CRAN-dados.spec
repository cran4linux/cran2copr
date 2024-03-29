%global __brp_check_rpaths %{nil}
%global packname  dados
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Translate Datasets to Portuguese

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-AmesHousing 
BuildRequires:    R-CRAN-babynames 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-fueleconomy 
BuildRequires:    R-CRAN-gapminder 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Lahman 
BuildRequires:    R-CRAN-palmerpenguins 
BuildRequires:    R-CRAN-nasaweather 
BuildRequires:    R-CRAN-nycflights13 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-pixarfilms 
Requires:         R-CRAN-AmesHousing 
Requires:         R-CRAN-babynames 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-fueleconomy 
Requires:         R-CRAN-gapminder 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Lahman 
Requires:         R-CRAN-palmerpenguins 
Requires:         R-CRAN-nasaweather 
Requires:         R-CRAN-nycflights13 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-pixarfilms 

%description
Este pacote traduz os seguintes conjuntos de dados: 'airlines',
'airports', 'ames_raw', 'AwardsManagers', 'babynames', 'Batting',
'diamonds', 'faithful', 'fueleconomy', 'Fielding', 'flights', 'gapminder',
'gss_cat', 'iris', 'Managers', 'mpg', 'mtcars', 'atmos', 'penguins',
'People, 'Pitching', 'pixarfilms','planes', 'presidential', 'table1',
'table2', 'table3', 'table4a', 'table4b', 'table5', 'vehicles', 'weather',
'who'.  English: It provides a Portuguese translated version of the
datasets listed above.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
