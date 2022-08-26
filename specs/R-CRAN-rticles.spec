%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rticles
%global packver   0.24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.24
Release:          1%{?dist}%{?buildtag}
Summary:          Article Formats for R Markdown

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 2.14
BuildRequires:    R-CRAN-knitr >= 1.30
BuildRequires:    R-CRAN-tinytex >= 0.30
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-rmarkdown >= 2.14
Requires:         R-CRAN-knitr >= 1.30
Requires:         R-CRAN-tinytex >= 0.30
Requires:         R-utils 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-yaml 

%description
A suite of custom R Markdown formats and templates for authoring journal
articles and conference submissions.

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
