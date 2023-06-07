%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  boxplotcluster
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering Method Based on Boxplot Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-graphics >= 4.0.0
BuildRequires:    R-grDevices >= 4.0.0
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-cluster >= 2.1.4
Requires:         R-graphics >= 4.0.0
Requires:         R-grDevices >= 4.0.0
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-cluster >= 2.1.4

%description
Following Arroyo-Maté-Roque (2006), the function calculates the distance
between rows or columns of the dataset using the generalized Minkowski
metric as described by Ichino-Yaguchi (1994). The distance measure gives
more weight to differences between quartiles than to differences between
extremes, making it less sensitive to outliers. Further,the function
calculates the silhouette width (Rousseeuw 1987) for different numbers of
clusters and selects the number of clusters that maximizes the average
silhouette width, unless a specific number of clusters is provided by the
user. The approach implemented in this package is based on the following
publications: Rousseeuw (1987) <doi:10.1016/0377-0427(87)90125-7>;
Ichino-Yaguchi (1994) <doi:10.1109/21.286391>; Arroyo-Maté-Roque (2006)
<doi:10.1007/3-540-34416-0_7>.

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
