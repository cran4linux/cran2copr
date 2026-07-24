%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  whatifbandit
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Randomized Experiments Using Multi-Arm Bandits

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.18.0
BuildRequires:    R-CRAN-bandit 
BuildRequires:    R-CRAN-clubSandwich 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-estimatr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-randomizr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-data.table >= 1.18.0
Requires:         R-CRAN-bandit 
Requires:         R-CRAN-clubSandwich 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-estimatr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-randomizr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Simulates response-adaptive experimental trials using Multi-Arm Bandits.
Adaptive robust estimators defined in Hadad et al. (2021)
<doi:10.1073/pnas.2014602118> and Offer-Westort et al. (2021)
<doi:10.1111/ajps.12597> are used to robustly estimate conditional
expectations and treatment effects. Provides significant simulation
customization options for imperfect information, non-stationary bandits,
and increased exploration strategies for assignments.

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
