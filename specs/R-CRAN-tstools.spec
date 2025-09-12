%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tstools
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          A Time Series Toolbox for Official Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.7.12
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-zoo >= 1.7.12
Requires:         R-CRAN-data.table 
Requires:         R-graphics 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-yaml 

%description
Plot official statistics' time series conveniently: automatic legends,
highlight windows, stacked bar chars with positive and negative
contributions, sum-as-line option, two y-axes with automatic horizontal
grids that fit both axes and other popular chart types. 'tstools' comes
with a plethora of defaults to let you plot without setting an abundance
of parameters first, but gives you the flexibility to tweak the defaults.
In addition to charts, 'tstools' provides a super fast, 'data.table'
backed time series I/O that allows the user to export / import long
format, wide format and transposed wide format data to various file types.

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
