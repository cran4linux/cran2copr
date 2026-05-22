%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pandemonium
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          High Dimensional Analysis in Linked Spaces

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.12.0
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-tibble >= 3.3.1
BuildRequires:    R-CRAN-alphahull >= 2.5
BuildRequires:    R-CRAN-magrittr >= 2.0.4
BuildRequires:    R-CRAN-tidyr >= 1.3.2
BuildRequires:    R-CRAN-tourr >= 1.2.6
BuildRequires:    R-CRAN-crosstalk >= 1.2.2
BuildRequires:    R-CRAN-tidyselect >= 1.2.1
BuildRequires:    R-CRAN-shinythemes >= 1.2.0
BuildRequires:    R-CRAN-dendextend >= 1.19.1
BuildRequires:    R-CRAN-shiny >= 1.13.0
BuildRequires:    R-CRAN-rlang >= 1.1.7
BuildRequires:    R-CRAN-viridis >= 0.6.5
BuildRequires:    R-CRAN-shinyFeedback >= 0.4.0
BuildRequires:    R-CRAN-DT >= 0.34.0
BuildRequires:    R-CRAN-uwot >= 0.2.4
BuildRequires:    R-CRAN-detourr >= 0.2.0
BuildRequires:    R-CRAN-ggpcp >= 0.2.0
BuildRequires:    R-CRAN-Rtsne >= 0.17
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fpc 
Requires:         R-CRAN-plotly >= 4.12.0
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-tibble >= 3.3.1
Requires:         R-CRAN-alphahull >= 2.5
Requires:         R-CRAN-magrittr >= 2.0.4
Requires:         R-CRAN-tidyr >= 1.3.2
Requires:         R-CRAN-tourr >= 1.2.6
Requires:         R-CRAN-crosstalk >= 1.2.2
Requires:         R-CRAN-tidyselect >= 1.2.1
Requires:         R-CRAN-shinythemes >= 1.2.0
Requires:         R-CRAN-dendextend >= 1.19.1
Requires:         R-CRAN-shiny >= 1.13.0
Requires:         R-CRAN-rlang >= 1.1.7
Requires:         R-CRAN-viridis >= 0.6.5
Requires:         R-CRAN-shinyFeedback >= 0.4.0
Requires:         R-CRAN-DT >= 0.34.0
Requires:         R-CRAN-uwot >= 0.2.4
Requires:         R-CRAN-detourr >= 0.2.0
Requires:         R-CRAN-ggpcp >= 0.2.0
Requires:         R-CRAN-Rtsne >= 0.17
Requires:         R-stats 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fpc 

%description
A 'shiny' GUI that performs high dimensional cluster analysis. This tool
performs data preparation, clustering and visualisation within a dynamic
GUI. With interactive methods allowing the user to change settings all
without having to to leave the GUI. An earlier version of this package was
described in Laa and Valencia (2022)
<doi:10.1140/epjp/s13360-021-02310-1>.

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
