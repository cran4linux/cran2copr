%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SixSigma
%global packver   0.11.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.0
Release:          1%{?dist}%{?buildtag}
Summary:          Six Sigma Tools for Quality Control and Improvement

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-xtable 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-xtable 

%description
Functions and utilities to perform Statistical Analyses in the Six Sigma
way. Through the DMAIC cycle (Define, Measure, Analyze, Improve, Control),
you can manage several Quality Management studies: Gage R&R, Capability
Analysis, Control Charts, Loss Function Analysis, etc. Data frames used in
the books "Six Sigma with R" [ISBN 978-1-4614-3652-2] and "Quality Control
with R" [ISBN 978-3-319-24046-6], are also included in the package.

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
