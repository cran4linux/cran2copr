%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  markdown
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Render Markdown with 'commonmark'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.1
Requires:         R-core >= 2.11.1
BuildArch:        noarch
BuildRequires:    R-CRAN-commonmark >= 1.9.0
BuildRequires:    R-CRAN-xfun >= 0.38
BuildRequires:    R-utils 
Requires:         R-CRAN-commonmark >= 1.9.0
Requires:         R-CRAN-xfun >= 0.38
Requires:         R-utils 

%description
Render Markdown to full and lightweight HTML/'LaTeX' documents with the
'commonmark' package. It also supports features that are missing in
'commonmark', such as raw HTML/'LaTeX' blocks, 'LaTeX' math, superscripts,
subscripts, footnotes, element attributes, appendices, and fenced 'Divs'.
With additional JavaScript and CSS, it can also create HTML slides and
articles.

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
