%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DDIwR
%global packver   0.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.18
Release:          1%{?dist}%{?buildtag}
Summary:          DDI with R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-admisc > 0.33
BuildRequires:    R-CRAN-declared > 0.23
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-admisc > 0.33
Requires:         R-CRAN-declared > 0.23
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-digest 
Requires:         R-tools 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-writexl 

%description
Useful functions for various DDI (Data Documentation Initiative) related
inputs and outputs. Converts data files to and from DDI, SPSS, Stata, SAS,
R and Excel, including user declared missing values.

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
