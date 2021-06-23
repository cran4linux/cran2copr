%global __brp_check_rpaths %{nil}
%global packname  equatags
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Equations to 'XML'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-xslt 
BuildRequires:    R-CRAN-locatexec 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-xslt 
Requires:         R-CRAN-locatexec 

%description
Provides function transform_mathjax() to transform equations defined using
'MathML', 'LaTeX' or 'ASCIIMathML' notation into format 'SVG' or 'Office
Open XML Math'. The 'XML' result can then be included in 'HTML',
'Microsoft Word' documents or 'Microsoft PowerPoint' presentations by
using a 'Markdown' document or the R package 'officer'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
