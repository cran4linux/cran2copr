%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FAMetA
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Fatty Acid Metabolic Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-LipidMS >= 3.0.4
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-accucor 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-LipidMS >= 3.0.4
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-accucor 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-gplots 
Requires:         R-grDevices 

%description
Fatty acid metabolic analysis aimed to the estimation of FA import (I), de
novo synthesis (S), fractional contribution of the 13C-tracers (D0, D1,
D2), elongation (E) and desaturation (Des) based on mass isotopologue
data.

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
