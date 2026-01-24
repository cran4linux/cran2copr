%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xdvir
%global packver   0.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Render 'LaTeX' in Plots

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-systemfonts >= 1.1.0
BuildRequires:    R-CRAN-hexView >= 0.3.4
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-tinytex 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-systemfonts >= 1.1.0
Requires:         R-CRAN-hexView >= 0.3.4
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-tinytex 
Requires:         R-CRAN-rlang 

%description
High-level functions to render 'LaTeX' fragments in plots, including as
labels and data symbols in 'ggplot2' plots, plus low-level functions to
author 'LaTeX' fragments (to produce 'LaTeX' documents), typeset 'LaTeX'
documents (to produce 'DVI' files), read 'DVI' files (to produce "DVI"
objects), and render "DVI" objects.

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
