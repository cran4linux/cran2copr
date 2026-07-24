%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  orchaRd
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing Meta-Analyses with Orchard Plots and Prediction Intervals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-ggbeeswarm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rWishart 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tester 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-ggbeeswarm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rWishart 
Requires:         R-stats 
Requires:         R-CRAN-tester 
Requires:         R-utils 

%description
Generates prediction intervals and orchard plots for meta-analytic and
meta-regression models fitted with the 'metafor' package. Orchard plots
augment classic forest plots by displaying individual effect sizes
together with group means and their confidence and prediction intervals,
providing an enhanced visualization of meta-analytic data for ecology,
evolution, and beyond. Methods are described in Nakagawa et al. (2023)
<doi:10.1111/2041-210X.14152>.

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
