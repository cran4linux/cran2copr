%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ImVol
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Volume Prediction of Trees Using Linear and Nonlinear Allometric Equations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-nls2 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-nls2 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 

%description
Volume prediction is one of challenging task in forestry research. This
package is a comprehensive toolset designed for the fitting and validation
of various linear and nonlinear allometric equations (Linear, Log-Linear,
Inverse, Quadratic, Cubic, Compound, Power and Exponential) used in the
prediction of conifer tree volume. This package is particularly useful for
forestry professionals, researchers, and resource managers engaged in
assessing and estimating the volume of coniferous trees. This package has
been developed using the algorithm of Sharma et al. (2017)
<doi:10.13140/RG.2.2.33786.62407>.

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
