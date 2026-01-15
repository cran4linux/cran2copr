%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ddpcr
%global packver   1.16.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.16.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis and Visualization of Droplet Digital PCR in R and on the Web

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-plyr >= 1.8.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-mixtools >= 1.0.2
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-shinyjs >= 0.4.0
BuildRequires:    R-CRAN-DT >= 0.2
BuildRequires:    R-CRAN-shiny >= 0.11.0
BuildRequires:    R-CRAN-readr >= 0.1.0
BuildRequires:    R-CRAN-shinydisconnect 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-plyr >= 1.8.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-mixtools >= 1.0.2
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-shinyjs >= 0.4.0
Requires:         R-CRAN-DT >= 0.2
Requires:         R-CRAN-shiny >= 0.11.0
Requires:         R-CRAN-readr >= 0.1.0
Requires:         R-CRAN-shinydisconnect 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 

%description
An interface to explore, analyze, and visualize droplet digital PCR
(ddPCR) data in R. This is the first non-proprietary software for
analyzing two-channel ddPCR data. An interactive tool was also created and
is available online to facilitate this analysis for anyone who is not
comfortable with using R.

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
