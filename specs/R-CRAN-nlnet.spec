%global packname  nlnet
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Network, Clustering, and Variable Selection Based on DCOL

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-TSP 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-TSP 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-coin 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-e1071 

%description
It includes four methods: DCOL-based K-profiles clustering, non-linear
network reconstruction, non-linear hierarchical clustering, and variable
selection for generalized additive model. References: Tianwei Yu
(2018)<DOI: 10.1002/sam.11381>; Haodong Liu and others (2016)<DOI:
10.1371/journal.pone.0158247>; Kai Wang and others (2015)<DOI:
10.1155/2015/918954>; Tianwei Yu and others (2010)<DOI:
10.1109/TCBB.2010.73>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
