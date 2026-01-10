%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vannstats
%global packver   1.6.1.08
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1.08
Release:          1%{?dist}%{?buildtag}
Summary:          Simplified Statistical Procedures for Social Sciences

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-rstatix 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-reshape2 

%description
Simplifies functions assess normality for bivariate and multivariate
statistical techniques. Includes functions designed to replicate plots and
tables that would result from similar calls in 'SPSS', including hst(),
box(), qq(), tab(), cormat(), and residplot(). Also includes simplified
formulae, such as mode(), scatter(), p.corr(), ow.anova(), and rm.anova().

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
