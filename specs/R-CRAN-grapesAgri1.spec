%global packname  grapesAgri1
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Shiny Apps for Agricultural Research Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.5.0
BuildRequires:    R-datasets >= 4.0.4
BuildRequires:    R-grid >= 4.0.4
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-rmarkdown >= 2.7
BuildRequires:    R-CRAN-devtools >= 2.4.1
BuildRequires:    R-CRAN-Rdpack >= 2.1.2
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-knitr >= 1.31
BuildRequires:    R-CRAN-agricolae >= 1.3.5
BuildRequires:    R-CRAN-pastecs >= 1.3.21
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.4
BuildRequires:    R-CRAN-shinycssloaders >= 1.0.0
BuildRequires:    R-CRAN-shinyWidgets >= 0.6.0
BuildRequires:    R-CRAN-gridGraphics >= 0.5.1
BuildRequires:    R-CRAN-ggpubr >= 0.4.0
Requires:         R-CRAN-Hmisc >= 4.5.0
Requires:         R-datasets >= 4.0.4
Requires:         R-grid >= 4.0.4
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-rmarkdown >= 2.7
Requires:         R-CRAN-devtools >= 2.4.1
Requires:         R-CRAN-Rdpack >= 2.1.2
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-knitr >= 1.31
Requires:         R-CRAN-agricolae >= 1.3.5
Requires:         R-CRAN-pastecs >= 1.3.21
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.4
Requires:         R-CRAN-shinycssloaders >= 1.0.0
Requires:         R-CRAN-shinyWidgets >= 0.6.0
Requires:         R-CRAN-gridGraphics >= 0.5.1
Requires:         R-CRAN-ggpubr >= 0.4.0

%description
Allows user to have graphical user interface to perform analysis of
Agricultural experimental data. On using the functions in this package a
Interactive User Interface will pop up. Apps Works by simple upload of
files in CSV format.

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
