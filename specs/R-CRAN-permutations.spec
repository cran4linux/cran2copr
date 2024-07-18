%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  permutations
%global packver   1.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          The Symmetric Group: Permutations of a Finite Set

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-partitions >= 1.9.17
BuildRequires:    R-CRAN-freealg >= 1.0.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-numbers 
Requires:         R-CRAN-partitions >= 1.9.17
Requires:         R-CRAN-freealg >= 1.0.4
Requires:         R-methods 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-numbers 

%description
Manipulates invertible functions from a finite set to itself.  Can
transform from word form to cycle form and back.  To cite the package in
publications please use Hankin (2020) "Introducing the permutations R
package", SoftwareX, volume 11 <doi:10.1016/j.softx.2020.100453>.

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
