%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ivreg2r
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extended Instrumental Variables Estimation with Diagnostics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-generics 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
Comprehensive instrumental variables and GMM estimation with automatic
diagnostics, inspired by the 'Stata' command 'ivreg2' of Baum, Schaffer,
and Stillman (2003) <doi:10.1177/1536867X0300300101> and Baum, Schaffer,
and Stillman (2007) <doi:10.1177/1536867X0800700402>. Supports 2SLS, LIML,
Fuller, k-class, two-step efficient GMM, and continuously-updated (CUE)
estimators. Provides classical, robust, cluster-robust, HAC, and
Driscoll-Kraay standard errors. Reports weak identification,
underidentification, overidentification, and endogeneity tests at
estimation time. All outputs are verified against 'Stata' within tight
numerical tolerances.

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
