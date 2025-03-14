%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clinify
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Clinical Table Styling Tools and Utilities

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-zoo 

%description
The primary motivation of this package is to take the things that are
great about the R packages 'flextable'
<https://davidgohel.github.io/flextable/> and 'officer'
<https://davidgohel.github.io/officer/>, take the standard and complex
pieces of formatting clinical tables for regulatory use, and simplify the
tedious pieces.

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
