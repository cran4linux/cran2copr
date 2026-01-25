%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GMMinit
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Initial Value for Gaussian Mixture Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mvnfast 
Requires:         R-stats 

%description
Generating, evaluating, and selecting initialization strategies for
Gaussian Mixture Models (GMMs), along with functions to run the
Expectation-Maximization (EM) algorithm. Initialization methods are
compared using log-likelihood, and the best-fitting model can be selected
using BIC. Methods build on initialization strategies for finite mixture
models described in Michael and Melnykov (2016)
<doi:10.1007/s11634-016-0264-8> and Biernacki et al. (2003)
<doi:10.1016/S0167-9473(02)00163-9>, and on the EM algorithm of Dempster
et al. (1977) <doi:10.1111/j.2517-6161.1977.tb01600.x>. Background on
model-based clustering includes Fraley and Raftery (2002)
<doi:10.1198/016214502760047131> and McLachlan and Peel (2000,
ISBN:9780471006268).

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
