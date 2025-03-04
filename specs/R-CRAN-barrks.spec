%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  barrks
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Bark Beetle Phenology Using Different Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.7.18
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-base 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-terra >= 1.7.18
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rdpack 
Requires:         R-base 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 

%description
Calculate the bark beetle phenology based on raster data or point-related
data. There are multiple models implemented for two bark beetle species.
The models can be customized and their submodels (onset of infestation,
beetle development, diapause initiation, mortality) can be combined. The
following models are available in the package: PHENIPS-Clim (first-time
release in this package), PHENIPS (Baier et al. 2007)
<doi:10.1016/j.foreco.2007.05.020>, RITY (Ogris et al. 2019)
<doi:10.1016/j.ecolmodel.2019.108775>, CHAPY (Ogris et al. 2020)
<doi:10.1016/j.ecolmodel.2020.109137>, BSO (Jakoby et al. 2019)
<doi:10.1111/gcb.14766>, Lange et al. (2008)
<doi:10.1007/978-3-540-85081-6_32>, Jönsson et al. (2011)
<doi:10.1007/s10584-011-0038-4>. The package may be expanded by models for
other bark beetle species in the future.

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
