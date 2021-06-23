%global __brp_check_rpaths %{nil}
%global packname  ggpp
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Grammar Extensions to 'ggplot2'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51.6
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-zoo >= 1.8.8
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-polynom >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-xts >= 0.12.0
BuildRequires:    R-CRAN-generics >= 0.1.0
BuildRequires:    R-grid 
Requires:         R-CRAN-MASS >= 7.3.51.6
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-zoo >= 1.8.8
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-polynom >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-xts >= 0.12.0
Requires:         R-CRAN-generics >= 0.1.0
Requires:         R-grid 

%description
Extensions to 'ggplot2' respecting the grammar of graphics paradigm.
Geomas: geom_table(), geom_plot() and geom_grob() add insets to plots
using native data coordinates, while geom_table_npc(), geom_plot_npc() and
geom_grob_npc() do the same using "npc" coordinates through new aesthetics
"npcx" and "npcy". Statistics: select observations based on 2D density.
Positions: radial nudging away from a center point and nudging away from a
line or curve.

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
