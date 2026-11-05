%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FARM.eval
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          FARM Algorithm Evaluation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FARM 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-DTWBI 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-nanoparquet 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-tsmp 
BuildRequires:    R-CRAN-optparse 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-FARM 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-readr 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-DTWBI 
Requires:         R-CRAN-reticulate 
Requires:         R-graphics 
Requires:         R-CRAN-shape 
Requires:         R-utils 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-nanoparquet 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-tsmp 
Requires:         R-CRAN-optparse 
Requires:         R-CRAN-tidyr 

%description
Providing data sets and functions used for evaluating the FARM (Forward
Alignment Relevance Measure) algorithm. Datasets include energy
consumption series from a university research cube in combination with two
and four exogenous series consisting 768 and 62840 samples, respectively.
To run particular functions from terminal: Rscript $(R -e
'cat(system.file("scripts","FARM.eval.R",package = "FARM.eval"))')
--fexecute get.global.rel.meas --parworkers 1 --parobjsize 500.

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
