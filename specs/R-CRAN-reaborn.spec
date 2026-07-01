%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reaborn
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Data Visualization, the 'seaborn' Way

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-stats 

%description
An 'R' port of the 'Python' 'seaborn' library. 'reaborn' mirrors the
'seaborn' public function API (identical function names, argument names,
and defaults) and renders visually indistinguishable plots using
'ggplot2'. Because every 'reaborn' plot is a 'ggplot' object, it can be
extended with the full 'ggplot2' grammar of graphics.

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
