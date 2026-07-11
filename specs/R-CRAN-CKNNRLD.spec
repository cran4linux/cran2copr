%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CKNNRLD
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering-Based K-Nearest Neighbor Regression for Longitudinal Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Directional 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
Requires:         R-CRAN-Directional 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 

%description
Implements the 'CKNNRLD' algorithm (Clustering-Based K-Nearest Neighbor
Regression for Longitudinal Data) for improving K-Nearest Neighbor ('KNN')
regression on longitudinal data through cluster-based partitioning and
localized prediction. Offers enhanced computational efficiency and
accuracy for high-volume longitudinal datasets. The acronym 'KNN' stands
for K-Nearest Neighbor. References: Loeloe MS, Tabatabaei SM, Sefidkar R,
Mehrparvar AH, Jambarsang S (2025). "Boosting K-nearest neighbor
regression performance for longitudinal data through a novel learning
approach." BMC Bioinformatics, 26, 232. <doi:10.1186/s12859-025-06205-1>.

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
