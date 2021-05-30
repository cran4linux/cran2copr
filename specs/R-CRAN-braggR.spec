%global packname  braggR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate the Revealed Aggregator of Probability Predictions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Forecasters predicting the chances of a future event may disagree due to
differing evidence or noise. To harness the collective evidence of the
crowd, Ville Satopää (2021) "Regularized Aggregation of One-off
Probability Predictions"
<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3769945> proposes a
Bayesian aggregator that is regularized by analyzing the forecasters'
disagreement and ascribing over-dispersion to noise. This aggregator
requires no user intervention and can be computed efficiently even for a
large numbers of predictions. The author evaluates the aggregator on
subjective probability predictions collected during a four-year
forecasting tournament sponsored by the US intelligence community. The
aggregator improves the accuracy of simple averaging by around 20%% and
other state-of-the-art aggregators by 10-25%%. The advantage stems almost
exclusively from improved calibration. This aggregator -- know as "the
revealed aggregator" -- inputs a) forecasters' probability predictions (p)
of a future binary event and b) the forecasters' common prior (p0) of the
future event. In this R-package, the function sample_aggregator(p,p0,...)
allows the user to calculate the revealed aggregator. Its use is
illustrated with a simple example.

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
