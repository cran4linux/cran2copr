%global __brp_check_rpaths %{nil}
%global packname  RHawkes
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Renewal Hawkes Process

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-IHSEP 
Requires:         R-CRAN-IHSEP 

%description
The renewal Hawkes (RHawkes) process (Wheatley, Filimonov, and Sornette,
2016 <doi:10.1016/j.csda.2015.08.007>) is an extension to the classical
Hawkes self-exciting point process widely used in the modelling of
clustered event sequence data. This package provides functions to simulate
the RHawkes process with a given immigrant hazard rate function and
offspring birth time density function, to compute the exact likelihood of
a RHawkes process using the recursive algorithm proposed by Chen and
Stindl (2018) <doi:10.1080/10618600.2017.1341324>, to compute the
Rosenblatt residuals for goodness-of-fit assessment, and to predict future
event times based on observed event times up to a given time. A function
implementing the linear time RHawkes process likelihood approximation
algorithm proposed in Stindl and Chen (2021)
<doi:10.1007/s11222-021-10002-0> is also included.

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
