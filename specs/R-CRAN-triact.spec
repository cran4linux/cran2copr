%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  triact
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing the Lying Behavior of Cows from Accelerometer Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-parallel >= 4.1.2
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-lubridate >= 1.7.10
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-parallel >= 4.1.2
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-lubridate >= 1.7.10
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-methods 
Requires:         R-stats 

%description
Assists in analyzing the lying behavior of cows from raw data recorded
with a triaxial accelerometer attached to the hind leg of a cow. Allows
the determination of common measures for lying behavior including total
lying duration, the number of lying bouts, and the mean duration of lying
bouts. Further capabilities are the description of lying laterality and
the calculation of proxies for the level of physical activity of the cow.
Reference: Simmler M., Brouwers S. (2023)
<https://gitlab.com/AgroSimi/triact_manuscript>.

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
