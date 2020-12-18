%global packname  SDCNway
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Evaluate Disclosure Risk

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-plyr >= 1.8.5
BuildRequires:    R-CRAN-dplyr >= 0.8.4
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-methods 
Requires:         R-CRAN-MASS >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-plyr >= 1.8.5
Requires:         R-CRAN-dplyr >= 0.8.4
Requires:         R-CRAN-Rdpack 
Requires:         R-methods 

%description
Tools for calculating disclosure risk measures for microdata, including
record-level and file-level measures. The record-level disclosure risk is
estimated primarily using exhaustive tabulation. The file-level disclosure
risk is estimated by fitting loglinear models on the observed sample
counts in cells formed by key variables and their interactions. Funded by
the National Center for Education Statistics. See Skinner and Shlomo
(2008) <doi:10.1198/016214507000001328> for a description of the
file-level risk measures and the loglinear model approach.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
