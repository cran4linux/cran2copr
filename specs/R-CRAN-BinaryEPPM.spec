%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BinaryEPPM
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mean and Scale-Factor Modeling of Under- And Over-Dispersed Binary Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-lmtest 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Under- and over-dispersed binary data are modeled using an extended
Poisson process model (EPPM) appropriate for binary data. A feature of the
model is that the under-dispersion relative to the binomial distribution
only needs to be greater than zero, but the over-dispersion is restricted
compared to other distributional models such as the beta and correlated
binomials. Because of this, the examples focus on under-dispersed data and
how, in combination with the beta or correlated distributions, flexible
models can be fitted to data displaying both under- and over-dispersion.
Using Generalized Linear Model (GLM) terminology, the functions utilize
linear predictors for the probability of success and scale-factor with
various link functions for p, and log link for scale-factor, to fit a
variety of models relevant to areas such as bioassay. Details of the EPPM
are in Faddy and Smith (2012) <doi:10.1002/bimj.201100214> and Smith and
Faddy (2019) <doi:10.18637/jss.v090.i08>.

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
