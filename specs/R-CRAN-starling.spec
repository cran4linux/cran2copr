%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  starling
%global packver   0.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Link Infectious Disease Cases to Vaccination and Hospitalization Records

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-reclin2 
BuildRequires:    R-CRAN-datawizard 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-reclin2 
Requires:         R-CRAN-datawizard 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 

%description
Facilitates probabilistic record linkage between infectious disease
surveillance datasets (notifiable disease registers, outbreak line-lists),
vaccination registries, and hospitalization records using methods based on
Fellegi and Sunter (1969) <doi:10.1080/01621459.1969.10501049> and Sayers
et al. (2016) <doi:10.1093/ije/dyv322>. The package provides core
functions for data preparation, linkage, and analysis: clean_the_nest()
standardizes variable names and formats across heterogeneous datasets;
murmuration() performs machine learning-based record linkage using
blocking variables and similarity metrics; molting() deidentifies datasets
for secure sharing; homing() re-identifies previously deidentified
datasets; plumage() identifies and categorizes comorbidities; and
preening() creates analysis-ready variables including age categories and
temporal groupings. Designed for epidemiological research linking acute
and post-acute disease outcomes to vaccination status and healthcare
utilization. Supports multiple linkage scenarios including
case-to-vaccination, case-to-hospitalization, and event-based vaccination
status determination (e.g., outbreak attendees, flight passengers,
exposure site visitors).

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
