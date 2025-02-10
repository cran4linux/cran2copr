%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  details
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Details HTML Tag for Markdown and Package Documentation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-desc 
Requires:         R-grid 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-png 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-httr 

%description
Create a details HTML tag around R objects to place in a Markdown,
'Rmarkdown' and 'roxygen2' documentation.

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
