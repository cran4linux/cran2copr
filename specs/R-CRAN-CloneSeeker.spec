%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CloneSeeker
%global packver   1.0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.13
Release:          1%{?dist}%{?buildtag}
Summary:          Seeking and Finding Clones in Copy Number and Sequencing Data

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-mc2d 
BuildRequires:    R-CRAN-quantmod 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-mc2d 
Requires:         R-CRAN-quantmod 

%description
Defines the classes and functions used to simulate and to analyze data
sets describing copy number variants and, optionally, sequencing mutations
in order to detect clonal subsets. See Zucker et al. (2019)
<doi:10.1093/bioinformatics/btz057>.

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
