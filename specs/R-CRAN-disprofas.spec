%global __brp_check_rpaths %{nil}
%global packname  disprofas
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Parametric Dissolution Profile Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-ggplot2 

%description
Similarity of dissolution profiles is assessed using the similarity factor
f2 according to the EMA guideline (European Medicines Agency 2010) "On the
investigation of bioequivalence". Dissolution profiles are regarded as
similar if the f2 value is between 50 and 100. For the applicability of
the similarity factor f2, the variability between profiles needs to be
within certain limits. Often, this constraint is violated. One possibility
in this situation is to resample the measured profiles in order to obtain
a bootstrap estimate of f2 (Shah et al. (1998)
<doi:10.1023/A:1011976615750>). Other alternatives are the
model-independent non-parametric multivariate confidence region (MCR)
procedure (Tsong et al. (1996) <doi:10.1177/009286159603000427>) or the
T2-test for equivalence procedure (Hoffelder (2016)
<https://www.ecv.de/suse_item.php?suseId=Z|pi|8430>). Functions for
estimation of f1, f2, bootstrap f2, MCR / T2-test for equivalence
procedure are implemented.

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
