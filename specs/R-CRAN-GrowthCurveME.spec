%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GrowthCurveME
%global packver   0.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed-Effects Modeling for Growth Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-saemix >= 3.3
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-knitr >= 1.46
BuildRequires:    R-CRAN-investr >= 1.4.2
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-minpack.lm >= 1.2.4
BuildRequires:    R-CRAN-patchwork >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.3
BuildRequires:    R-CRAN-flextable >= 0.9.6
BuildRequires:    R-CRAN-viridis >= 0.6.5
BuildRequires:    R-CRAN-moments >= 0.14.1
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-saemix >= 3.3
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-knitr >= 1.46
Requires:         R-CRAN-investr >= 1.4.2
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-minpack.lm >= 1.2.4
Requires:         R-CRAN-patchwork >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.3
Requires:         R-CRAN-flextable >= 0.9.6
Requires:         R-CRAN-viridis >= 0.6.5
Requires:         R-CRAN-moments >= 0.14.1

%description
Simple and user-friendly wrappers to the 'saemix' package for performing
linear and non-linear mixed-effects regression modeling for growth data to
account for clustering or longitudinal analysis via repeated measurements.
The package allows users to fit a variety of growth models, including
linear, exponential, logistic, and 'Gompertz' functions. For non-linear
models, starting values are automatically calculated using initial
least-squares estimates. The package includes functions for summarizing
models, visualizing data and results, calculating doubling time and other
key statistics, and generating model diagnostic plots and residual summary
statistics. It also provides functions for generating publication-ready
summary tables for reports. Additionally, users can fit linear and
non-linear least-squares regression models if clustering is not
applicable. The mixed-effects modeling methods in this package are based
on Comets, Lavenu, and Lavielle (2017) <doi:10.18637/jss.v080.i03> as
implemented in the 'saemix' package. Please contact us at
models@dfci.harvard.edu with any questions.

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
