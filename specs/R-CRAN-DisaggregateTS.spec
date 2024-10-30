%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DisaggregateTS
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Temporal Disaggregation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-withr 

%description
Provides tools for temporal disaggregation, including: (1)
High-dimensional and low-dimensional series generation for simulation
studies; (2) A toolkit for temporal disaggregation and benchmarking using
low-dimensional indicator series as proposed by Dagum and Cholette (2006,
ISBN:978-0-387-35439-2); (3) Novel techniques by Mosley, Gibberd, and
Eckley (2022, <doi:10.1111/rssa.12952>) for disaggregating low-frequency
series in the presence of high-dimensional indicator matrices.

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
