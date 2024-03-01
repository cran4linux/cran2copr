%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  agcounts
%global packver   0.6.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.6
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate 'ActiGraph' Counts from Accelerometer Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-gsignal 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-GGIR 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-read.gt3x 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-gsignal 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-GGIR 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-read.gt3x 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 

%description
Calculate 'ActiGraph' counts from the X, Y, and Z axes of a triaxial
accelerometer. This work was inspired by Neishabouri et al. who published
the article "Quantification of Acceleration as Activity Counts in
'ActiGraph' Wearables" on February 24, 2022. The link to the article
(<https://pubmed.ncbi.nlm.nih.gov/35831446>) and 'python' implementation
of this code (<https://github.com/actigraph/agcounts>).

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
