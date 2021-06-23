%global __brp_check_rpaths %{nil}
%global packname  TeXCheckR
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parses LaTeX Documents for Errors

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-hunspell >= 2.5
BuildRequires:    R-CRAN-data.table >= 1.9.0
BuildRequires:    R-CRAN-hutils >= 0.8.0
BuildRequires:    R-CRAN-clisymbols 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-hunspell >= 2.5
Requires:         R-CRAN-data.table >= 1.9.0
Requires:         R-CRAN-hutils >= 0.8.0
Requires:         R-CRAN-clisymbols 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-CRAN-zoo 

%description
Checks LaTeX documents and .bib files for typing errors, such as spelling
errors, incorrect quotation marks. Also provides useful functions for
parsing and linting bibliography files.

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
