%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RIbench
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Benchmark Suite for Indirect Methods for RI Estimation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-optparse 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-sfsmisc 
Requires:         R-stats 
Requires:         R-CRAN-optparse 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-msm 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-sfsmisc 

%description
The provided benchmark suite enables the automated evaluation and
comparison of any existing and novel indirect method for reference
interval ('RI') estimation in a systematic way. Indirect methods take
routine measurements of diagnostic tests, containing pathological and
non-pathological samples as input and use sophisticated statistical
methods to derive a model describing the distribution of the
non-pathological samples, which can then be used to derive reference
intervals. The benchmark suite contains 5,760 simulated test sets with
varying difficulty. To include any indirect method, a custom wrapper
function needs to be provided. The package offers functions for generating
the test sets, executing the indirect method and evaluating the results.
See ?RIbench or vignette("RIbench_package") for a more comprehensive
description of the features. A detailed description and application is
described in Ammer T., Schuetzenmeister A., Prokosch H.-U., Zierk J., Rank
C.M., Rauh M. "RIbench: A Proposed Benchmark for the Standardized
Evaluation of Indirect Methods for Reference Interval Estimation".
Clinical Chemistry (2022) <doi:10.1093/clinchem/hvac142>.

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
