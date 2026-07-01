%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BioTooltipR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Add Bio Tooltips to HTML Reports

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-utils 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-utils 

%description
Provides lightweight helpers for adding gene and chemical tooltips to R
Markdown, Quarto, Shiny, pkgdown, and other HTML outputs. The package
emits small HTML spans with module-specific data attributes and attaches
the browser-side 'bio-tooltips' JavaScript and CSS assets through
'htmltools'. Entity lookup and rendering are handled in the browser by
'bio-tooltips'; this package does not query biological databases from R
during package checks.

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
