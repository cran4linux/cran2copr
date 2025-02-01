%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  YEAB
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Data from Analysis of Behavior Experiments

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-Polychrome 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-boot 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-Polychrome 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-usethis 
Requires:         R-stats 
Requires:         R-utils 

%description
Analyze data from behavioral experiments conducted using 'MED-PC' software
developed by Med Associates Inc. Includes functions to fit exponential and
hyperbolic models for delay discounting tasks, exponential mixtures for
inter-response times, and Gaussian plus ramp models for peak procedure
data, among others. For more details, refer to Alcala et al. (2023)
<doi:10.31234/osf.io/8aq2j>.

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
