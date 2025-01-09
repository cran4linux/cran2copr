%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  npiv
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Instrumental Variables Estimation and Inference

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-withr 

%description
Implements methods introduced in Chen, Christensen, and Kankanala (2024)
<doi:10.1093/restud/rdae025> for estimating and constructing uniform
confidence bands for nonparametric structural functions using instrumental
variables, including data-driven choice of tuning parameters. All methods
in this package apply to nonparametric regression as a special case.

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
