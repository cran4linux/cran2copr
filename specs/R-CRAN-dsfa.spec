%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsfa
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Distributional Stochastic Frontier Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-gratia 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-gratia 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Rdpack 

%description
Framework to fit distributional stochastic frontier models. Casts the
stochastic frontier model into the flexible framework of distributional
regression or otherwise known as General Additive Models of Location,
Scale and Shape (GAMLSS). Allows for linear, non-linear, random and
spatial effects on all the parameters of the distribution of the output,
e.g. effects on the production or cost function, heterogeneity of the
noise and inefficiency. Available distributions are the normal-halfnormal
and normal-exponential distribution. Estimation via the fast and reliable
routines of the 'mgcv' package. For more details see Schmidt R, Kneib T
(2022) <doi:10.48550/arXiv.2208.10294>.

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
