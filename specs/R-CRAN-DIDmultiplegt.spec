%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DIDmultiplegt
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation in DID with Multiple Groups and Periods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-fixest >= 0.6.0
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-wooldridge 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-fixest >= 0.6.0
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sampling 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-wooldridge 

%description
Estimate the effect of a treatment on an outcome in sharp
Difference-in-Difference designs with multiple groups and periods. It
computes the DIDM estimator introduced in Section 4 of "Two-Way Fixed
Effects Estimators with Heterogeneous Treatment Effects" (Chaisemartin,
D'Haultfoeuille (2020) <doi:10.1257/aer.20181169>), which generalizes the
standard DID estimator with two groups, two periods and a binary treatment
to situations with many groups,many periods and a potentially non-binary
treatment. For each pair of consecutive time periods t-1 and t and for
each value of the treatment d, the package computes a DID estimator
comparing the outcome evolution among the switchers, the groups whose
treatment changes from d to some other value between t-1 and t, to the
same evolution among control groups whose treatment is equal to d both in
t-1 and t. Then the DIDM estimator is equal to the average of those DIDs
across all pairs of consecutive time periods and across all values of the
treatment. Under a parallel trends assumption, DIDM is an unbiased and
consistent estimator of the average treatment effect among switchers, at
the time period when they switch. The package can also compute placebo
estimators that can be used to test the parallel trends assumption.
Finally, in staggered adoption designs where each group's treatment is
weakly increasing over time, it can compute estimators of switchers'
dynamic treatment effects, one time period or more after they have started
receiving the treatment.

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
