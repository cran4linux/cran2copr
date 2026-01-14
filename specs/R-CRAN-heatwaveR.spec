%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  heatwaveR
%global packver   0.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          Detect Heatwaves and Cold-Spells

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fasttime 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fasttime 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-RcppRoll 
Requires:         R-stats 
Requires:         R-utils 

%description
The different methods for defining, detecting, and categorising the
extreme events known as heatwaves or cold-spells, as first proposed in
Hobday et al. (2016) <doi: 10.1016/j.pocean.2015.12.014> and Hobday et al.
(2018) <https://www.jstor.org/stable/26542662>. The functions in this
package work on both air and water temperature data of hourly and daily
temporal resolution. These detection algorithms may be used on
non-temperature data as well.

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
