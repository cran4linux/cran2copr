%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinyCLT
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          1%{?dist}%{?buildtag}
Summary:          Central Limit Theorem 'shiny' Application

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-waiter 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-future 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-waiter 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-cachem 
Requires:         R-CRAN-knitr 

%description
A 'shiny' application estimating the operating characteristics of the
Student's t-test by Student (1908) <doi:10.1093/biomet/6.1.1>, Welch's
t-test by Welch (1947) <doi:10.1093/biomet/34.1-2.28>, and Wilcoxon test
by Wilcoxon (1945) <doi:10.2307/3001968> in one-sample or two-sample
cases, in settings defined by the user (conditional distribution, sample
size per group, location parameter per group, nuisance parameter per
group), using Monte Carlo simulations Malvin H. Kalos, Paula A. Whitlock
(2008) <doi:10.1002/9783527626212>.

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
