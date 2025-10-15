%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  myCRAN
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Graph of Daily and Cumulative Downloads of your Packages

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cranlogs 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-pkgsearch 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-stats 
Requires:         R-CRAN-cranlogs 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-pkgsearch 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-lubridate 
Requires:         R-stats 

%description
Plot the daily and cumulative number of downloads of your packages. It is
designed to be slightly more convenient than the several similar programs.
If you want to run this each morning, you do not need to keep typing in
the names of your packages. Also, this combines the daily and cumulative
counts in one run, you do not need to run separate programs to get both
types of information.

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
