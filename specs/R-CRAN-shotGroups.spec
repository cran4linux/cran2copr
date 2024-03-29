%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shotGroups
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Shot Group Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CompQuadForm >= 1.4.2
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-CompQuadForm >= 1.4.2
Requires:         R-CRAN-boot 
Requires:         R-CRAN-coin 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Analyzes shooting data with respect to group shape, precision, and
accuracy. This includes graphical methods, descriptive statistics, and
inference tests using standard, but also non-parametric and robust
statistical methods. Implements distributions for radial error in
bivariate normal variables. Works with files exported by 'OnTarget
PC/TDS', 'Silver Mountain' e-target, 'ShotMarker' e-target, or 'Taran', as
well as with custom data files in text format. Supports inference from
range statistics such as extreme spread. Includes a set of web-based
graphical user interfaces.

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
