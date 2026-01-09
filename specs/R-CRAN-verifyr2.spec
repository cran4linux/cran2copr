%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  verifyr2
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compare and Verify File Contents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-diffobj 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-striprtf 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-diffobj 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-striprtf 
Requires:         R-CRAN-tibble 

%description
Extendable 'R6' file comparison classes, including a 'shiny' app for
combining the comparison functionality into a file comparison application.
The package idea originates from pharma companies' drug development
processes, where statisticians and statistical programmers need to review
and compare different versions of the same outputs and datasets. The
package implementation itself is not tied to any specific industry and can
be used in any context for easy file comparisons between different file
version sets.

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
