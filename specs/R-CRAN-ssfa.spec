%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ssfa
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Stochastic Frontier Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-spdep >= 1.1.1
BuildRequires:    R-CRAN-spatialreg >= 1.1.1
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-spdep >= 1.1.1
Requires:         R-CRAN-spatialreg >= 1.1.1
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-sp 

%description
Spatial Stochastic Frontier Analysis (SSFA) is an original method for
controlling the spatial heterogeneity in Stochastic Frontier Analysis
(SFA) models, for cross-sectional data, by splitting the inefficiency term
into three terms: the first one related to spatial peculiarities of the
territory in which each single unit operates, the second one related to
the specific production features and the third one representing the error
term.

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
