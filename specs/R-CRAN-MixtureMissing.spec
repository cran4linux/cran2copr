%global __brp_check_rpaths %{nil}
%global packname  MixtureMissing
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Model-Based Clustering for Data Sets with Missing Values at Random

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-cluster >= 2.1.2
BuildRequires:    R-CRAN-mnormt >= 2.0.2
BuildRequires:    R-CRAN-GGally >= 2.0.0
BuildRequires:    R-CRAN-rootSolve >= 1.8.2.2
BuildRequires:    R-CRAN-ContaminatedMixt >= 1.3.4.1
BuildRequires:    R-CRAN-mvtnorm >= 1.1.2
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-cluster >= 2.1.2
Requires:         R-CRAN-mnormt >= 2.0.2
Requires:         R-CRAN-GGally >= 2.0.0
Requires:         R-CRAN-rootSolve >= 1.8.2.2
Requires:         R-CRAN-ContaminatedMixt >= 1.3.4.1
Requires:         R-CRAN-mvtnorm >= 1.1.2

%description
Implementation of robust model based cluster analysis with missing data.
The models used are: Multivariate Contaminated Normal Mixtures (MCNM),
Multivariate Student's t Mixtures (MtM), and Multivariate Normal Mixtures
(MNM) for data sets with missing values at random. "Cluster analysis and
outlier detection with missing data" Hung Tong, Cristina Tortora (2020)
<arXiv:2012.05394>.

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
