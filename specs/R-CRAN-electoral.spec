%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  electoral
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Allocating Seats Methods and Party System Scores

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-tibble 

%description
Highest averages & largest remainders allocating seats methods and several
party system scores. Implemented highest averages allocating seats methods
are D'Hondt, Webster, Danish, Imperiali, Hill-Huntington, Dean, Modified
Sainte-Lague, equal proportions and Adams. Implemented largest remainders
allocating seats methods are Hare, Droop, Hangenbach-Bischoff, Imperial,
modified Imperial and quotas & remainders. The main advantage of this
package is that ties are always reported and not incorrectly allocated.
Party system scores provided are competitiveness, concentration, effective
number of parties, party nationalization score, party system
nationalization score and volatility. References: Gallagher (1991)
<doi:10.1016/0261-3794(91)90004-C>. Norris (2004, ISBN:0-521-82977-1).
Laakso & Taagepera (1979) <https://escholarship.org/uc/item/703827nv>.
Jones & Mainwaring (2003)
<https://kellogg.nd.edu/sites/default/files/old_files/documents/304_0.pdf>.
Pedersen (1979) <https://janda.org/c24/Readings/Pedersen/Pedersen.htm>.
Golosov (2010) <doi:10.1177/1354068809339538>. Golosov (2014)
<doi:10.1177/1354068814549342>.

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
