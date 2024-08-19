%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HierPortfolios
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Risk Clustering Portfolio Allocation Strategies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-cluster 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-cluster 

%description
Machine learning hierarchical risk clustering portfolio allocation
strategies. The implemented methods are: Hierarchical risk parity (De
Prado, 2016) <DOI: 10.3905/jpm.2016.42.4.059>. Hierarchical
clustering-based asset allocation (Raffinot, 2017) <DOI:
10.3905/jpm.2018.44.2.089>. Hierarchical equal risk contribution portfolio
(Raffinot, 2018) <DOI: 10.2139/ssrn.3237540>. A Constrained Hierarchical
Risk Parity Algorithm with Cluster-based Capital Allocation (Pfitzingera
and Katzke, 2019)
<https://www.ekon.sun.ac.za/wpapers/2019/wp142019/wp142019.pdf>.

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
