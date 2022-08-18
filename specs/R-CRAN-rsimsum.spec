%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rsimsum
%global packver   0.11.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Simulation Studies Including Monte Carlo Error

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-scales 
Requires:         R-stats 

%description
Summarise results from simulation studies and compute Monte Carlo standard
errors of commonly used summary statistics. This package is modelled on
the 'simsum' user-written command in 'Stata' (White I.R., 2010
<https://www.stata-journal.com/article.html?article=st0200>), further
extending it with additional performance measures and functionality.

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
