%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TestNet
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Method for Inferring Microbial Networks with FDR Control

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-dcov 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-dcov 
Requires:         R-stats 
Requires:         R-utils 

%description
A testing method for inferring microbial networks. It differs from
existing microbial network analyses in that it provides calibrated results
by controlling the false discovery rate. The method accounts for the
complex features of taxa count data. It also accommodates both independent
and clustered samples, offers separate linear and nonlinear tests for each
pair of taxa, and includes an omnibus test that bypasses the need to
specify the type of relationship for each pair of taxa.

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
