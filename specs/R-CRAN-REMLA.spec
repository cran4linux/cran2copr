%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  REMLA
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Expectation-Maximization Estimation for Latent Variable Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-geex 
BuildRequires:    R-stats 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-geex 
Requires:         R-stats 

%description
Traditional latent variable models assume that the population is
homogeneous, meaning that all individuals in the population are assumed to
have the same latent structure. However, this assumption is often violated
in practice given that individuals may differ in their age, gender,
socioeconomic status, and other factors that can affect their latent
structure. The robust expectation maximization (REM) algorithm is a
statistical method for estimating the parameters of a latent variable
model in the presence of population heterogeneity as recommended by Nieser
& Cochran (2023) <doi:10.1037/met0000413>. The REM algorithm is based on
the expectation-maximization (EM) algorithm, but it allows for the case
when all the data are generated by the assumed data generating model.

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
