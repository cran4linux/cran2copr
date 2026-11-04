%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clustEff
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clusters of Effects Curves in Quantile Regression Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
Requires:         R-CRAN-cluster 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-splines 
Requires:         R-stats 

%description
Clustering of curves based on a dissimilarity that combines the
concordance of their shapes and their closeness, as proposed by Sottile
and Adelfio (2019) <doi:10.1007/s00180-018-0817-8>. The method can be
applied to the effects curves of quantile regression coefficients models
fitted with 'qrcm', with univariate or multivariate responses, and to
curves observed in time, as in functional data analysis. The package also
implements the clustering of waveforms by trimmed k-means of functional
principal component scores (Adelfio, Chiodi, D'Alessandro and Luzio,
2011).

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
