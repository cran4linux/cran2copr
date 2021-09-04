%global __brp_check_rpaths %{nil}
%global packname  ggpmisc
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Extensions to 'ggplot2'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51.6
BuildRequires:    R-CRAN-quantreg >= 5.85
BuildRequires:    R-CRAN-ggplot2 >= 3.3.1
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-lmodel2 >= 1.7.3
BuildRequires:    R-CRAN-polynom >= 1.4.0
BuildRequires:    R-CRAN-splus2R >= 1.2.2
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-ggpp >= 0.4.2
BuildRequires:    R-CRAN-generics >= 0.1.0
BuildRequires:    R-grid 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS >= 7.3.51.6
Requires:         R-CRAN-quantreg >= 5.85
Requires:         R-CRAN-ggplot2 >= 3.3.1
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-lmodel2 >= 1.7.3
Requires:         R-CRAN-polynom >= 1.4.0
Requires:         R-CRAN-splus2R >= 1.2.2
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-ggpp >= 0.4.2
Requires:         R-CRAN-generics >= 0.1.0
Requires:         R-grid 
Requires:         R-stats 

%description
Extensions to 'ggplot2' respecting the grammar of graphics paradigm.
Statistics: locate and tag peaks and valleys; label plot with the equation
of a fitted polynomial or other types of models; labels with P-value, R^2
or adjusted R^2 or information criteria for fitted models; label with
ANOVA table for fitted models; label with summary for fitted models. Model
fit classes for which suitable methods are provided by package 'broom' and
'broom.mixed' are supported. Scales and stats to build volcano and
quadrant plots based on outcomes, fold changes, p-values and false
discovery rates.

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
