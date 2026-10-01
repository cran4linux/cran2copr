%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RESIDE
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rapid Easy Synthesis to Inform Data Extraction

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-bestNormalize 
BuildRequires:    R-CRAN-RDP 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-simstudy 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-bestNormalize 
Requires:         R-CRAN-RDP 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-simstudy 

%description
Assists researchers with planning analysis prior to obtaining data from
Trusted Research Environments (TREs), also known as safe havens. Marginal
distributions of one or more related data frames can be exported from a
TRE and imported elsewhere, where data can be synthesised from them, with
or without user specified correlations, by sampling from a multivariate
cumulative distribution (copula). The International Stroke Trial (IST) is
included as an example dataset under the ODC-By licence, Sandercock et al.
(2011) <doi:10.7488/ds/104>, Sandercock et al. (2011)
<doi:10.1186/1745-6215-12-101>.

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
