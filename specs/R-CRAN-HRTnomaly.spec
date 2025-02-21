%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HRTnomaly
%global packver   25.2.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          25.2.18
Release:          1%{?dist}%{?buildtag}
Summary:          Historical, Relational, and Tail Anomaly-Detection Algorithms

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 

%description
The presence of outliers in a dataset can substantially bias the results
of statistical analyses. To correct for outliers, micro edits are manually
performed on all records. A set of constraints and decision rules is
typically used to aid the editing process. However, straightforward
decision rules might overlook anomalies arising from disruption of linear
relationships. Computationally efficient methods are provided to identify
historical, tail, and relational anomalies at the data-entry level
(Sartore et al., 2024; <doi:10.6339/24-JDS1136>). A score statistic is
developed for each anomaly type, using a distribution-free approach
motivated by the Bienaymé-Chebyshev's inequality, and fuzzy logic is used
to detect cellwise outliers resulting from different types of anomalies.
Each data entry is individually scored and individual scores are combined
into a final score to determine anomalous entries. In contrast to fuzzy
logic, Bayesian bootstrap and a Bayesian test based on empirical
likelihoods are also provided as studied by Sartore et al. (2024;
<doi:10.3390/stats7040073>). These algorithms allow for a more nuanced
approach to outlier detection, as it can identify outliers at data-entry
level which are not obviously distinct from the rest of the data. --- This
research was supported in part by the U.S. Department of Agriculture,
National Agriculture Statistics Service. The findings and conclusions in
this publication are those of the authors and should not be construed to
represent any official USDA, or US Government determination or policy.

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
