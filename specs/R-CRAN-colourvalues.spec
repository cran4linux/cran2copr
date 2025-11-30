%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  colourvalues
%global packver   0.3.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.11
Release:          1%{?dist}%{?buildtag}
Summary:          Assigns Colours to Values

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-BH >= 1.81.0
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-graphics 

%description
Maps one of the viridis colour palettes, or a user-specified palette to
values. Viridis colour maps are created by Stéfan van der Walt and
Nathaniel Smith, and were set as the default palette for the 'Python'
'Matplotlib' library <https://matplotlib.org/>. Other palettes available
in this library have been derived from 'RColorBrewer'
<https://CRAN.R-project.org/package=RColorBrewer> and 'colorspace'
<https://CRAN.R-project.org/package=colorspace> packages.

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
