%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iMRMC
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Reader, Multi-Case Analysis Methods (ROC, Agreement, and Other Metrics)

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       R-java
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-utils 

%description
This software does Multi-Reader, Multi-Case (MRMC) analyses of data from
imaging studies where clinicians (readers) evaluate patient images
(cases). What does this mean? ... Many imaging studies are designed so
that every reader reads every case in all modalities, a fully-crossed
study. In this case, the data is cross-correlated, and we consider the
readers and cases to be cross-correlated random effects. An MRMC analysis
accounts for the variability and correlations from the readers and cases
when estimating variances, confidence intervals, and p-values. The
functions in this package can treat arbitrary study designs and studies
with missing data, not just fully-crossed study designs. An overview of
this software, including references presenting details on the methods, can
be found here:
<https://www.fda.gov/medical-devices/science-and-research-medical-devices/imrmc-software-do-multi-reader-multi-case-statistical-analysis-reader-studies>.

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
