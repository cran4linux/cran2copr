%global __brp_check_rpaths %{nil}
%global packname  xaringan
%global packver   0.24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.24
Release:          1%{?dist}%{?buildtag}
Summary:          Presentation Ninja

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 2.8
BuildRequires:    R-CRAN-knitr >= 1.30
BuildRequires:    R-CRAN-xfun >= 0.18
BuildRequires:    R-CRAN-servr >= 0.13
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-rmarkdown >= 2.8
Requires:         R-CRAN-knitr >= 1.30
Requires:         R-CRAN-xfun >= 0.18
Requires:         R-CRAN-servr >= 0.13
Requires:         R-CRAN-htmltools 

%description
Create HTML5 slides with R Markdown and the JavaScript library 'remark.js'
(<https://remarkjs.com>).

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
