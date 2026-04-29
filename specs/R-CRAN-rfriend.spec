%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rfriend
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Provides Batch Functions and Visualisation for Basic Statistical Procedures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bestNormalize 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-DHARMa 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-this.path 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-xfun 
Requires:         R-CRAN-bestNormalize 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-DHARMa 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-png 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rstatix 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-this.path 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-xfun 

%description
Designed to streamline data analysis and statistical testing, reducing the
length of R scripts while generating well-formatted outputs in 'pdf',
'Microsoft Word', and 'Microsoft Excel' formats. In essence, the package
contains functions which are sophisticated wrappers around existing R
functions that are called by using 'f_' (user f_riendly) prefix followed
by the normal function name. This third version of the 'rfriend' package
focuses primarily on data exploration, including tools for creating
summary tables, f_summary(), summary figures, f_scan(), outlier detection
and removal, f_outlier() and f_remove_outliers(), performing data
transformations, f_boxcox() in part based on 'MASS/boxcox' and
'rcompanion', and f_bestNormalize() which wraps and extends functionality
from the 'bestNormalize' package. Furthermore, 'rfriend' can automatically
(or on request) generate visualizations such as boxplots, f_boxplot(),
QQ-plots, f_qqnorm(), histograms f_hist(), and density plots f_density().
Additionally, the package includes several statistical test functions:
f_aov(), f_chisq_test(), f_corplot(), f_kruskal_test(), f_lmer(), f_glm(),
f_t_test(), f_wilcox_test(), for sequential testing and visualisation of
the similar named 'stats' functions. These functions, except for
f_chisq_test(), support testing multiple response variables and
predictors, while also handling assumption checks, data transformations,
and post hoc tests. Post hoc results are automatically summarized in a
table using the compact letter display (cld) format for easy
interpretation. The package also provides a function to do model
comparison, f_model_comparison(), and several utility functions to
simplify common R tasks. For example, f_clear() clears the workspace and
restarts R with a single command; f_setwd() sets the working directory to
match the directory of the current script; f_theme() quickly changes
'RStudio' themes; and f_factors() converts multiple columns of a data
frame to factors, and much more. If you encounter any issues or have
feature requests, please feel free to contact me via email.

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
