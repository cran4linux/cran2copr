%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dynamicSDM
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Species Distribution and Abundance Modelling at High Spatio-Temporal Resolution

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rgee 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-googledrive 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rgee 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tidyr 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-readr 

%description
A collection of novel tools for generating species distribution and
abundance models (SDM) that are dynamic through both space and time. These
highly flexible functions incorporate spatial and temporal aspects across
key SDM stages; including when cleaning and filtering species occurrence
data, generating pseudo-absence records, assessing and correcting sampling
biases and autocorrelation, extracting explanatory variables and
projecting distribution patterns. Throughout, functions utilise Google
Earth Engine and Google Drive to minimise the computing power and storage
demands associated with species distribution modelling at high
spatio-temporal resolution.

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
