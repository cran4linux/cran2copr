%global __brp_check_rpaths %{nil}
%global packname  ebreg
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Implementation of the Empirical Bayes Method

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-lars 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 

%description
Implements a Bayesian-like approach to the high-dimensional sparse linear
regression problem based on an empirical or data-dependent prior
distribution, which can be used for estimation/inference on the model
parameters, variable selection, and prediction of a future response. The
method was first presented in Martin, Ryan and Mess, Raymond and Walker,
Stephen G (2017) <doi:10.3150/15-BEJ797>. More details focused on the
prediction problem are given in Martin, Ryan and Tang, Yiqi (2019)
<arXiv:1903.00961>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
