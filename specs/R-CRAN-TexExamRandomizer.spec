%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TexExamRandomizer
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Personalizes and Randomizes Exams Written in 'LaTeX'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       latexmk
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-utils 

%description
Randomizing exams with 'LaTeX'. If you can compile your main document with
'LaTeX', the program should be able to compile the randomized versions
without much extra effort when creating the document.

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
