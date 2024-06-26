%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggwordcloud
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Word Cloud Geom for 'ggplot2'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridtext 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-grid 
Requires:         R-CRAN-gridtext 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-png 

%description
Provides a word cloud text geom for 'ggplot2'. Texts are placed so that
they do not overlap as in 'ggrepel'.  The algorithm used is a variation
around the one of 'wordcloud2.js'.

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
