%global __brp_check_rpaths %{nil}
%global packname  cleanr
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Helps You to Code Cleaner

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-fritools 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-rprojroot 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-fritools 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-rprojroot 

%description
Check your R code for some of the most common layout flaws.  Many tried to
teach us how to write code less dreadful, be it implicitly as B. W.
Kernighan and D. M. Ritchie (1988) <ISBN:0-13-110362-8> in 'The C
Programming Language' did, be it explicitly as R.C. Martin (2008)
<ISBN:0-13-235088-2> in 'Clean Code: A Handbook of Agile Software
Craftsmanship' did.  So we should check our code for files too long or
wide, functions with too many lines, too wide lines, too many arguments or
too many levels of nesting. Note: This is not a static code analyzer like
pylint or the like. Checkout <https://cran.r-project.org/package=lintr>
instead.

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
