%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  capybara
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Memory Efficient Fitting of Linear Models with High-Dimensional Fixed Effects

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-armadillo4r 
BuildRequires:    R-CRAN-cpp4r 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Fast and user-friendly estimation of generalized linear models with
multiple fixed effects and cluster the standard errors. The method to
obtain the estimated fixed-effects coefficients is based on Stammann
(2018) <doi:10.48550/arXiv.1707.01815>, Gaure (2013)
<doi:10.1016/j.csda.2013.03.024>, Berge (2018)
<https://ideas.repec.org/p/luc/wpaper/18-13.html>, and Correia et al.
(2020) <doi: 10.1177/1536867X20909691>. This implementation is described
in Vargas Sepulveda (2025) <doi:10.1371/journal.pone.0331178>.

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
