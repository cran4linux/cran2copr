%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cmprsk
%global packver   2.2-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.12
Release:          1%{?dist}%{?buildtag}
Summary:          Subdistribution Analysis of Competing Risks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-survival 

%description
Estimation, testing and regression modeling of subdistribution functions
in competing risks, as described in Gray (1988), A class of K-sample tests
for comparing the cumulative incidence of a competing risk, Ann. Stat.
16:1141-1154 <DOI:10.1214/aos/1176350951>, and Fine JP and Gray RJ (1999),
A proportional hazards model for the subdistribution of a competing risk,
JASA, 94:496-509, <DOI:10.1080/01621459.1999.10474144>.

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
