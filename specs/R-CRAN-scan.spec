%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scan
%global packver   0.59.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.59.0
Release:          1%{?dist}%{?buildtag}
Summary:          Single-Case Data Analyses for Single and Multiple Baseline Designs

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-mblm 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-nlme 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-car 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-mblm 
Requires:         R-CRAN-magrittr 

%description
A collection of procedures for analysing, visualising, and managing
single-case data. These include piecewise linear regression models,
multilevel models, overlap indices ('PND', 'PEM', 'PAND', 'PET', 'tau-u',
'baseline corrected tau', 'CDC'), and randomization tests. Data
preparation functions support outlier detection, handling missing values,
scaling, truncation, rank transformation, and smoothing. An export
function helps to generate html and latex tables in a publication friendly
style. More details can be found in the online book 'Analyzing single-case
data with R and scan', Juergen Wilbert (2023)
<https://jazznbass.github.io/scan-Book/>.

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
