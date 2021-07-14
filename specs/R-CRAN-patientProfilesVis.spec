%global __brp_check_rpaths %{nil}
%global packname  patientProfilesVis
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization of Patient Profiles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-clinUtils 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-clinUtils 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-cowplot 
Requires:         R-tools 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-knitr 
Requires:         R-grid 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-parallel 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-scales 

%description
Creation of patient profile visualizations for exploration, diagnostic or
monitoring purposes during a clinical trial. These static visualizations
display a patient-specific overview of the evolution during the trial time
frame of parameters of interest (as laboratory, ECG, vital signs),
presence of adverse events, exposure to a treatment; associated with
metadata patient information, as demography, concomitant medication. The
visualizations can be tailored for specific domain(s) or endpoint(s) of
interest. Visualizations are exported into patient profile report(s) or
can be embedded in custom report(s).

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
