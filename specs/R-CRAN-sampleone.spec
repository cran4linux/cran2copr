%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sampleone
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Survey Sampling Methods for Teaching and Practice

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Planning, selection, and estimation for surveys under the main probability
sampling designs taught in introductory sampling courses: simple random
sampling with and without replacement, stratified sampling (proportional,
Neyman, and cost-based allocation), systematic sampling, one- and
two-stage cluster sampling, and ratio and regression estimators. Functions
accept a superset of the inputs a given formula requires and silently
ignore arguments that are not needed for the selected computation. Each
function returns a structured object with the point estimate, the
associated variance and confidence interval, a step-by-step breakdown of
the calculation, and a short pedagogical note suggesting related methods
to explore, making the package suitable both for applied survey work and
for classroom use. Methods follow Cochran (1977, ISBN:0-471-16240-X) and
Bolfarine & Bussab (2005, ISBN:8521203675), among others referenced in
each function's documentation.

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
