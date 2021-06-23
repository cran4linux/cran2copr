%global __brp_check_rpaths %{nil}
%global packname  addinslist
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Discover and Install Useful RStudio Addins

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinyjs >= 0.6
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
BuildRequires:    R-CRAN-rvest >= 0.3.1
BuildRequires:    R-CRAN-shiny >= 0.13.2
BuildRequires:    R-CRAN-xml2 >= 0.1.2
BuildRequires:    R-CRAN-DT >= 0.1
BuildRequires:    R-CRAN-miniUI >= 0.1
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-utils 
Requires:         R-CRAN-shinyjs >= 0.6
Requires:         R-CRAN-rappdirs >= 0.3.1
Requires:         R-CRAN-rvest >= 0.3.1
Requires:         R-CRAN-shiny >= 0.13.2
Requires:         R-CRAN-xml2 >= 0.1.2
Requires:         R-CRAN-DT >= 0.1
Requires:         R-CRAN-miniUI >= 0.1
Requires:         R-CRAN-curl 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-rmarkdown 
Requires:         R-utils 

%description
Browse through a continuously updated list of existing RStudio addins and
install/uninstall their corresponding packages.

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
