%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  etsi
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Testing Using Surrogate Information

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-hetsurr 
BuildRequires:    R-stats 
Requires:         R-CRAN-hetsurr 
Requires:         R-stats 

%description
Provides functions for treatment effect estimation, hypothesis testing,
and future study design for settings where the surrogate is used in place
of the primary outcome for individuals for whom the surrogate is valid,
and the primary outcome is purposefully measured in the remaining
patients. More details are available in: Knowlton, R., Parast, L. (2024)
``Efficient Testing Using Surrogate Information," Biometrical Journal,
67(6): e70086, <doi:10.1002/bimj.70086>. A tutorial for this package can
be found at <https://www.laylaparast.com/etsi>.

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
