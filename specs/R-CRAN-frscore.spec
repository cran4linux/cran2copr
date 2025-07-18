%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  frscore
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate the Fit-Robustness of CNA-Solutions

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cna >= 3.5.1
BuildRequires:    R-CRAN-lifecycle >= 1.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-cna >= 3.5.1
Requires:         R-CRAN-lifecycle >= 1.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-igraph 

%description
Automatically perform a reanalysis series on a data set using CNA, and
calculate the fit-robustness of the resulting models, as described in
Parkkinen and Baumgartner (2021) <doi:10.1177/0049124120986200>.

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
