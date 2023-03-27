%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmarkdown
%global packver   2.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.21
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Documents for R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.1.19
BuildRequires:    R-CRAN-knitr >= 1.22
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-htmltools >= 0.5.1
BuildRequires:    R-CRAN-fontawesome >= 0.5.0
BuildRequires:    R-CRAN-xfun >= 0.36
BuildRequires:    R-CRAN-tinytex >= 0.31
BuildRequires:    R-CRAN-bslib >= 0.2.5.1
BuildRequires:    R-CRAN-evaluate >= 0.13
BuildRequires:    R-CRAN-jquerylib 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-yaml >= 2.1.19
Requires:         R-CRAN-knitr >= 1.22
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-htmltools >= 0.5.1
Requires:         R-CRAN-fontawesome >= 0.5.0
Requires:         R-CRAN-xfun >= 0.36
Requires:         R-CRAN-tinytex >= 0.31
Requires:         R-CRAN-bslib >= 0.2.5.1
Requires:         R-CRAN-evaluate >= 0.13
Requires:         R-CRAN-jquerylib 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-utils 

%description
Convert R Markdown documents into a variety of formats.

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
