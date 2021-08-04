%global __brp_check_rpaths %{nil}
%global packname  rbokeh
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface for Bokeh

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 0.5
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gistr 
Requires:         R-CRAN-htmlwidgets >= 0.5
Requires:         R-CRAN-maps 
Requires:         R-methods 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gistr 

%description
A native R plotting library that provides a flexible declarative interface
for creating interactive web-based graphics, backed by the Bokeh
visualization library <https://bokeh.pydata.org/>.

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
