%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  photosynthesis
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Plant Ecophysiology & Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-graphics >= 4.0.0
BuildRequires:    R-grDevices >= 4.0.0
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-utils >= 4.0.0
BuildRequires:    R-methods >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-nlme >= 3.1.147
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-magrittr >= 1.5.0
BuildRequires:    R-CRAN-glue >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-minpack.lm >= 1.2.1
BuildRequires:    R-CRAN-tealeaves >= 1.0.5
BuildRequires:    R-CRAN-gunit >= 1.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-units >= 0.6.6
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-pkgnet >= 0.4.1
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-furrr >= 0.1.0
Requires:         R-graphics >= 4.0.0
Requires:         R-grDevices >= 4.0.0
Requires:         R-stats >= 4.0.0
Requires:         R-utils >= 4.0.0
Requires:         R-methods >= 3.5.0
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-nlme >= 3.1.147
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-magrittr >= 1.5.0
Requires:         R-CRAN-glue >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-minpack.lm >= 1.2.1
Requires:         R-CRAN-tealeaves >= 1.0.5
Requires:         R-CRAN-gunit >= 1.0.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-units >= 0.6.6
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-pkgnet >= 0.4.1
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-furrr >= 0.1.0

%description
Contains modeling and analytical tools for plant ecophysiology. MODELING:
Simulate C3 photosynthesis using the Farquhar, von Caemmerer, Berry (1980)
<doi:10.1007/BF00386231> model as described in Buckley and Diaz-Espejo
(2015) <doi:10.1111/pce.12459>. It uses units to ensure that parameters
are properly specified and transformed before calculations. Temperature
response functions get automatically "baked" into all parameters based on
leaf temperature following Bernacchi et al. (2002)
<doi:10.1104/pp.008250>. The package includes boundary layer, cuticular,
stomatal, and mesophyll conductances to CO2, which each can vary on the
upper and lower portions of the leaf. Use straightforward functions to
simulate photosynthesis over environmental gradients such as
Photosynthetic Photon Flux Density (PPFD) and leaf temperature, or over
trait gradients such as CO2 conductance or photochemistry. ANALYTICAL
TOOLS: Fit ACi (Farquhar et al. (1980) <doi:10.1007/BF00386231>) and AQ
curves (Marshall & Biscoe (1980) <doi:10.1093/jxb/31.1.29>), temperature
responses (Heskel et al. (2016) <doi:10.1073/pnas.1520282113>; Kruse et
al. (2008) <doi:10.1111/j.1365-3040.2008.01809.x>, Medlyn et al. (2002)
<doi:10.1046/j.1365-3040.2002.00891.x>, Hobbs et al. (2013)
<doi:10.1021/cb4005029>), respiration in the light (Kok (1956)
<doi:10.1016/0006-3002(56)90003-8>, Walker & Ort (2015)
<doi:10.1111/pce.12562>, Yin et al. (2009)
<doi:10.1111/j.1365-3040.2009.01934.x>, Yin et al. (2011)
<doi:10.1093/jxb/err038>), mesophyll conductance (Harley et al. (1992)
<doi:10.1104/pp.98.4.1429>), pressure-volume curves (Koide et al. (2000)
<doi:10.1007/978-94-009-2221-1_9>, Sack et al. (2003)
<doi:10.1046/j.0016-8025.2003.01058.x>, Tyree et al. (1972)
<doi:10.1093/jxb/23.1.267>), hydraulic vulnerability curves (Ogle et al.
(2009) <doi:10.1111/j.1469-8137.2008.02760.x>, Pammenter et al. (1998)
<doi:10.1093/treephys/18.8-9.589>), and tools for running sensitivity
analyses particularly for variables with uncertainty (e.g. g_mc(),
gamma_star(), R_d()).

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
