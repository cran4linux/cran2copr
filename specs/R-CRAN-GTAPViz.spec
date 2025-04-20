%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GTAPViz
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Automating 'GTAP' Data Processing and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-HARplus 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-openxlsx2 
Requires:         R-CRAN-HARplus 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-colorspace 
Requires:         R-grDevices 
Requires:         R-CRAN-scales 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-stringdist 
Requires:         R-stats 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-openxlsx2 

%description
Tools to streamline the extraction, processing, and visualization of
Computable General Equilibrium (CGE) results from 'GTAP' models. Designed
for compatibility with both .har and .sl4 files, the package enables users
to automate data preparation, apply mapping metadata, and generate
high-quality plots and summary tables with minimal coding. 'GTAPViz'
supports flexible export options (e.g., Text, CSV, 'Stata', or 'Excel'
formats). This facilitates efficient post-simulation analysis for economic
research and policy reporting. Includes helper functions to filter,
format, and customize outputs with reproducible styling.

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
