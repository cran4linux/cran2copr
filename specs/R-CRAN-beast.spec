%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  beast
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Estimation of Change-Points in the Slope of Multivariate Time-Series

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-RColorBrewer 

%description
Assume that a temporal process is composed of contiguous segments with
differing slopes and replicated noise-corrupted time series measurements
are observed. The unknown mean of the data generating process is modelled
as a piecewise linear function of time with an unknown number of
change-points. The package infers the joint posterior distribution of the
number and position of change-points as well as the unknown mean
parameters per time-series by MCMC sampling. A-priori, the proposed model
uses an overfitting number of mean parameters but, conditionally on a set
of change-points, only a subset of them influences the likelihood. An
exponentially decreasing prior distribution on the number of change-points
gives rise to a posterior distribution concentrating on sparse
representations of the underlying sequence, but also available is the
Poisson distribution. See Papastamoulis et al (2019)
<doi:10.1515/ijb-2018-0052> for a detailed presentation of the method.

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
