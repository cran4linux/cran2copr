%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ffmanova
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fifty-Fifty MANOVA

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
General linear modeling with multiple responses (MANCOVA). An overall
p-value for each model term is calculated by the 50-50 MANOVA method by
Langsrud (2002) <doi:10.1111/1467-9884.00320>, which handles collinear
responses. Rotation testing, described by Langsrud (2005)
<doi:10.1007/s11222-005-4789-5>, is used to compute adjusted single
response p-values according to familywise error rates and false discovery
rates (FDR). The approach to FDR is described in the appendix of Moen et
al. (2005) <doi:10.1128/AEM.71.4.2086-2094.2005>. Unbalanced designs are
handled by Type II sums of squares as argued in Langsrud (2003)
<doi:10.1023/A:1023260610025>. Furthermore, the Type II philosophy is
extended to continuous design variables as described in Langsrud et al.
(2007) <doi:10.1080/02664760701594246>. This means that the method is
invariant to scale changes and that common pitfalls are avoided.

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
