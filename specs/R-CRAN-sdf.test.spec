%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sdf.test
%global packver   0.0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Two Sample Test for Equality of Spectral Densities

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dtt 
BuildRequires:    R-stats 
Requires:         R-CRAN-dtt 
Requires:         R-stats 

%description
Nonparametric method for testing the equality of the spectral densities of
two time series of possibly different lengths. The time series are
preprocessed with the discrete cosine transform and the variance
stabilising transform to obtain an approximate Gaussian regression setting
for the log-spectral density function. The test statistic is based on the
squared L2 norm of the difference between the estimated log-spectral
densities. The test returns the result, the statistic value, and the
p-value. It also provides the estimated empirical quantile and null
distribution under the hypothesis of equal spectral densities. An example
using EEG data is included. For details see Nadin, Krivobokova, Enikeeva
(2026), <doi:10.48550/arXiv.2602.10774>.

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
