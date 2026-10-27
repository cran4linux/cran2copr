%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Analitica
%global packver   2.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Data Analysis, Group Comparison Tools, and Other Procedures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.6
Requires:         R-core >= 4.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-multcompView 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a comprehensive set of tools for descriptive statistics,
graphical data exploration, outlier detection, homoscedasticity testing,
and multiple comparison procedures. Includes manual implementations of
Levene's test, Bartlett's test, and the Fligner-Killeen test; parametric
post hoc methods such as Tukey, Scheffe, Duncan, SNK, LSD, Games-Howell
and Tamhane; and rank-based post hoc methods such as Dunn, Conover-Iman,
Nemenyi, Dwass-Steel-Critchlow-Fligner and Bonferroni-corrected
Mann-Whitney tests, with plots suited to each type of procedure. Also
includes the Jonckheere-Terpstra trend test, the Jarque-Bera test with
Glinskiy's (2024) correction, and a post hoc test planner that helps
choose the most suitable procedure. Designed for use in teaching, applied
statistical analysis, and reproducible research.

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
