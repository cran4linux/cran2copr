%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pandemonium
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          High Dimensional Analysis in Linked Spaces

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-detourr >= 0.2.0
BuildRequires:    R-CRAN-tourr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-alphahull 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-shinyFeedback 
BuildRequires:    R-CRAN-ggpcp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-detourr >= 0.2.0
Requires:         R-CRAN-tourr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-crosstalk 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-alphahull 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-shinyFeedback 
Requires:         R-CRAN-ggpcp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-viridis 

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
