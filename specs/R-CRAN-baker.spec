%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baker
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          "Nested Partially Latent Class Models"

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.6
BuildRequires:    R-CRAN-mvbutils >= 2.7.4.1
BuildRequires:    R-CRAN-robCompositions >= 2.0.3
BuildRequires:    R-CRAN-gridExtra >= 2.0
BuildRequires:    R-CRAN-mgcv >= 1.8.6
BuildRequires:    R-CRAN-reshape2 >= 1.4
BuildRequires:    R-CRAN-lubridate >= 1.3
BuildRequires:    R-CRAN-binom >= 1.1
BuildRequires:    R-CRAN-ggplot2 >= 1.0
BuildRequires:    R-CRAN-shinyFiles >= 0.6
BuildRequires:    R-CRAN-shinydashboard >= 0.5.1
BuildRequires:    R-CRAN-R2jags >= 0.5
BuildRequires:    R-CRAN-ggpubr >= 0.4.0
BuildRequires:    R-CRAN-coda >= 0.16
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-rjags >= 4.6
Requires:         R-CRAN-mvbutils >= 2.7.4.1
Requires:         R-CRAN-robCompositions >= 2.0.3
Requires:         R-CRAN-gridExtra >= 2.0
Requires:         R-CRAN-mgcv >= 1.8.6
Requires:         R-CRAN-reshape2 >= 1.4
Requires:         R-CRAN-lubridate >= 1.3
Requires:         R-CRAN-binom >= 1.1
Requires:         R-CRAN-ggplot2 >= 1.0
Requires:         R-CRAN-shinyFiles >= 0.6
Requires:         R-CRAN-shinydashboard >= 0.5.1
Requires:         R-CRAN-R2jags >= 0.5
Requires:         R-CRAN-ggpubr >= 0.4.0
Requires:         R-CRAN-coda >= 0.16
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-abind 

%description
Provides functions to specify, fit and visualize nested partially-latent
class models ( Wu, Deloria-Knoll, Hammitt, and Zeger (2016)
<doi:10.1111/rssc.12101>; Wu, Deloria-Knoll, and Zeger (2017)
<doi:10.1093/biostatistics/kxw037>; Wu and Chen (2021)
<doi:10.1002/sim.8804>) for inference of population disease etiology and
individual diagnosis. In the motivating Pneumonia Etiology Research for
Child Health (PERCH) study, because both quantities of interest sum to one
hundred percent, the PERCH scientists frequently refer to them as
population etiology pie and individual etiology pie, hence the name of the
package.

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
