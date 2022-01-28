%global __brp_check_rpaths %{nil}
%global packname  ompr.roi
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Solver for 'ompr' that Uses the R Optimization Infrastructure ('ROI')

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ompr >= 1.0.0
BuildRequires:    R-CRAN-ROI >= 0.3.0
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-ompr >= 1.0.0
Requires:         R-CRAN-ROI >= 0.3.0
Requires:         R-CRAN-slam 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 

%description
A solver for 'ompr' based on the R Optimization Infrastructure ('ROI').
The package makes all solvers in 'ROI' available to solve 'ompr' models.
Please see the 'ompr' website <https://dirkschumacher.github.io/ompr/> and
package docs for more information and examples on how to use it.

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
