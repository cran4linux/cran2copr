%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rsf
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Report of Statistical Findings in 'bookdown'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-renv 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-ymlthis 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-here 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-renv 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-ymlthis 

%description
A report of statistical findings (RSF) project template is generated using
a 'bookdown' format. 'YAML' fields can be further customized. Additional
helper functions provide extra features to the RSF.

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
