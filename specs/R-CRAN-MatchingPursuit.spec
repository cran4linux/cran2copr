%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MatchingPursuit
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Processing Time Series Data Using the Matching Pursuit Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-edf 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-edf 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-raster 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-digest 

%description
Provides tools for analysing and decomposing time series data using the
Matching Pursuit (MP) algorithm, a greedy signal decomposition technique
that represents complex signals as a linear combination of simpler
functions (called atoms) selected from a redundant dictionary. For more
details see Mallat and Zhang (1993) <doi:10.1109/78.258082>, Pati et al.
(1993) <doi:10.1109/ACSSC.1993.342465>, Elad (2010)
<doi:10.1007/978-1-4419-7011-4> and Różański (2024) <doi:10.1145/3674832>.

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
