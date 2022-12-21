%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weyl
%global packver   0.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          The Weyl Algebra

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-freealg >= 1.0.4
BuildRequires:    R-CRAN-spray >= 1.0.19
BuildRequires:    R-CRAN-disordR >= 0.0.8
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mathjaxr 
Requires:         R-CRAN-freealg >= 1.0.4
Requires:         R-CRAN-spray >= 1.0.19
Requires:         R-CRAN-disordR >= 0.0.8
Requires:         R-methods 
Requires:         R-CRAN-mathjaxr 

%description
A suite of routines for Weyl algebras.  Notation follows Coutinho (1995,
ISBN 0-521-55119-6, "A Primer of Algebraic D-Modules").  Uses 'disordR'
discipline (Hankin 2022 <doi:10.48550/ARXIV.2210.03856>).  To cite the
package in publications, use Hankin 2022 <doi:10.48550/ARXIV.2212.09230>.

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
