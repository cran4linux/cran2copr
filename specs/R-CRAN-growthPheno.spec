%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  growthPheno
%global packver   2.1.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.17
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Analysis of Phenotypic Growth Data to Smooth and Extract Traits

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dae 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-JOPS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
Requires:         R-CRAN-dae 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-JOPS 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-reshape 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-utils 

%description
Assists in the plotting and functional smoothing of traits measured over
time and the extraction of features from these traits, implementing the
SET (Smoothing and Extraction of Traits) method described in Brien et al.
(2020) Plant Methods, 16. Smoothing of growth trends for individual plants
using natural cubic smoothing splines or P-splines is available for
removing transient effects and segmented smoothing is available to deal
with discontinuities in growth trends. There are graphical tools for
assessing the adequacy of trait smoothing, both when using this and other
packages, such as those that fit nonlinear growth models. A range of
per-unit (plant, pot, plot) growth traits or features can be extracted
from the data, including single time points, interval growth rates and
other growth statistics, such as maximum growth or days to maximum growth.
The package also has tools adapted to inputting data from high-throughput
phenotyping facilities, such from a Lemna-Tec Scananalyzer 3D (see
<https://www.youtube.com/watch?v=MRAF_mAEa7E/> for more information). The
package 'growthPheno' can also be installed from
<http://chris.brien.name/rpackages/>.

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
