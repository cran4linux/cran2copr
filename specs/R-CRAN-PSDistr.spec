%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PSDistr
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Distributions Derived from Normal Distribution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-pracma 

%description
Presentation of distributions such as: two-piece power normal (TPPN),
plasticizing component (PC), DS normal (DSN), expnormal (EN), Sulewski
plasticizing component (SPC), easily changeable kurtosis (ECK)
distributions. Density, distribution function, quantile function and
random generation are presented. For details on this method see: Sulewski
(2019) <doi:10.1080/03610926.2019.1674871>, Sulewski (2021)
<doi:10.1080/03610926.2020.1837881>, Sulewski (2021)
<doi:10.1134/S1995080221120337>, Sulewski (2022) <"New members of the
Johnson family of probability dis-tributions: properties and
application">, Sulewski, Volodin (2022) <doi:10.1134/S1995080222110270>,
Sulewski (2023) <doi:10.17713/ajs.v52i3.1434>.

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
