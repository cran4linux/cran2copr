%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HDMFA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Matrix Factor Analysis

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-RSpectra 

%description
Hign-dimensional matrix factor models have drawn much attention in view of
the fact that observations are usually well structured to be an array such
as in macroeconomics and finance. In addition, data often exhibit
heavy-tails and thus it is also important to develop robust procedures. We
aim to address this issue by replacing the least square loss with Huber
loss function. We propose two algorithms to do robust factor analysis by
considering the Huber loss. One is based on minimizing the Huber loss of
the idiosyncratic error's Frobenius norm, which leads to a weighted
iterative projection approach to compute and learn the parameters and
thereby named as Robust-Matrix-Factor-Analysis (RMFA), see the details in
He et al. (2023)<doi:10.1080/07350015.2023.2191676>. The other one is
based on minimizing the element-wise Huber loss, which can be solved by an
iterative Huber regression algorithm (IHR). In this package, we also
provide the algorithm for alpha-PCA by Chen & Fan (2021)
<doi:10.1080/01621459.2021.1970569>, the Projected estimation (PE) method
by Yu et al. (2022)<doi:10.1016/j.jeconom.2021.04.001>. In addition, the
methods for determining the pair of factor numbers are also given.

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
