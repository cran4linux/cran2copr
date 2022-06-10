%global __brp_check_rpaths %{nil}
%global packname  starticles
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Generic, Publisher-Independent Template for Writing Scientific Documents in 'rmarkdown'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel > 3.5.0
Requires:         R-core > 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-knitr 

%description
Provides a generic, publisher-independent Rmarkdown template for writing
scientific papers and reports in Rmarkdown. The template allows for all
the basic features of a scientific article, including a title page with
author affiliations and footnotes possibly shown in two common formats,
multi-language abstracts and keywords, page headers and footers, and the
ability to place figures and tables at the end of the output PDF. Smart
cross-referencing of figures, tables, equations and sections is provided
using the bookdown package. See package README.md for basic package usage.

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
