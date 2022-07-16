%global __brp_check_rpaths %{nil}
%global packname  mada
%global packver   0.5.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.11
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Analysis of Diagnostic Accuracy

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-mvmeta 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-mvmeta 
Requires:         R-CRAN-metafor 
Requires:         R-methods 

%description
Provides functions for diagnostic meta-analysis. Next to basic analysis
and visualization the bivariate Model of Reitsma et al. (2005) that is
equivalent to the HSROC of Rutter & Gatsonis (2001) can be fitted. A new
approach based to diagnostic meta-analysis of Holling et al. (2012) is
also available. Standard methods like summary, plot and so on are
provided.

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
