%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aopdata
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data from the 'Access to Opportunities Project (AOP)'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.0.0
BuildRequires:    R-CRAN-sf >= 0.9.3
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 5.0.0
Requires:         R-CRAN-sf >= 0.9.3
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-utils 

%description
Download data from the 'Access to Opportunities Project (AOP)'. The
'aopdata' package brings annual estimates of access to employment, health,
education and social assistance services by transport mode, as well as
data on the spatial distribution of population, jobs, health care, schools
and social assistance facilities at a fine spatial resolution for all
cities included in the project. More info on the 'AOP' website
<https://www.ipea.gov.br/acessooportunidades/en/>.

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
