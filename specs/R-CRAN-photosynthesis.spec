%global packname  photosynthesis
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Model C3 Photosynthesis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.5.0
BuildRequires:    R-CRAN-checkmate >= 1.9.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-crayon >= 1.3.0
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-future >= 1.10.0
BuildRequires:    R-CRAN-tealeaves >= 1.0.5
BuildRequires:    R-CRAN-gunit >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-units >= 0.6.0
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-tidyselect >= 0.2.5
BuildRequires:    R-CRAN-furrr >= 0.1.0
Requires:         R-methods >= 3.5.0
Requires:         R-CRAN-checkmate >= 1.9.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-crayon >= 1.3.0
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-future >= 1.10.0
Requires:         R-CRAN-tealeaves >= 1.0.5
Requires:         R-CRAN-gunit >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-units >= 0.6.0
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-tidyselect >= 0.2.5
Requires:         R-CRAN-furrr >= 0.1.0

%description
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
trait gradients such as CO2 conductance or photochemistry.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
