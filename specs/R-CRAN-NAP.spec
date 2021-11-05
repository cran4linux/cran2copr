%global __brp_check_rpaths %{nil}
%global packname  NAP
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Local Alternative Priors in Psychology

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-graphics 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-graphics 

%description
Conducts Bayesian Hypothesis tests of a point null hypothesis against a
two-sided alternative using Non-local Alternative Prior (NAP) for one- and
two-sample z- and t-tests (Johnson, V. and Rossell, R. (2010)
<doi:10.1111/j.1467-9868.2009.00730.x>). Under the alternative, the NAP is
assumed on the standardized effects size in one-sample tests and on their
differences in two-sample tests. The package considers two types of NAP
densities: (1) the normal moment prior, and (2) the composite alternative.
In fixed design tests, the functions calculate the Bayes factors and the
expected weight of evidence for varied effect size and sample size. The
package also provides a sequential testing framework using the Sequential
Bayes Factor (SBF) design. The functions calculate the operating
characteristics (OC) and the average sample number (ASN), and also
conducts sequential tests for a sequentially observed data.

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
