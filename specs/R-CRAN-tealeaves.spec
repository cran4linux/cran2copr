%global __brp_check_rpaths %{nil}
%global packname  tealeaves
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Solve for Leaf Temperature Using Energy Balance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.5.0
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-magrittr >= 1.5.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-crayon >= 1.3.0
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-future >= 1.10.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-units >= 0.6.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-furrr >= 0.1.0
Requires:         R-methods >= 3.5.0
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-magrittr >= 1.5.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-crayon >= 1.3.0
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-future >= 1.10.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-units >= 0.6.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-furrr >= 0.1.0

%description
Implements models of leaf temperature using energy balance. It uses units
to ensure that parameters are properly specified and transformed before
calculations. It allows separate lower and upper surface conductances to
heat and water vapour, so sensible and latent heat loss are calculated for
each surface separately as in Foster and Smith (1986)
<doi:10.1111/j.1365-3040.1986.tb02108.x>. It's straightforward to model
leaf temperature over environmental gradients such as light, air
temperature, humidity, and wind. It can also model leaf temperature over
trait gradients such as leaf size or stomatal conductance. Other
references are Monteith and Unsworth (2013, ISBN:9780123869104), Nobel
(2009, ISBN:9780123741431), and Okajima et al. (2012)
<doi:10.1007/s11284-011-0905-5>.

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
