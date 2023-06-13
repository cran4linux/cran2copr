%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  posologyr
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Individual Dose Optimization using Population Pharmacokinetics

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rxode2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-rxode2 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-data.table 

%description
Determine individual pharmacokinetic (and pharmacokinetic-pharmacodynamic)
profiles and use them to personalise drug regimens. You provide the data
and a population pharmacokinetic model, 'posologyr' provides the
individual a posteriori estimate and allows you to determine the optimal
dosing. The empirical Bayes estimates are computed as described in Kang et
al. (2012) <doi:10.4196/kjpp.2012.16.2.97>.

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
