%global __brp_check_rpaths %{nil}
%global packname  RFpredInterval
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Prediction Intervals with Random Forests and Boosted Forests

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-hdrcde 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-DiagrammeR 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-hdrcde 
Requires:         R-parallel 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-DiagrammeR 

%description
Implements various prediction interval methods with random forests and
boosted forests. The package has two main functions: pibf() produces
prediction intervals with boosted forests (PIBF) as described in Alakus et
al. (2021) <arXiv:2106.08217> and rfpi() builds 15 distinct variations of
prediction intervals with random forests (RFPI) proposed by Roy and
Larocque (2020) <doi:10.1177/0962280219829885>.

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
