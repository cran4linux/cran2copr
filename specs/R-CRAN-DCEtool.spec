%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DCEtool
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient and Accessible Discrete Choice Experiments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-idefix 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-mlogit 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-dfidx 
BuildRequires:    R-CRAN-adjustedcranlogs 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-idefix 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-mlogit 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-dfidx 
Requires:         R-CRAN-adjustedcranlogs 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 

%description
Design, conduct and analyze 'DCEs' from a virtual interface in shiny.
Reference: Perez-Troncoso, D. (2022)
<https://github.com/danielpereztr/DCEtool>.

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
