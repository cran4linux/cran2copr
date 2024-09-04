%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RWNN
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Random Weight Neural Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.4.6
Requires:         R-methods 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-randtoolbox 
Requires:         R-stats 
Requires:         R-utils 

%description
Creation, estimation, and prediction of random weight neural networks
(RWNN), Schmidt et al. (1992) <doi:10.1109/ICPR.1992.201708>, including
popular variants like extreme learning machines, Huang et al. (2006)
<doi:10.1016/j.neucom.2005.12.126>, sparse RWNN, Zhang et al. (2019)
<doi:10.1016/j.neunet.2019.01.007>, and deep RWNN, Henríquez et al. (2018)
<doi:10.1109/IJCNN.2018.8489703>. It further allows for the creation of
ensemble RWNNs like bagging RWNN, Sui et al. (2021)
<doi:10.1109/ECCE47101.2021.9595113>, boosting RWNN, stacking RWNN, and
ensemble deep RWNN, Shi et al. (2021) <doi:10.1016/j.patcog.2021.107978>.

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
