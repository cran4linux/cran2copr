%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WALS
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted-Average Least Squares Model Averaging

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51.6
BuildRequires:    R-CRAN-Rdpack >= 2.1
BuildRequires:    R-CRAN-Formula >= 1.2.3
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS >= 7.3.51.6
Requires:         R-CRAN-Rdpack >= 2.1
Requires:         R-CRAN-Formula >= 1.2.3
Requires:         R-methods 
Requires:         R-stats 

%description
Implements Weighted-Average Least Squares model averaging for negative
binomial regression models of Huynh (2023) (mimeo), generalized linear
models of De Luca, Magnus, Peracchi (2018)
<doi:10.1016/j.jeconom.2017.12.007> and linear regression models of
Magnus, Powell, Pruefer (2010) <doi:10.1016/j.jeconom.2009.07.004>, see
also Magnus, De Luca (2016) <doi:10.1111/joes.12094>. Weighted-Average
Least Squares for the linear regression model is based on the original
'MATLAB' code by Magnus and De Luca
<https://www.janmagnus.nl/items/WALS.pdf>, see also Kumar, Magnus (2013)
<doi:10.1007/s13571-013-0060-9> and De Luca, Magnus (2011)
<doi:10.1177/1536867X1201100402>.

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
