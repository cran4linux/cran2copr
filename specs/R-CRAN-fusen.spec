%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fusen
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Build a Package from Rmarkdown Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-usethis >= 2.0.0
BuildRequires:    R-CRAN-here >= 1.0.0
BuildRequires:    R-CRAN-attachment 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lightparser 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-usethis >= 2.0.0
Requires:         R-CRAN-here >= 1.0.0
Requires:         R-CRAN-attachment 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lightparser 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-roxygen2 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
Use Rmarkdown First method to build your package. Start your package with
documentation, functions, examples and tests in the same unique file.
Everything can be set from the Rmarkdown template file provided in your
project, then inflated as a package. Inflating the template copies the
relevant chunks and sections in the appropriate files required for package
development.

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
