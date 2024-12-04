%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  npclust
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Tests for Incomplete Clustered Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 

%description
Nonparametric tests for clustered data in pre-post intervention design
documented in Cui and Harrar (2021) <doi:10.1002/bimj.201900310> and
Harrar and Cui (2022) <doi:10.1016/j.jspi.2022.05.009>. Other than the
main test results mentioned in the reference paper, this package also
provides a function to calculate the sample size allocations for the input
long format data set, and also a function for adjusted/unadjusted
confidence intervals calculations. There are also functions to visualize
the distribution of data across different intervention groups over time,
and also the adjusted/unadjusted confidence intervals.

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
