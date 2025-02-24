%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plotscaper
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Explore Your Data with Interactive Figures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.8
BuildRequires:    R-CRAN-htmlwidgets >= 1.6
BuildRequires:    R-CRAN-httpuv >= 1.6
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-jsonlite >= 1.8
Requires:         R-CRAN-htmlwidgets >= 1.6
Requires:         R-CRAN-httpuv >= 1.6
Requires:         R-CRAN-knitr 
Requires:         R-stats 
Requires:         R-CRAN-uuid 

%description
A framework for creating interactive figures for data exploration. All
plots are automatically linked and support several kinds of interactive
features, including selection, zooming, panning, and parameter
manipulation. The figures can be interacted with either manually, using a
mouse and a keyboard, or by running code from inside an active R session.

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
