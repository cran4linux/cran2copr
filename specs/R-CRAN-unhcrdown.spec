%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  unhcrdown
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          UNHCR Branded Templates for R Markdown Documents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-officedown 
BuildRequires:    R-CRAN-pagedown 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-xaringan 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-officedown 
Requires:         R-CRAN-pagedown 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-xaringan 

%description
Create United Nations High Commissioner for Refugees (UNHCR) branded
documents, presentations, and reports using R Markdown templates. This
package provides customized formats that align with UNHCR's official brand
guidelines for creating professional PDF reports, Word documents,
PowerPoint presentations, and HTML outputs.

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
