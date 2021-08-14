%global __brp_check_rpaths %{nil}
%global packname  powdR
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Full Pattern Summation of X-Ray Powder Diffraction Data

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.2.1
BuildRequires:    R-stats >= 3.4.3
BuildRequires:    R-utils >= 3.4.3
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-FactoMineR >= 2.3
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-CRAN-shiny >= 1.4.0.2
BuildRequires:    R-CRAN-nnls >= 1.4
BuildRequires:    R-CRAN-baseline >= 1.2
BuildRequires:    R-CRAN-factoextra >= 1.0.7
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-reshape >= 0.8.8
BuildRequires:    R-CRAN-shinyWidgets >= 0.5.1
BuildRequires:    R-CRAN-rxylib >= 0.2.6
BuildRequires:    R-CRAN-ggpubr >= 0.2.5
BuildRequires:    R-CRAN-DT >= 0.13
Requires:         R-CRAN-plotly >= 4.9.2.1
Requires:         R-stats >= 3.4.3
Requires:         R-utils >= 3.4.3
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-FactoMineR >= 2.3
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-CRAN-shiny >= 1.4.0.2
Requires:         R-CRAN-nnls >= 1.4
Requires:         R-CRAN-baseline >= 1.2
Requires:         R-CRAN-factoextra >= 1.0.7
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-reshape >= 0.8.8
Requires:         R-CRAN-shinyWidgets >= 0.5.1
Requires:         R-CRAN-rxylib >= 0.2.6
Requires:         R-CRAN-ggpubr >= 0.2.5
Requires:         R-CRAN-DT >= 0.13

%description
Full pattern summation of X-ray powder diffraction data as described in
Chipera and Bish (2002) <doi:10.1107/S0021889802017405> and Butler and
Hillier (2021) <doi:10.1016/j.cageo.2020.104662>. Derives quantitative
estimates of crystalline and amorphous phase concentrations in complex
mixtures.

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
