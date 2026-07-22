%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  facomplex
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Assessing Factor Complexity in Factor Analysis Solutions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
Provides methods for estimating factor complexity coefficients in
exploratory and confirmatory factor analysis (EFA/CFA) results. Included
indices are the Hofman coefficient, Fleming's approach for factor
simplicity, and others. Additional outputs include descriptive statistics
(minimum, maximum, and mean) for target and non-target loadings, and
visualization of results. References: Fleming, J.S. (2003)
<doi:10.3758/bf03195531>; Hofmann, R.J. (1978)
<doi:10.1207/s15327906mbr1302_9>; Kaiser, H.F. (1974)
<doi:10.1007/BF02291575>; Bentler, P.M. (1977) <doi:10.1007/BF02294054>;
Lorenzo-Seva, U. (2003) <doi:10.1007/BF02296652>.

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
