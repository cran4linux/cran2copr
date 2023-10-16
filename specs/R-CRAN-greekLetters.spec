%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  greekLetters
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Routines for Writing Greek Letters and Mathematical Symbols on the 'RStudio' and 'RGui'

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-assertthat 

%description
An implementation of functions to display Greek letters on the 'RStudio'
(include subscript and superscript indexes) and 'RGui' (without subscripts
and only with superscript 1, 2 or 3; because 'RGui' doesn't support
printing the corresponding Unicode characters as a string: all subscripts
ranging from 0 to 9 and superscripts equal to 0, 4, 5, 6, 7, 8 or 9). The
functions in this package do not work properly on the R console.
Characters are used via Unicode and encoded as UTF-8 to ensure that they
can be viewed on all operating systems. Other characters related to
mathematics are included, such as the infinity symbol. All this accessible
from very simple commands. This is a package that can be used for teaching
purposes, the statistical notation for hypothesis testing can be written
from this package and so it is possible to build a course from the
'swirlify' package. Another utility of this package is to create new
summary functions that contain the functional form of the model adjusted
with the Greek letters, thus making the transition from statistical theory
to practice easier. In addition, it is a natural extension of the
'clisymbols' package.

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
