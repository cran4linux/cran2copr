%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fragility
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Assessing and Visualizing Fragility of Clinical Results

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 8.0.1
BuildRequires:    R-CRAN-survival >= 3.8.3
BuildRequires:    R-CRAN-plotrix >= 3.7.5
BuildRequires:    R-graphics >= 3.5.0
BuildRequires:    R-grDevices >= 3.5.0
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-metafor >= 2.0.0
BuildRequires:    R-CRAN-netmeta >= 1.0.0
Requires:         R-CRAN-meta >= 8.0.1
Requires:         R-CRAN-survival >= 3.8.3
Requires:         R-CRAN-plotrix >= 3.7.5
Requires:         R-graphics >= 3.5.0
Requires:         R-grDevices >= 3.5.0
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-metafor >= 2.0.0
Requires:         R-CRAN-netmeta >= 1.0.0

%description
A collection of user-friendly functions for assessing fragility of
clinical results with binary and survival outcomes. For binary outcomes,
the package assesses and visualizes fragility of individual studies (Walsh
et al., 2014 <doi:10.1016/j.jclinepi.2013.10.019>; Lin, 2021
<doi:10.1111/jep.13428>), conventional pairwise meta-analyses (Atal et
al., 2019 <doi:10.1016/j.jclinepi.2019.03.012>), and network meta-analyses
of multiple treatments with binary outcomes (Xing et al., 2020
<doi:10.1016/j.jclinepi.2020.07.003>). The functions for binary outcomes
are designed to: 1) calculate the fragility index (i.e., the minimal event
status modifications that can alter the significance or non-significance
of the original result) and fragility quotient (i.e., fragility index
divided by sample size) at a specific significance level; 2) give the
cases of event status modifications for altering the result's significance
or non-significance and visualize these cases; 3) visualize the trend of
statistical significance as event status is modified; 4) efficiently
derive fragility indexes and fragility quotients at multiple significance
levels, and visualize the relationship between these fragility measures
against the significance levels; and 5) calculate fragility indexes and
fragility quotients of multiple datasets (e.g., a collection of clinical
trials or meta-analyses) and produce plots of their overall distributions.
For survival outcomes, the package implements the event status
modification method based on the log-rank test described by Xing et al.
(2026 <doi:10.1093/aje/kwaf229>). It calculates the fragility index and
fragility quotient for two-group studies with right-censored data,
modifying event status in one or both groups while preserving follow-up
times and group assignments. Results include the sequence of
modifications, corresponding p-values, and an S3 print method. The outputs
from these functions may inform the robustness of clinical results in
terms of statistical significance and aid the interpretation of fragility
measures. The usage of this package is illustrated in Lin et al. (2023
<doi:10.1016/j.ajog.2022.08.053>) and detailed in Lin and Chu (2022
<doi:10.1371/journal.pone.0268754>).

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
