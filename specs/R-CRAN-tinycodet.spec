%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tinycodet
%global packver   0.5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.8
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Help in your Coding Etiquette

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-stringi >= 1.7.12
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-stringi >= 1.7.12
Requires:         R-CRAN-Rcpp >= 1.0.11

%description
Adds some functions to help in your coding etiquette. 'tinycodet'
primarily focuses on 4 aspects. 1) Safer decimal (in)equality testing,
standard-evaluated alternatives to with() and aes(), and other functions
for safer coding. 2) A new package import system, that attempts to combine
the benefits of using a package without attaching it, with the benefits of
attaching a package. 3) Extending the string manipulation capabilities of
the 'stringi' R package. 4) Reducing repetitive code. Besides linking to
'Rcpp', 'tinycodet' has only one other dependency, namely 'stringi'.

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
