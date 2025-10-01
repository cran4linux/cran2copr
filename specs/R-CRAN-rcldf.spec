%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcldf
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Read Linguistic Data in the Cross Linguistic Data Format (CLDF)

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bib2df >= 1.1.1
BuildRequires:    R-CRAN-archive 
BuildRequires:    R-CRAN-csvwr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-utils 
Requires:         R-CRAN-bib2df >= 1.1.1
Requires:         R-CRAN-archive 
Requires:         R-CRAN-csvwr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-logger 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-rlang 
Requires:         R-tools 
Requires:         R-CRAN-urltools 
Requires:         R-utils 

%description
Cross-Linguistic Data Format (CLDF) is a framework for storing
cross-linguistic data, ensuring compatibility and ease of data exchange
between different linguistic datasets see Forkel et al. (2018)
<doi:10.1038/sdata.2018.205>. The 'rcldf' package is designed to
facilitate the manipulation and analysis of these datasets by simplifying
the loading, querying, and visualisation of CLDF datasets making it easier
to conduct comparative linguistic analyses, manage language data, and
apply statistical methods directly within R.

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
