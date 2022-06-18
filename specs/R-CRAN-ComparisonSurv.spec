%global __brp_check_rpaths %{nil}
%global packname  ComparisonSurv
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comparison of Survival Curves Between Two Groups

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-survRM2 
BuildRequires:    R-CRAN-TSHRC 
BuildRequires:    R-CRAN-muhaz 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-survRM2 
Requires:         R-CRAN-TSHRC 
Requires:         R-CRAN-muhaz 

%description
Various statistical methods for survival analysis in comparing survival
curves between two groups, including overall hypothesis tests described in
Li et al. (2015) <doi:10.1371/journal.pone.0116774> and Huang et al.
(2020) <doi:10.1080/03610918.2020.1753075>, fixed-point tests in Klein et
al. (2007) <doi:10.1002/sim.2864>, short-term tests, and long-term tests
in Logan et al. (2008) <doi:10.1111/j.1541-0420.2007.00975.x>. Some
commonly used descriptive statistics and plots are also included.

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
