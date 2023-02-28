%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OLCPM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Online Change Point Detection for Matrix-Valued Time Series

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-RSpectra 

%description
We provide two algorithms for monitoring change points with online
matrix-valued time series, under the assumption of a two-way factor
structure. The algorithms are based on different calculations of the
second moment matrices. One is based on stacking the columns of matrix
observations, while another is by a more delicate projected approach. A
well-known fact is that, in the presence of a change point, a factor model
can be rewritten as a model with a larger number of common factors. In
turn, this entails that, in the presence of a change point, the number of
spiked eigenvalues in the second moment matrix of the data increases.
Based on this, we propose two families of procedures - one based on the
fluctuations of partial sums, and one based on extreme value theory - to
monitor whether the first non-spiked eigenvalue diverges after a point in
time in the monitoring horizon, thereby indicating the presence of a
change point. See more details in He et al. (2021)<arXiv:2112.13479>.

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
