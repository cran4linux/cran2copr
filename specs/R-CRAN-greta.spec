%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  greta
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Simple and Scalable Statistical Modelling in R

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-tensorflow >= 2.7.0
BuildRequires:    R-CRAN-glue >= 1.5.1
BuildRequires:    R-CRAN-parallelly >= 1.29.0
BuildRequires:    R-CRAN-future >= 1.22.1
BuildRequires:    R-CRAN-progress >= 1.2.0
BuildRequires:    R-CRAN-reticulate >= 1.19.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-yesno 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-tensorflow >= 2.7.0
Requires:         R-CRAN-glue >= 1.5.1
Requires:         R-CRAN-parallelly >= 1.29.0
Requires:         R-CRAN-future >= 1.22.1
Requires:         R-CRAN-progress >= 1.2.0
Requires:         R-CRAN-reticulate >= 1.19.0
Requires:         R-CRAN-abind 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-yesno 

%description
Write statistical models in R and fit them by MCMC and optimisation on
CPUs and GPUs, using Google 'TensorFlow'.  greta lets you write your own
model like in BUGS, JAGS and Stan, except that you write models right in
R, it scales well to massive datasets, and it’s easy to extend and build
on.  See the website for more information, including tutorials, examples,
package documentation, and the greta forum.

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
