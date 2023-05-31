%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FCPS
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Fundamental Clustering Problems Suite

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DataVisualizations 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DataVisualizations 

%description
Over sixty clustering algorithms are provided in this package with
consistent input and output, which enables the user to try out algorithms
swiftly. Additionally, 26 statistical approaches for the estimation of the
number of clusters as well as the mirrored density plot (MD-plot) of
clusterability are implemented. The packages is published in Thrun, M.C.,
Stier Q.: "Fundamental Clustering Algorithms Suite" (2021), SoftwareX,
<DOI:10.1016/j.softx.2020.100642>. Moreover, the fundamental clustering
problems suite (FCPS) offers a variety of clustering challenges any
algorithm should handle when facing real world data, see Thrun, M.C.,
Ultsch A.: "Clustering Benchmark Datasets Exploiting the Fundamental
Clustering Problems" (2020), Data in Brief,
<DOI:10.1016/j.dib.2020.105501>.

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
