%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CropWaterBalance
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Climate Water Balance for Irrigation Purposes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.10
Requires:         R-core >= 3.10
BuildArch:        noarch
BuildRequires:    R-CRAN-PowerSDI 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-stats 
Requires:         R-CRAN-PowerSDI 
Requires:         R-CRAN-lubridate 
Requires:         R-stats 

%description
Calculates daily climate water balance for irrigation purposes and also
calculates the reference evapotranspiration (ET) using three methods,
Penman and Monteith (Allen et al. 1998, ISBN:92-5-104219-5); Priestley and
Taylor (1972) <doi:10/cr3qwn>; or Hargreaves and Samani (1985)
<doi:10.13031/2013.26773>.  Users may specify a management allowed
depletion (MAD), which is used to suggest when to irrigate.  The
functionality allows for the use of crop and water stress coefficients as
well.

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
