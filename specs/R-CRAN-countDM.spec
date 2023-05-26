%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  countDM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Count Data Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lamW 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-miscTools 
Requires:         R-CRAN-lamW 
Requires:         R-stats 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-miscTools 

%description
The maximum likelihood estimation (MLE) of the count data models along
with standard error of the estimates and Akaike information model section
criterion are provided. The functions allow to compute the MLE for the
following distributions such as the Bell distribution, the Borel
distribution, the Poisson distribution, zero inflated Bell distribution,
zero inflated Bell Touchard distribution, zero inflated Poisson
distribution, zero one inflated Bell distribution and zero one inflated
Poisson distribution. Moreover, the probability mass function (PMF),
distribution function (CDF), quantile function (QF) and random numbers
generation of the Bell Touchard and zero inflated Bell Touchard
distribution are also provided.

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
