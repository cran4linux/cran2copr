%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CareDensity
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate the Care Density or Fragmented Care Density Given a Patient-Sharing Network

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 2.0.0
BuildRequires:    R-CRAN-MatrixExtra 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
Requires:         R-CRAN-igraph >= 2.0.0
Requires:         R-CRAN-MatrixExtra 
Requires:         R-CRAN-data.table 
Requires:         R-utils 

%description
Given a patient-sharing network, calculate either the classic care density
as proposed by Pollack et al. (2013) <doi:10.1007/s11606-012-2104-7> or
the fragmented care density as proposed by Engels et al. (2024)
<doi:10.1186/s12874-023-02106-0>. By utilizing the 'igraph' and
'data.table' packages, the provided functions scale well for very large
graphs.

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
