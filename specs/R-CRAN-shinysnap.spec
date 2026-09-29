%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinysnap
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Save and Restore the State of 'shiny' Applications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.8.0
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zmij 
Requires:         R-CRAN-shiny >= 1.8.0
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-R6 
Requires:         R-utils 
Requires:         R-CRAN-zmij 

%description
Save the state of applications built with 'shiny', the web application
framework by Chang et al. (2026) <doi:10.32614/CRAN.package.shiny>. Users
can share their work and continue it in another session. Input values and
selected values held by the server are saved in JSON (JavaScript Object
Notation) files that can be read and edited by hand. Saved state can be
restored without reloading the page or setting up bookmarking. Restoration
waits for inputs that appear as the page changes and reports which values
were restored, missing, or could not be applied.

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
