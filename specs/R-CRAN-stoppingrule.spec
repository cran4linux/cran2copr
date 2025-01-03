%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stoppingrule
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Create and Evaluate Stopping Rules for Safety Monitoring

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-matrixStats 

%description
Provides functions for creating, displaying, and evaluating stopping rules
for safety monitoring in clinical studies. Implements stopping rule
methods described in Goldman (1987) <doi:10.1016/0197-2456(87)90153-X>;
Geller et al. (2003, ISBN:9781135524388); Ivanova, Qaqish, and Schell
(2005) <doi:10.1111/j.1541-0420.2005.00311.x>; Chen and Chaloner (2006)
<doi:10.1002/sim.2429>; and Kulldorff et al. (2011)
<doi:10.1080/07474946.2011.539924>.

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
