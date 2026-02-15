%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  semTools
%global packver   0.5-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.8
Release:          1%{?dist}%{?buildtag}
Summary:          Useful Tools for Structural Equation Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.6.21
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-lavaan >= 0.6.21
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-pbivnorm 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides miscellaneous tools for structural equation modeling, many of
which extend the 'lavaan' package. For example, latent interactions can be
estimated using product indicators (Lin et al., 2010,
<doi:10.1080/10705511.2010.488999>) and simple effects probed; analytical
power analyses can be conducted (Jak et al., 2021,
<doi:10.3758/s13428-020-01479-0>); and scale reliability can be estimated
based on estimated factor-model parameters.

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
