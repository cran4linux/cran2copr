%global __brp_check_rpaths %{nil}
%global packname  babsim.hospital
%global packver   11.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          11.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bartz & Bartz Simulation Hospital

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SPOT 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-markovchain 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-padr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-simmer 
BuildRequires:    R-CRAN-slider 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-SPOT 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-markovchain 
Requires:         R-methods 
Requires:         R-CRAN-padr 
Requires:         R-parallel 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-simmer 
Requires:         R-CRAN-slider 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-xml2 

%description
Implements a discrete-event simulation model for a hospital resource
planning problem. The project is motivated by the challenges faced by
health care institutions in the current COVID-19 pandemic. It can be used
by health departments to forecast demand for intensive care beds,
ventilators, and staff resources. Our modelling approach is inspired by "A
novel modelling technique to predict resource requirements in critical
care - a case study" (Lawton and McCooe 2019) and combines two powerful
technologies: (i) discrete event simulation using the 'simmer' package and
(ii) model-based optimization using 'SPOT'. Ucar I, Smeets B, Azcorra A
(2019) <doi:10.18637/jss.v090.i02>. Bartz-Beielstein T, Lasarczyk C W G,
Preuss M (2005) <doi:10.1109/CEC.2005.1554761>. Lawton T, McCooe M (2019)
<doi:10.7861/futurehosp.6-1-17>.

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
