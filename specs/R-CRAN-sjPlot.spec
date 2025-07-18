%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sjPlot
%global packver   2.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Visualization for Statistics in Social Science

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-sjmisc >= 2.8.2
BuildRequires:    R-CRAN-insight >= 1.3.1
BuildRequires:    R-CRAN-sjlabelled >= 1.1.2
BuildRequires:    R-CRAN-datawizard >= 1.1.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-parameters >= 0.27.0
BuildRequires:    R-CRAN-sjstats >= 0.17.8
BuildRequires:    R-CRAN-bayestestR >= 0.16.1
BuildRequires:    R-CRAN-performance >= 0.15.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggeffects 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-sjmisc >= 2.8.2
Requires:         R-CRAN-insight >= 1.3.1
Requires:         R-CRAN-sjlabelled >= 1.1.2
Requires:         R-CRAN-datawizard >= 1.1.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-parameters >= 0.27.0
Requires:         R-CRAN-sjstats >= 0.17.8
Requires:         R-CRAN-bayestestR >= 0.16.1
Requires:         R-CRAN-performance >= 0.15.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggeffects 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 

%description
Collection of plotting and table output functions for data visualization.
Results of various statistical analyses (that are commonly used in social
sciences) can be visualized using this package, including simple and cross
tabulated frequencies, histograms, box plots, (generalized) linear models,
mixed effects models, principal component analysis and correlation
matrices, cluster analyses, scatter plots, stacked scales, effects plots
of regression models (including interaction terms) and much more. This
package supports labelled data.

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
