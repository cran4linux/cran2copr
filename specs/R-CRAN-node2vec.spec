%global packname  node2vec
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Algorithmic Framework for Representational Learning on Graphs

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-word2vec 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-word2vec 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-vegan 

%description
Given any graph, the 'node2vec' algorithm can learn continuous feature
representations for the nodes, which can then be used for various
downstream machine learning tasks.The techniques are detailed in the paper
"node2vec: Scalable Feature Learning for Networks" by Aditya Grover, Jure
Leskovec(2016),available at <arXiv:1607.00653>.

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
