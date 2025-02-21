%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RobPC
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Panel Clustering Algorithm

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-trimcluster 
Requires:         R-stats 
Requires:         R-CRAN-trimcluster 

%description
Performs both classical and robust panel clustering by applying Principal
Component Analysis (PCA) for dimensionality reduction and clustering via
standard K-Means or Trimmed K-Means. The method is designed to ensure
stable and reliable clustering, even in the presence of outliers. Suitable
for analyzing panel data in domains such as economic research, financial
time-series, healthcare analytics, and social sciences. The package allows
users to choose between classical K-Means for standard clustering and
Trimmed K-Means for robust clustering, making it a flexible tool for
various applications. For this package, we have benefited from the studies
Rencher (2003), Wang and Lu (2021) <DOI:10.25236/AJBM.2021.031018>,
Cuesta-Albertos et al. (1997)
<https://www.jstor.org/stable/2242558?seq=1>.

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
