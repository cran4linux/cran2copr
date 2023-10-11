%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rphylopic
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Get Silhouettes of Organisms from PhyloPic

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rsvg >= 2.6.0
BuildRequires:    R-CRAN-grImport2 >= 0.3.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-grid 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-rsvg >= 2.6.0
Requires:         R-CRAN-grImport2 >= 0.3.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jsonlite 
Requires:         R-grid 
Requires:         R-graphics 
Requires:         R-CRAN-png 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 
Requires:         R-methods 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-knitr 

%description
Work with the PhyloPic Web Service (<http://api-docs.phylopic.org/v2/>) to
fetch silhouette images of organisms. Includes functions for adding
silhouettes to both base R plots and ggplot2 plots.

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
