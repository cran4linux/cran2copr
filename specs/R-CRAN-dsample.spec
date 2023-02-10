%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsample
%global packver   0.91.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.91.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Discretization-Based Direct Random Sample Generation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mnormt 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mnormt 

%description
Discretization-based random sampling algorithm that is useful for a
complex model in high dimension is implemented. The normalizing constant
of a target distribution is not needed. Posterior summaries are compared
with those by 'OpenBUGS'. The method is described: Wang and Lee (2014)
<doi:10.1016/j.csda.2013.06.011> and exercised in Lee (2009)
<http://hdl.handle.net/1993/21352>.

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
