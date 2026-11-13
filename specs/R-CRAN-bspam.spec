%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bspam
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Speed-Accuracy Psychometric Modeling for Binomial Count Outcome Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-tryCatchLog 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-miscTools 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-tryCatchLog 
Requires:         R-parallel 
Requires:         R-CRAN-miscTools 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-statmod 

%description
Provides functions to fit speed-accuracy psychometric models for binomial
count outcome data. The models jointly represent accuracy and response
time and can be used for model-based calibration and scoring of oral
reading fluency (ORF) assessment data. The methods are based on Potgieter,
Kamata and Kara (2017) <doi:10.48550/arXiv.1705.10446> and Kara, Kamata,
Potgieter and Nese (2020) <doi:10.1177/0013164419900208>.

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
