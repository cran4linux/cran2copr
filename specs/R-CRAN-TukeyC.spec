%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TukeyC
%global packver   1.3-43
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.43
Release:          1%{?dist}%{?buildtag}
Summary:          Conventional Tukey Test

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-xtable 

%description
Provides tools to perform multiple comparison analyses, based on the
well-known Tukey's "Honestly Significant Difference" (HSD) test. In models
involving interactions, 'TukeyC' stands out from other R packages by
implementing intuitive and easy-to-use functions. In addition to
accommodating traditional R methods such as lm() and aov(), it has also
been extended to objects of the lmer() class, that is, mixed models with
fixed effects. For more details see Tukey (1949) <doi:10.2307/3001913>.

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
