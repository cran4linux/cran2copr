%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ThinkingGrid
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Thinking Grid Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.45
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gifski 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-reticulate >= 1.45
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gifski 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides comprehensive tools for conducting research using the Thinking
Grid framework, a psychological measurement approach for understanding the
stream of thought. Includes functions for generating Qualtrics surveys
with the thinking grid, processing survey responses, calculating quadrant
depths, and creating various visualization types including heatmaps,
animations, and statistical plots. See Irving, Z. C., Murray, S., Kuvar,
V., Urena, M., and Mills, C. (2025) "Consciousness, Just in Time:
Fluctuations in the Stream of Consciousness during Tasks and Rest"
(manuscript under review, draft available from zci7c@virginia.edu).

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
