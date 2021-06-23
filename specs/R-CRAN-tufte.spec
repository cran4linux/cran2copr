%global __brp_check_rpaths %{nil}
%global packname  tufte
%global packver   0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Tufte's Styles for R Markdown Documents

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 2.1
BuildRequires:    R-CRAN-knitr >= 1.28
BuildRequires:    R-CRAN-xfun >= 0.13
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-rmarkdown >= 2.1
Requires:         R-CRAN-knitr >= 1.28
Requires:         R-CRAN-xfun >= 0.13
Requires:         R-CRAN-htmltools 

%description
Provides R Markdown output formats to use Tufte styles for PDF and HTML
output.

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
