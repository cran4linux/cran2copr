%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rankdifferencetest
%global packver   2025.12.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2025.12.4
Release:          1%{?dist}%{?buildtag}
Summary:          Kornbrot's Rank Difference Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-exactRankTests 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-generics 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-exactRankTests 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-generics 

%description
Implements Kornbrot's rank difference test as described in
<doi:10.1111/j.2044-8317.1990.tb00939.x>. This method is a modified
Wilcoxon signed-rank test which produces consistent and meaningful results
for ordinal or monotonically-transformed data.

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
