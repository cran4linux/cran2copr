%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  groupedHyperframe.random
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulated Grouped Hyper Data Frame

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-groupedHyperframe 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-groupedHyperframe 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-MASS 

%description
An intuitive interface to simulate (1) superimposed (marked) point
patterns with vectorized parameterization of random point pattern and
distribution of marks; and (2) grouped hyper data frame based on
population parameters and subject-specific random effects.

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
