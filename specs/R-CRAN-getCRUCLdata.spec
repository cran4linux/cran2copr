%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  getCRUCLdata
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          'CRU' 'CL' v. 2.0 Climatology Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-hoardr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-hoardr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-terra 
Requires:         R-utils 

%description
Provides functions that automate downloading and importing University of
East Anglia Climate Research Unit ('CRU') 'CL' v. 2.0 climatology data,
facilitates the calculation of minimum temperature and maximum temperature
and formats the data into a data.table object or a list of 'terra' 'rast'
objects for use.  'CRU' 'CL' v. 2.0 data are a gridded climatology of
1961-1990 monthly means released in 2002 and cover all land areas
(excluding Antarctica) at 10 arc minutes (0.1666667 degree) resolution.
For more information see the description of the data provided by the
University of East Anglia Climate Research Unit,
<https://crudata.uea.ac.uk/cru/data/hrg/tmc/readme.txt>.

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
