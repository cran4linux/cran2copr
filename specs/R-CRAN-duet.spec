%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  duet
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysing Non-Verbal Communication in Dyadic Interactions from Video Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-kza 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggthemes 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-kza 
Requires:         R-parallel 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-signal 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Analyzes non-verbal communication by processing data extracted from video
recordings of dyadic interactions. It supports integration with open
source tools, currently limited to 'OpenPose' (Cao et al. (2019)
<doi:10.1109/TPAMI.2019.2929257>), converting its outputs into CSV format
for further analysis. The package includes functions for data
pre-processing, visualization, and computation of motion indices such as
velocity, acceleration, and jerkiness (Cook et al. (2013)
<doi:10.1093/brain/awt208>), facilitating the analysis of non-verbal cues
in paired interactions and contributing to research on human communication
dynamics.

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
