%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggfacto
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Graphs for Correspondence Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-FactoMineR >= 2.0
BuildRequires:    R-CRAN-withr >= 2.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.0
BuildRequires:    R-CRAN-magrittr >= 1.5.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-tabxplor >= 1.0.3
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-ggrepel >= 0.9.0
BuildRequires:    R-CRAN-ggiraph >= 0.8.2
BuildRequires:    R-CRAN-forcats >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-ggforce >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-FactoMineR >= 2.0
Requires:         R-CRAN-withr >= 2.0.0
Requires:         R-CRAN-gridExtra >= 2.0
Requires:         R-CRAN-magrittr >= 1.5.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-tabxplor >= 1.0.3
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-ggrepel >= 0.9.0
Requires:         R-CRAN-ggiraph >= 0.8.2
Requires:         R-CRAN-forcats >= 0.5.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-ggforce >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-vctrs >= 0.3.0

%description
Readable, complete and pretty graphs for correspondence analysis made with
'FactoMineR'. They can be rendered as interactive 'HTML' plots, showing
useful informations at mouse hover. The interest is not mainly visual but
statistical: it helps the reader to keep in mind the data contained in the
cross-table or Burt table while reading the correspondence analysis, thus
preventing over-interpretation. Most graphs are made with 'ggplot2', which
means that you can use the + syntax to manually add as many graphical
pieces you want, or change theme elements. 3D graphs are made with
'plotly'.

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
