%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AquaBEHER
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Rainy Season Calendar and Soil Water Balance for Agriculture

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 

%description
Computes and integrates daily reference 'evapotranspiration' ('Eto') into
a water balance model, to estimate the calendar of wet-season (Onset,
Cessation and Duration) based on 'agroclimatic' approach, for further
information please refer to Allen 'et al.' (1998, ISBN:92-5-104219-5),
Allen (2005, ISBN:9780784408056), 'Doorenbos' and Pruitt (1975,
ISBN:9251002797) 'Guo et al.' (2016) <doi:10.1016/j.envsoft.2015.12.019>,
Hargreaves and 'Samani' (1985) <doi:10.13031/2013.26773>, Priestley and
Taylor (1972)
<https://journals.ametsoc.org/downloadpdf/journals/mwre/100/2/1520-0493_1972_100_0081_otaosh_2_3_co_2.pdf>.

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
