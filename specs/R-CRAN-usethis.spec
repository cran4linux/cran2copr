%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  usethis
%global packver   2.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Automate Package and Project Setup

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.1
BuildRequires:    R-CRAN-curl >= 2.7
BuildRequires:    R-CRAN-withr >= 2.3.0
BuildRequires:    R-CRAN-desc >= 1.4.2
BuildRequires:    R-CRAN-gert >= 1.4.1
BuildRequires:    R-CRAN-fs >= 1.3.0
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-gh >= 1.2.1
BuildRequires:    R-CRAN-rprojroot >= 1.2
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.0
BuildRequires:    R-CRAN-clipr >= 0.3.0
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-cli >= 3.0.1
Requires:         R-CRAN-curl >= 2.7
Requires:         R-CRAN-withr >= 2.3.0
Requires:         R-CRAN-desc >= 1.4.2
Requires:         R-CRAN-gert >= 1.4.1
Requires:         R-CRAN-fs >= 1.3.0
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-gh >= 1.2.1
Requires:         R-CRAN-rprojroot >= 1.2
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-lifecycle >= 1.0.0
Requires:         R-CRAN-clipr >= 0.3.0
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rstudioapi 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-yaml 

%description
Automate package and project setup tasks that are otherwise performed
manually. This includes setting up unit testing, test coverage, continuous
integration, Git, 'GitHub', licenses, 'Rcpp', 'RStudio' projects, and
more.

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
