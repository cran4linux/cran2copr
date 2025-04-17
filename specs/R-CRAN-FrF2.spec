%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FrF2
%global packver   2.3-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Fractional Factorial Designs with 2-Level Factors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sfsmisc >= 1.0.26
BuildRequires:    R-CRAN-igraph >= 0.7
BuildRequires:    R-CRAN-DoE.base >= 0.25
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-methods 
Requires:         R-CRAN-sfsmisc >= 1.0.26
Requires:         R-CRAN-igraph >= 0.7
Requires:         R-CRAN-DoE.base >= 0.25
Requires:         R-utils 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-methods 

%description
Regular and non-regular Fractional Factorial 2-level designs can be
created. Furthermore, analysis tools for Fractional Factorial designs with
2-level factors are offered (main effects and interaction plots for all
factors simultaneously, cube plot for looking at the simultaneous effects
of three factors, full or half normal plot, alias structure in a more
readable format than with the built-in function alias).

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
