%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MKinfer
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Inferential Statistics

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MKdescr 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-arrangements 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-exactRankTests 
BuildRequires:    R-CRAN-miceadds 
Requires:         R-stats 
Requires:         R-CRAN-MKdescr 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-arrangements 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-exactRankTests 
Requires:         R-CRAN-miceadds 

%description
Computation of various confidence intervals (Altman et al. (2000),
ISBN:978-0-727-91375-3; Hedderich and Sachs (2018),
ISBN:978-3-662-56657-2) including bootstrapped versions (Davison and
Hinkley (1997), ISBN:978-0-511-80284-3) as well as Hsu (Hedderich and
Sachs (2018), ISBN:978-3-662-56657-2), permutation (Janssen (1997),
<doi:10.1016/S0167-7152(97)00043-6>), bootstrap (Davison and Hinkley
(1997), ISBN:978-0-511-80284-3), intersection-union (Sozu et al. (2015),
ISBN:978-3-319-22005-5) and multiple imputation (Barnard and Rubin (1999),
<doi:10.1093/biomet/86.4.948>) t-test; furthermore, computation of
intersection-union z-test as well as multiple imputation Wilcoxon tests.
Graphical visualization by volcano and Bland-Altman plots (Bland and
Altman (1986), <doi:10.1016/S0140-6736(86)90837-8>; Shieh (2018),
<doi:10.1186/s12874-018-0505-y>).

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
