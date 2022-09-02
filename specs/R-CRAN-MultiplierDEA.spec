%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiplierDEA
%global packver   0.1.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.19
Release:          1%{?dist}%{?buildtag}
Summary:          Multiplier Data Envelopment Analysis and Cross Efficiency

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ROI 
BuildRequires:    R-CRAN-ROI.plugin.glpk 
BuildRequires:    R-CRAN-ompr 
BuildRequires:    R-CRAN-ompr.roi 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ROI 
Requires:         R-CRAN-ROI.plugin.glpk 
Requires:         R-CRAN-ompr 
Requires:         R-CRAN-ompr.roi 

%description
Functions are provided for calculating efficiency using multiplier DEA
(Data Envelopment Analysis): Measuring the efficiency of decision making
units (Charnes et al., 1978 <doi:10.1016/0377-2217(78)90138-8>) and cross
efficiency using single and two-phase approach. In addition, it includes
some datasets for calculating efficiency and cross efficiency.

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
