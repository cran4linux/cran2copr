%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sketchy
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Create Custom Research Compendiums

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-packrat 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-xaringanExtra 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-packrat 
Requires:         R-utils 
Requires:         R-CRAN-git2r 
Requires:         R-CRAN-xaringanExtra 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-cli 

%description
Provides functions to create and manage research compendiums for data
analysis. Research compendiums are a standard and intuitive folder
structure for organizing the digital materials of a research project,
which can significantly improve reproducibility. The package offers
several compendium structure options that fit different research project
as well as the ability of duplicating the folder structure of existing
projects or implementing custom structures. It also simplifies the use of
version control.

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
