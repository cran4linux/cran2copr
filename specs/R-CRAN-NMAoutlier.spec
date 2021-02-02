%global packname  NMAoutlier
%global packver   0.1.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.17
Release:          1%{?dist}%{?buildtag}
Summary:          Detecting Outliers in Network Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.47
BuildRequires:    R-stats >= 3.4.3
BuildRequires:    R-parallel >= 3.4.1
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-netmeta >= 0.9.7
Requires:         R-CRAN-MASS >= 7.3.47
Requires:         R-stats >= 3.4.3
Requires:         R-parallel >= 3.4.1
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-netmeta >= 0.9.7

%description
A set of functions providing several outlier (i.e., studies with extreme
findings) and influential detection measures and methodologies in network
meta-analysis: - Simple outlier and influential deletion measures
provided: (a) Raw, (b) Standardized, (c) Studentized residuals; (d)
Mahalanobis distance and (c) leverage. - Outlier and influential detection
measures by considering study deletion (Shift the mean): (a) Raw (b)
Standardized, (c) Studentized deleted residuals; (d) Cook distance; (e)
Ratio of variance-covariance matrix; (f) weight leave one out; (g)
leverage leave one out; (h) heterogeneity leave one out; (i) R
heterogeneity; (k) R Q total; (l) R Q heterogeneity (m); R Q inconsistency
and (n) statistic that indicate the effect that deleting each study has on
the treatment estimates. - Plots for outlier and influential detection
simply and deletion measures (all the above measures) and Q-Q plot for
network meta-analysis. - Forward Search algorithm in network
meta-analysis. - Forward plots for the monitoring statistics in each step
of Forward search algorithm: (a) P-scores; (b) z-values for difference of
direct and indirect evidence with back-calculation method; (c)
Standardized residuals; (d) heterogeneity variance estimator; (e) cook
distance; (f) ratio of variances; (g) Q statistics. - Forward plots for
summary estimates and their confidence intervals in each step of forward
search algorithm.

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
