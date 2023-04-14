%global __brp_check_rpaths %{nil}
%global packname  TSEntropies
%global packver   0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9
Release:          3%{?dist}%{?buildtag}
Summary:          Time Series Entropies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0

%description
Computes various entropies of given time series. This is the initial
version that includes ApEn() and SampEn() functions for calculating
approximate entropy and sample entropy. Approximate entropy was proposed
by S.M. Pincus in "Approximate entropy as a measure of system complexity",
Proceedings of the National Academy of Sciences of the United States of
America, 88, 2297-2301 (March 1991). Sample entropy was proposed by J. S.
Richman and J. R. Moorman in "Physiological time-series analysis using
approximate entropy and sample entropy", American Journal of Physiology,
Heart and Circulatory Physiology, 278, 2039-2049 (June 2000). This package
also contains FastApEn() and FastSampEn() functions for calculating fast
approximate entropy and fast sample entropy. These are newly designed very
fast algorithms, resulting from the modification of the original
algorithms. The calculated values of these entropies are not the same as
the original ones, but the entropy trend of the analyzed time series
determines equally reliably. Their main advantage is their speed, which is
up to a thousand times higher. A scientific article describing their
properties has been submitted to The Journal of Supercomputing and in
present time it is waiting for the acceptance.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
