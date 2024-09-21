%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DemoDecomp
%global packver   1.14.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.14.1
Release:          1%{?dist}%{?buildtag}
Summary:          Decompose Demographic Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-numDeriv 

%description
Three general demographic decomposition methods: Pseudo-continuous
decomposition proposed by Horiuchi, Wilmoth, and Pletcher (2008)
<doi:10.1353/dem.0.0033>, stepwise replacement decomposition proposed by
Andreev, Shkolnikov and Begun (2002) <doi:10.4054/DemRes.2002.7.14>, and
lifetable response experiments proposed by Caswell (1989)
<doi:10.1016/0304-3800(89)90019-7>.

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
