%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GenTwoArmsTrialSize
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Two Arms Clinical Trial Sample Size Calculation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-TrialSize 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-TrialSize 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Hmisc 

%description
Two arms clinical trials required sample size is calculated in the
comprehensive parametric context. The calculation is based on the type of
endpoints(continuous/binary/time-to-event/ordinal), design
(parallel/crossover), hypothesis tests
(equality/noninferiority/superiority/equivalence), trial arms
noncompliance rates and expected loss of follow-up. Methods are described
in: Chow SC, Shao J, Wang H, Lokhnygina Y (2017)
<doi:10.1201/9781315183084>, Wittes, J (2002)
<doi:10.1093/epirev/24.1.39>, Sato, T (2000)
<doi:10.1002/1097-0258(20001015)19:19%%3C2689::aid-sim555%%3E3.0.co;2-0>,
Lachin J M, Foulkes, M A (1986) <doi:10.2307/2531201>, Whitehead J(1993)
<doi:10.1002/sim.4780122404>, Julious SA (2023)
<doi:10.1201/9780429503658>.

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
