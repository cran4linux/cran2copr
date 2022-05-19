%global __brp_check_rpaths %{nil}
%global packname  grwat
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          River Hydrograph Separation and Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-trend 
BuildRequires:    R-CRAN-mblm 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-trend 
Requires:         R-CRAN-mblm 

%description
River hydrograph separation and daily runoff time series analysis.
Provides various filters to separate baseflow and quickflow using methods
by Lyne and Hollick (1979)
<https://www.researchgate.net/publication/272491803_Stochastic_Time-Variable_Rainfall-Runoff_Modeling>,
Chapman (1991) <doi:10.1029/91WR01007>, Boughton (1993)
<https://cir.nii.ac.jp/crid/1572543026556977024>, Jakeman and Hornberger
(1993) <doi:10.1029/93WR00877>, Chapman and Maxwell (1996)
<https://search.informit.org/doi/10.3316/informit.360361071346753>, and
Kudelin (1960)
<https://www.worldcat.org/title/printsipy-regionalnoi-otsenki-estestvennykh-resursov-podzemnykh-vod/>.
Implements advanced separation technique by Rets et al. (2022)
<doi:10.1134/S0097807822010146> which involves meteorological data to
reveal genetic components of the runoff: ground, rain, thaw and spring
(seasonal thaw). High-performance C++17 computation, annually aggregated
variables, statistical testing and numerous plotting functions for
high-quality visualization.

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
