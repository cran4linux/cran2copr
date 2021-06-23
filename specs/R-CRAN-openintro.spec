%global __brp_check_rpaths %{nil}
%global packname  openintro
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Sets and Supplemental Functions from 'OpenIntro' Textbooks and Labs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-airports 
BuildRequires:    R-CRAN-cherryblossom 
BuildRequires:    R-CRAN-usdata 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-airports 
Requires:         R-CRAN-cherryblossom 
Requires:         R-CRAN-usdata 
Requires:         R-graphics 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-tibble 

%description
Supplemental functions and data for 'OpenIntro' resources, which includes
open-source textbooks and resources for introductory statistics
(<https://www.openintro.org/>). The package contains data sets used in our
open-source textbooks along with custom plotting functions for reproducing
book figures. Note that many functions and examples include color
transparency; some plotting elements may not show up properly (or at all)
when run in some versions of Windows operating system.

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
