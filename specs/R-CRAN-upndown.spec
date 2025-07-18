%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  upndown
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities and Design Aids for Up-and-Down Dose-Finding Studies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cir 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-cir 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-plyr 

%description
Up-and-Down (UD) is the most popular design approach for dose-finding, but
it has been severely under-served by the statistical and computing
communities. This is the first package that comprehensively addresses UD's
needs. Recent applied UD tutorial: Oron et al., 2022
<doi:10.1097/ALN.0000000000004282>. Recent methodological overview: Oron
and Flournoy, 2024 <doi:10.51387/24-NEJSDS74>.

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
