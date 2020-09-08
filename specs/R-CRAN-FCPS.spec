%global packname  FCPS
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Fundamental Clustering Problems Suite

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


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
Many conventional clustering algorithms are provided in this package with
consistent input and output, which enables the user to try out algorithms
swiftly. Additionally, 26 statistical approaches for the estimation of the
number of clusters as well as the the mirrored density plot (MD-plot) of
clusterability are implemented. Moreover, the fundamental clustering
problems suite (FCPS) offers a variety of clustering challenges any
algorithm should handle when facing real world data, see Thrun, M.C.,
Ultsch A.: "Clustering Benchmark Datasets Exploiting the Fundamental
Clustering Problems" (2020), Data in Brief,
<DOI:10.1016/j.dib.2020.105501>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
