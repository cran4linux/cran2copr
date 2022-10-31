%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  markdown
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Render Markdown with 'commonmark'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.1
Requires:         R-core >= 2.11.1
BuildArch:        noarch
BuildRequires:    R-CRAN-mime >= 0.3
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-xfun 
Requires:         R-CRAN-mime >= 0.3
Requires:         R-utils 
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-xfun 

%description
Render Markdown to full HTML documents with the 'commonmark' package.
Markdown is a plain-text formatting syntax that can be converted to
'XHTML' or other formats. See <https://en.wikipedia.org/wiki/Markdown> for
more information about Markdown.

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
