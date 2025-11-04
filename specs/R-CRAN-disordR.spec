%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  disordR
%global packver   0.9-8-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8.5
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Ordered Vectors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix >= 1.3.3
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix >= 1.3.3
Requires:         R-CRAN-digest 
Requires:         R-methods 

%description
Functionality for manipulating values of associative maps.  The package is
a dependency for mvp-type packages that use the STL map class: it traps
plausible idiom that is ill-defined (implementation-specific) and returns
an informative error, rather than returning a possibly incorrect result.
To cite the package in publications please use Hankin (2022)
<doi:10.48550/ARXIV.2210.03856>.

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
