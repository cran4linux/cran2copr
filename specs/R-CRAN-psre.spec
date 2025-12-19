%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psre
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Presenting Statistical Results Effectively

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-marginaleffects 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-fANCOVA 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-VizTest 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-car 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-marginaleffects 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-boot 
Requires:         R-grid 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-fANCOVA 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-VizTest 

%description
Includes functions and data used in the book "Presenting Statistical
Results Effectively", Andersen and Armstrong (2022, ISBN: 978-1446269800).
Several functions aid in data visualization - creating compact letter
displays for simple slopes, kernel density estimates with normal density
overlay.  Other functions aid in post-model evaluation heatmap fit
statistics for binary predictors, several variable importance measures,
compact letter displays and simple-slope calculation. Finally, the package
makes available the example datasets used in the book.

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
