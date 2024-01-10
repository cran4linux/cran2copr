%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iopspackage
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          IO-PS Framework Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-economiccomplexity 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-economiccomplexity 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-usethis 

%description
A developmental R tool related to the input-output product space (IO-PS).
The package requires two compulsory user inputs (raw CEPPI BACI trade
data, and any acceptable ISO country code) and has 4 optional user inputs
(a value chain map, chosen complexity method, number of iterations to be
performed, and a trade digit level). Various metrics are calculated, such
as Economic- and Product complexity, distance, opportunity gain, and
inequality metrics, to facilitate better decision making regarding
industrial policy making.

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
