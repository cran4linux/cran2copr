%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Certara.NLME8
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Certara's Nonlinear Mixed-Effects Modeling Engine

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-batchtools >= 0.9.9
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-batchtools >= 0.9.9
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-reshape 
Requires:         R-utils 
Requires:         R-CRAN-data.table 

%description
Perform Nonlinear Mixed-Effects (NLME) Modeling using Certara's
NLME-Engine. Access the same Maximum Likelihood engines used in the
Phoenix platform, including algorithms for parametric methods, individual,
and pooled data analysis
<https://www.certara.com/app/uploads/2020/06/BR_PhoenixNLME-v4.pdf>. The
Quasi-Random Parametric Expectation-Maximization Method (QRPEM) is also
supported <https://www.page-meeting.org/default.asp?abstract=2338>.
Execution is supported both locally or on remote machines. Remote
execution includes support for Linux Sun Grid Engine (SGE), Terascale
Open-source Resource and Queue Manager (TORQUE) grids, Linux and Windows
multicore, and individual runs.

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
