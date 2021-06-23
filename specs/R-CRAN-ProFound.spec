%global __brp_check_rpaths %{nil}
%global packname  ProFound
%global packver   1.14.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.14.1
Release:          1%{?dist}%{?buildtag}
Summary:          Photometry Tools

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-magicaxis >= 2.0.8
BuildRequires:    R-CRAN-celestial >= 1.4.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-FITSio 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-magicaxis >= 2.0.8
Requires:         R-CRAN-celestial >= 1.4.1
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-FITSio 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 

%description
Core package containing all the tools for simple and advanced source
extraction. This is used to create inputs for 'ProFit', or for source
detection, extraction and photometry in its own right.

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
