%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lab2clean
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automation and Standardization of Cleaning Clinical Laboratory Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-stats 
Requires:         R-utils 

%description
Navigating the shift of clinical laboratory data from primary everyday
clinical use to secondary research purposes presents a significant
challenge. Given the substantial time and expertise required for lab data
pre-processing and cleaning and the lack of all-in-one tools tailored for
this need, we developed our algorithm 'lab2clean' as an open-source
R-package. 'lab2clean' package is set to automate and standardize the
intricate process of cleaning clinical laboratory results. With a keen
focus on improving the data quality of laboratory result values and units,
our goal is to equip researchers with a straightforward, plug-and-play
tool, making it smoother for them to unlock the true potential of clinical
laboratory data in clinical research and clinical machine learning (ML)
model development. Functions to clean & validate result values (Version
1.0) are described in detail in 'Zayed et al. (2024)'
<doi:10.1186/s12911-024-02652-7>. Functions to standardize & harmonize
result units (added in Version 2.0) are described in detail in 'Zayed et
al. (2025)' <doi:10.1016/j.ijmedinf.2025.106131>.

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
