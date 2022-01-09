%global __brp_check_rpaths %{nil}
%global packname  mclcar
%global packver   0.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Conditional Auto-Regressive (CAR) Models using Monte Carlo Likelihood Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-rsm 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-spatialreg 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-rsm 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-spatialreg 

%description
The likelihood of direct CAR models and Binomial and Poisson GLM with
latent CAR variables are approximated by the Monte Carlo likelihood. The
Maximum Monte Carlo likelihood estimator is found either by an iterative
procedure of directly maximising the Monte Carlo approximation or by a
response surface design method.Reference for the method can be found in
the DPhil thesis in Z. Sha (2016). For application a good reference is
R.Bivand et.al (2017) <doi:10.1016/j.spasta.2017.01.002>.

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
