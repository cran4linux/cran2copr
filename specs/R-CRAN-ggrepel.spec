%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggrepel
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}%{?buildtag}
Summary:          Automatically Position Non-Overlapping Text Labels with 'ggplot2'

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-withr >= 2.5.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-scales >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-withr >= 2.5.0
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-scales >= 0.5.0
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-grid 
Requires:         R-CRAN-Rcpp 

%description
Provides text and label geoms for 'ggplot2' that help to avoid overlapping
text labels. Labels repel away from each other and away from the data
points.

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
