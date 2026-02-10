%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HaDeX2
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis and Visualisation of Hydrogen/Deuterium Exchange Mass Spectrometry Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-r3dmol >= 0.1.2
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggiraph 
Requires:         R-CRAN-r3dmol >= 0.1.2
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggiraph 

%description
Processing, analysis and visualization of Hydrogen Deuterium eXchange
monitored by Mass Spectrometry experiments (HDX-MS). 'HaDeX2' introduces a
new standardized and reproducible workflow for the analysis of the HDX-MS
data, including uncertainty propagation, data aggregation and
visualization on 3D structure. Additionally, it covers data exploration,
quality control and generation of publication-quality figures. All
functionalities are also available in the accompanying 'shiny' app.

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
