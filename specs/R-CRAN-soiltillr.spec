%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  soiltillr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyse Soil Tillage Depth and Erosion Over Time

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-dplyr >= 1.1.0

%description
Provides tools to record, validate, and analyse soil tillage depth and
erosion across years and field treatments. Includes functions for
year-wise tillage operation summaries, erosion depth tracking, compaction
detection, soil loss estimation, and visualisation of temporal changes in
tillage and erosion profiles. Methods follow Lal (2001)
<doi:10.1201/9780203739280> and Renard et al. (1997) "Predicting Soil
Erosion by Water: A Guide to Conservation Planning with the Revised
Universal Soil Loss Equation (RUSLE)"
<https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/PB97153704.xhtml>.

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
