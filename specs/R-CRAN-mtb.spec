%global __brp_check_rpaths %{nil}
%global packname  mtb
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Toolkit for Assisting Kitchen and Garden Projects

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-htmltools >= 0.4.0
BuildRequires:    R-CRAN-labeling >= 0.3
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-htmltools >= 0.4.0
Requires:         R-CRAN-labeling >= 0.3

%description
The purpose of this package is to share a collection of functions the
author wrote during weekends for managing kitchen and garden tasks, e.g.
making plant growth charts or Thanksgiving kitchen schedule charts, etc.
Functions might include but not limited to: (1) aiding summarizing time
related data; (2) generating axis transformation from data; and (3) aiding
Markdown (with html output) and Shiny file editing.

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
