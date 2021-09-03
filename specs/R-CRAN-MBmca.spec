%global __brp_check_rpaths %{nil}
%global packname  MBmca
%global packver   1.0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Nucleic Acid Melting Curve Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-robustbase >= 0.9
BuildRequires:    R-CRAN-chipPCR >= 0.0.7
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-robustbase >= 0.9
Requires:         R-CRAN-chipPCR >= 0.0.7
Requires:         R-stats 
Requires:         R-utils 

%description
Lightweight utilities for nucleic acid melting curve analysis are
important in life sciences and diagnostics. This software can be used for
the analysis and presentation of melting curve data from microbead-based
assays (surface melting curve analysis) and reactions in solution (e.g.,
quantitative PCR (qPCR), real-time isothermal Amplification). Further
information are described in detail in two publications in The R Journal [
<https://journal.r-project.org/archive/2013-2/roediger-bohm-schimke.pdf>;
<https://journal.r-project.org/archive/2015-1/RJ-2015-1.pdf>].

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
