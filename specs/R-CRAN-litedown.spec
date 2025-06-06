%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  litedown
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          1%{?dist}%{?buildtag}
Summary:          A Lightweight Version of R Markdown

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-commonmark >= 1.9.5
BuildRequires:    R-CRAN-xfun >= 0.52
BuildRequires:    R-utils 
Requires:         R-CRAN-commonmark >= 1.9.5
Requires:         R-CRAN-xfun >= 0.52
Requires:         R-utils 

%description
Render R Markdown to Markdown (without using 'knitr'), and Markdown to
lightweight HTML or 'LaTeX' documents with the 'commonmark' package
(instead of 'Pandoc'). Some missing Markdown features in 'commonmark' are
also supported, such as raw HTML or 'LaTeX' blocks, 'LaTeX' math,
superscripts, subscripts, footnotes, element attributes, and appendices,
but not all 'Pandoc' Markdown features are (or will be) supported. With
additional JavaScript and CSS, you can also create HTML slides and
articles. This package can be viewed as a trimmed-down version of R
Markdown and 'knitr'. It does not aim at rich Markdown features or a large
variety of output formats (the primary formats are HTML and 'LaTeX'). Book
and website projects of multiple input documents are also supported.

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
