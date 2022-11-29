%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reporter
%global packver   1.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.8
Release:          1%{?dist}%{?buildtag}
Summary:          Creates Statistical Reports

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-common 
BuildRequires:    R-CRAN-fmtr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-common 
Requires:         R-CRAN-fmtr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-jpeg 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-glue 

%description
Contains functions to create regulatory-style statistical reports.
Originally designed to create tables, listings, and figures for the
pharmaceutical, biotechnology, and medical device industries, these
reports are generalized enough that they could be used in any industry.
Generates text, rich-text, PDF, HTML, and Microsoft Word file formats. The
package specializes in printing wide and long tables with automatic page
wrapping and splitting. Reports can be produced with a minimum of function
calls, and without relying on other table packages.  The package supports
titles, footnotes, page header, page footers, spanning headers, page by
variables, and automatic page numbering.

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
