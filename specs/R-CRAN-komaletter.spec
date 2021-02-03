%global packname  komaletter
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simply Beautiful PDF Letters from Markdown

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 0.6
Requires:         R-CRAN-rmarkdown >= 0.6

%description
Write beautiful yet customizable letters in R Markdown and directly obtain
the finished PDF. Smooth generation of PDFs is realized by 'rmarkdown',
the 'pandoc-letter' template and the 'KOMA-Script' letter class.
'KOMA-Script' provides enhanced replacements for the standard 'LaTeX'
classes with emphasis on typography and versatility. 'KOMA-Script' is
particularly useful for international writers as it handles various paper
formats well, provides layouts for many common window envelope types (e.g.
German, US, French, Japanese) and lets you define your own layouts. The
package comes with a default letter layout based on 'DIN 5008B'.

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
