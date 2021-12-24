%global __brp_check_rpaths %{nil}
%global packname  lrstat
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Power and Sample Size Calculation for Non-Proportional Hazards

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-Rcpp >= 1.0.7

%description
Performs power and sample size calculation for non-proportional hazards
model using the Fleming-Harrington family of weighted log-rank tests. The
sequentially calculated log-rank test score statistics are assumed to have
independent increments as characterized in Anastasios A. Tsiatis (1982)
<doi:10.1080/01621459.1982.10477898>. The mean and variance of log-rank
test score statistics are calculated based on Edward Lakatos (1986)
<doi:10.1016/0197-2456(86)90047-4> and Kaifeng Lu (2021)
<doi:10.1002/pst.2069>. The boundary crossing probabilities are calculated
using the recursive integration algorithm described in Christopher
Jennison and Bruce W. Turnbull (2000, ISBN:0849303168). The inverse normal
combination method due to Lu Cui, H. M. James Hung, and Sue-Jane Wang
(1999) <doi:10.1111/j.0006-341x.1999.00853.x> is used in the simulation
study to accommodate the information time not proportional to the total
number of events for weighted log-rank tests.

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
