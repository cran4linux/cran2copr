%global __brp_check_rpaths %{nil}
%global packname  SMITIDvisu
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Visualize Data for Host and Viral Population from 'SMITIDstruct' using 'HTMLwidgets'

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-yaml >= 2.1.16
BuildRequires:    R-CRAN-jsonlite >= 1.5.0
BuildRequires:    R-CRAN-htmlwidgets >= 0.3.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-yaml >= 2.1.16
Requires:         R-CRAN-jsonlite >= 1.5.0
Requires:         R-CRAN-htmlwidgets >= 0.3.2
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-utils 
Requires:         R-CRAN-magrittr 

%description
Visualisation tools for 'SMITIDstruct' package. Allow to visualize host
timeline, transmission tree, index diversities and variant graph using
'HTMLwidgets'. It mainly using 'D3JS' javascript framework.

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
