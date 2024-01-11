%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EVchargcost
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computes and Plot the Optimal Charging Strategy for Electric Vehicles

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 

%description
The purpose of this library is to compute the optimal charging cost
function for a electric vehicle (EV). It is well known that the charging
function of a EV is a concave function that can be approximated by a
piece-wise linear function, so bigger the state of charge, slower the
charging process is. Moreover, the other important function is the one
that gives the electricity price. This function is usually step-wise,
since depending on the time of the day, the price of the electricity is
different. Then, the problem of charging an EV to a certain state of
charge is not trivial. This library implements an algorithm to compute the
optimal charging cost function, that is, it plots for a given state of
charge r (between 0 and 1) the minimum cost we need to pay in order to
charge the EV to that state of charge r. The details of the algorithm are
described in González-Rodríguez et at (2023)
<https://inria.hal.science/hal-04362876v1>.

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
