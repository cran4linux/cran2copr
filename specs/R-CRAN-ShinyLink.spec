%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ShinyLink
%global packver   0.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          'Shiny' Based Record Linkage Tool

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shinydashboardPlus >= 2.0.3
BuildRequires:    R-CRAN-shiny >= 1.7.2
BuildRequires:    R-CRAN-golem >= 0.3.5
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-DT >= 0.25
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fastLink 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-shinydashboardPlus >= 2.0.3
Requires:         R-CRAN-shiny >= 1.7.2
Requires:         R-CRAN-golem >= 0.3.5
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-DT >= 0.25
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fastLink 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tibble 

%description
A bridge is created between existing robust open-source record linkage
algorithms and an urgently needed user-friendly platform that removes
financial and technical barriers, setting a new standard for data
interoperability in public health and bioinformatics. The 'fastLink'
algorithms are used for matching. Ted Enamorado et al. (2019)
<doi:10.1017/S0003055418000783>.

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
