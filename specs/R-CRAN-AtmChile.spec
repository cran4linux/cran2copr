%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AtmChile
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Download Air Quality and Meteorological Information of Chile

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-openair 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-openair 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-DT 

%description
Download air quality and meteorological information of Chile from the
National Air Quality System (S.I.N.C.A.)<https://sinca.mma.gob.cl/>
dependent on the Ministry of the Environment and the Meteorological
Directorate of Chile (D.M.C.)<https://www.meteochile.gob.cl/> dependent on
the Directorate General of Civil Aeronautics.

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
