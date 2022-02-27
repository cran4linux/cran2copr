%global __brp_check_rpaths %{nil}
%global packname  mxnorm
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Apply Normalization Methods to Multiplexed Images

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-kSamples 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-fossil 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-fda 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-kSamples 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-fossil 
Requires:         R-CRAN-glue 
Requires:         R-methods 

%description
Implements methods to normalize multiplexed imaging data, including
statistical metrics and visualizations to quantify technical variation in
this data type.

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
