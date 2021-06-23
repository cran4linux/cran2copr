%global __brp_check_rpaths %{nil}
%global packname  kayadata
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Kaya Identity Data for Nations and Regions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-scales >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.8
BuildRequires:    R-CRAN-tidyr >= 0.8
BuildRequires:    R-CRAN-forcats >= 0.3
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-scales >= 1.0
Requires:         R-CRAN-dplyr >= 0.8
Requires:         R-CRAN-tidyr >= 0.8
Requires:         R-CRAN-forcats >= 0.3

%description
Provides data for Kaya identity variables (population, gross domestic
product, primary energy consumption, and energy-related CO2 emissions) for
the world and for individual nations, and utility functions for looking up
data, plotting trends of Kaya variables, and plotting the fuel mix for a
given country or region. The Kaya identity (Yoichi Kaya and Keiichi
Yokobori, "Environment, Energy, and Economy: Strategies for
Sustainability" (United Nations University Press, 1998) and
<https://en.wikipedia.org/wiki/Kaya_identity>) expresses a nation's or
region's greenhouse gas emissions in terms of its population, per-capita
Gross Domestic Product, the energy intensity of its economy, and the
carbon-intensity of its energy supply.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
