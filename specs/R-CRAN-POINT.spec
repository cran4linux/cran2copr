%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  POINT
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Protein Structure Guided Local Test

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-CompQuadForm 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-rARPACK 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-CompQuadForm 

%description
Provides an implementation of a rare variant association test that
utilizes protein tertiary structure to increase signal and to identify
likely causal variants. Performs structure-guided collapsing, which leads
to local tests that borrow information from neighboring variants on a
protein and that provide association information on a variant-specific
level. For details of the implemented method see West, R. M., Lu, W.,
Rotroff, D. M., Kuenemann, M., Chang, S-M., Wagner M. J., Buse, J. B.,
Motsinger-Reif, A., Fourches, D., and Tzeng, J-Y. (2019)
<doi:10.1371/journal.pcbi.1006722>.

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
