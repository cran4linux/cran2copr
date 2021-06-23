%global __brp_check_rpaths %{nil}
%global packname  waveband
%global packver   4.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computes Credible Intervals for Bayesian Wavelet Shrinkage

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildRequires:    R-CRAN-wavethresh >= 4.6
Requires:         R-CRAN-wavethresh >= 4.6

%description
Computes Bayesian wavelet shrinkage credible intervals for nonparametric
regression. The method uses cumulants to derive Bayesian credible
intervals for wavelet regression estimates. The first four cumulants of
the posterior distribution of the estimates are expressed in terms of the
observed data and integer powers of the mother wavelet functions. These
powers are closely approximated by linear combinations of wavelet scaling
functions at an appropriate finer scale. Hence, a suitable modification of
the discrete wavelet transform allows the posterior cumulants to be found
efficiently for any data set. Johnson transformations then yield the
credible intervals themselves. Barber, S., Nason, G.P. and Silverman, B.W.
(2002) <doi:10.1111/1467-9868.00332>.

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
