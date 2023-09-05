%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  altair
%global packver   4.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'Altair'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.23
BuildRequires:    R-CRAN-vegawidget >= 0.4.1
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-repr 
Requires:         R-CRAN-reticulate >= 1.23
Requires:         R-CRAN-vegawidget >= 0.4.1
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-CRAN-repr 

%description
Interface to 'Altair' <https://altair-viz.github.io>, which itself is a
'Python' interface to 'Vega-Lite' <https://vega.github.io/vega-lite/>.
This package uses the 'Reticulate' framework
<https://rstudio.github.io/reticulate/> to manage the interface between R
and 'Python'.

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
