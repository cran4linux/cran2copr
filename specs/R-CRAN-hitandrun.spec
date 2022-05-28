%global __brp_check_rpaths %{nil}
%global packname  hitandrun
%global packver   0.5-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.6
Release:          1%{?dist}%{?buildtag}
Summary:          "Hit and Run" and "Shake and Bake" for Sampling Uniformly from Convex Shapes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rcdd >= 1.1
BuildRequires:    R-stats 
Requires:         R-CRAN-rcdd >= 1.1
Requires:         R-stats 

%description
The "Hit and Run" Markov Chain Monte Carlo method for sampling uniformly
from convex shapes defined by linear constraints, and the "Shake and Bake"
method for sampling from the boundary of such shapes. Includes specialized
functions for sampling normalized weights with arbitrary linear
constraints. Tervonen, T., van Valkenhoef, G., Basturk, N., and Postmus,
D. (2012) <doi:10.1016/j.ejor.2012.08.026>. van Valkenhoef, G., Tervonen,
T., and Postmus, D. (2014) <doi:10.1016/j.ejor.2014.06.036>.

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
