%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpeTestNP
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Parametric Tests of Parametric Specifications

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-stats 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Performs non-parametric tests of parametric specifications. Five tests are
available. Specific bandwidth and kernel methods can be chosen along with
many other options. Allows parallel computing to quickly compute p-values
based on the bootstrap. Methods implemented in the package are H.J.
Bierens (1982) <doi:10.1016/0304-4076(82)90105-1>, J.C. Escanciano (2006)
<doi:10.1017/S0266466606060506>, P.L. Gozalo (1997)
<doi:10.1016/S0304-4076(97)86571-2>, P. Lavergne and V. Patilea (2008)
<doi:10.1016/j.jeconom.2007.08.014>, P. Lavergne and V. Patilea (2012)
<doi:10.1198/jbes.2011.07152>, J.H. Stock and M.W. Watson (2006)
<doi:10.1111/j.1538-4616.2007.00014.x>, C.F.J. Wu (1986)
<doi:10.1214/aos/1176350142>, J. Yin, Z. Geng, R. Li, H. Wang (2010)
<https://www.jstor.org/stable/24309002> and J.X. Zheng (1996)
<doi:10.1016/0304-4076(95)01760-7>.

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
