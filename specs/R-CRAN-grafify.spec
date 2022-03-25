%global __brp_check_rpaths %{nil}
%global packname  grafify
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Graphs for Data Visualisation and Linear Models for ANOVA

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-car 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Easily explore data by generating different kinds of graphs with few lines
of code. Use these ggplot() wrappers to quickly draw graphs of
scatter/dots with box-whiskers, violins or SD error bars, data
distributions, before-after graphs, factorial ANOVA and more. Customise
graphs and choose from 8 colour-blind friendly discreet or 1 continuous
colour scheme. Simple code for ANOVA as ordinary (lm()) or mixed-effects
linear models (lmer()), including randomised-block or repeated-measures
designs. Carry out post-hoc comparisons on fitted models (via emmeans()
wrappers). Also includes small datasets for practicing code and teaching
basics before users move on to more complex designs. See vignettes for
details on usage <https://grafify-vignettes.netlify.app/>. Citation:
<doi:10.5281/zenodo.5136508>.

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
