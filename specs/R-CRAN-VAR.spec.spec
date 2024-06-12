%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VAR.spec
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Allows Specifying a Bivariate VAR (Vector Autoregression) with Desired Spectral Characteristics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
The spectral characteristics of a bivariate series (Marginal Spectra,
Coherency- and Phase-Spectrum) determine whether there is a strong
presence of short-, medium-, or long-term fluctuations (components of
certain frequencies in the spectral representation of the series) in each
one of them.  These are induced by strong peaks of the marginal spectra of
each series at the corresponding frequencies. The spectral characteristics
also determine how strongly these short-, medium-, or long-term
fluctuations of the two series are correlated between the two series.
Information on this is provided by the Coherency spectrum at the
corresponding frequencies. Finally, certain fluctuations of the two series
may be lagged to each other. Information on this is provided by the Phase
spectrum at the corresponding frequencies. The idea in this package is to
define a VAR (Vector autoregression) model with desired spectral
characteristics by specifying a number of polynomials, required to define
the VAR. See Ioannidis(2007) <doi:10.1016/j.jspi.2005.12.013>. These are
specified via their roots, instead of via their coefficients. This is an
idea borrowed from the Time Series Library of R. Dahlhaus, where it is
used for defining ARMA models for univariate time series. This way, one
may e.g. specify a VAR inducing a strong presence of long-term
fluctuations in series 1 and in series 2, which are weakly correlated, but
lagged by a number of time units to each other, while short-term
fluctuations in series 1 and in series 2, are strongly present only in one
of the two series, while they are strongly correlated to each other
between the two series. Simulation from such models allows studying the
behavior of data-analysis tools, such as estimation of the spectra, under
different circumstances, as e.g. peaks in the spectra, generating bias,
induced by leakage.

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
