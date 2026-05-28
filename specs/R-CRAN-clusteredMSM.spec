%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clusteredMSM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Analysis of Clustered Multistate Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-utils 

%description
Nonparametric estimation of population-averaged transition probabilities,
with cluster-bootstrap pointwise confidence intervals, simultaneous
confidence bands, and two-sample Kolmogorov-Smirnov-type tests for
clustered or independent multistate process data. Estimation follows
Bakoyannis (2021) <doi:10.1111/biom.13327>; two-sample inference for the
cluster-randomized and independent-samples designs follows Bakoyannis and
Bandyopadhyay (2022) <doi:10.1007/s10463-021-00819-x>. Both methods use
the working-independence Aalen-Johansen estimator. The package supports
both progressive (acyclic) and non-monotone (e.g., illness-death with
recovery) multistate processes, right censoring, left truncation, and
informative cluster size. The user supplies data in interval format (one
row per mutually-exclusive time interval per subject) and interacts with
the package through a single formula-based function, patp().

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
