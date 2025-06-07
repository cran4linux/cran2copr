%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RMCDA
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Criteria Decision Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-matlib 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-matlib 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-pracma 

%description
Supporting decision making involving multiple criteria. Annice Najafi,
Shokoufeh Mirzaei (2025) RMCDA: The Comprehensive R Library for applying
multi-criteria decision analysis methods, Volume 24, e100762
<doi:10.1016/j.simpa.2025.100762>.

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
