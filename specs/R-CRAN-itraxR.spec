%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  itraxR
%global packver   1.12.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12.2
Release:          1%{?dist}%{?buildtag}
Summary:          Itrax Data Analysis Tools

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-compositions 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-munsellinterpol 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-compositions 
Requires:         R-grid 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-munsellinterpol 
Requires:         R-utils 

%description
Parse, trim, join, visualise and analyse data from Itrax sediment core
multi-parameter scanners manufactured by Cox Analytical Systems, Sweden.
Functions are provided for parsing XRF-peak area files, line-scan optical
images, and radiographic images, alongside accompanying metadata. A
variety of data wrangling tasks like trimming, joining and reducing
XRF-peak area data are simplified. Multivariate methods are implemented
with appropriate data transformation.

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
