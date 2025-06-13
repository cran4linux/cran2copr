%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyspec
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spectroscopy Analysis Using the Tidy Data Philosophy

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-timetk 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-timetk 

%description
Enables the analysis of spectroscopy data such as infrared ('IR'), Raman,
and nuclear magnetic resonance ('NMR') using the tidy data framework from
the 'tidyverse'. The 'tidyspec' package provides functions for data
transformation, normalization, baseline correction, smoothing,
derivatives, and both interactive and static visualization. It promotes
structured, reproducible workflows for spectral data exploration and
preprocessing. Implemented methods include Savitzky and Golay (1964)
"Smoothing and Differentiation of Data by Simplified Least Squares
Procedures" <doi:10.1021/ac60214a047>, Sternberg (1983) "Biomedical Image
Processing"
<https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1654163>,
Zimmermann and Kohler (1996) "Baseline correction using the rolling ball
algorithm" <doi:10.1016/0168-583X(95)00908-6>, Beattie and Esmonde-White
(2021) "Exploration of Principal Component Analysis: Deriving Principal
Component Analysis Visually Using Spectra" <doi:10.1177/0003702820987847>,
Wickham et al. (2019) "Welcome to the tidyverse"
<doi:10.21105/joss.01686>, and Kuhn, Wickham and Hvitfeldt (2024)
"recipes: Preprocessing and Feature Engineering Steps for Modeling"
<https://CRAN.R-project.org/package=recipes>.

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
