%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simulateDCE
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Data for Discrete Choice Experiments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mixl 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-qs 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-evd 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mixl 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-qs 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-glue 

%description
Supports simulating choice experiment data for given designs. It helps to
quickly test different designs against each other and compare the
performance of new models. The goal of 'simulateDCE' is to make it easy to
simulate choice experiment datasets using designs from 'NGENE', 'idefix'
or 'spdesign'. You have to store the design file(s) in a sub-directory and
need to specify certain parameters and the utility functions for the data
generating process. For more details on choice experiments see Mariel et
al. (2021) <doi:10.1007/978-3-030-62669-3>.

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
