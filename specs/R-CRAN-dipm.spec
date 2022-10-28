%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dipm
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Depth Importance in Precision Medicine (DIPM) Method

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-partykit >= 1.2.6
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
Requires:         R-CRAN-partykit >= 1.2.6
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 

%description
An implementation by Chen, Li, and Zhang (2022) <doi:
10.1093/bioadv/vbac041> of the Depth Importance in Precision Medicine
(DIPM) method in Chen and Zhang (2022) <doi:10.1093/biostatistics/kxaa021>
and Chen and Zhang (2020) <doi:10.1007/978-3-030-46161-4_16>. The DIPM
method is a classification tree that searches for subgroups with
especially poor or strong performance in a given treatment group.

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
