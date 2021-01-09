%global packname  KPC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel Partial Correlation Coefficient

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-emstreeR 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-proxy 
Requires:         R-parallel 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-emstreeR 

%description
Implementations of two empirical versions the kernel partial correlation
(KPC) coefficient and the associated variable selection algorithms. KPC is
a measure of the strength of conditional association between Y and Z given
X, with X, Y, Z being random variables taking values in general
topological spaces. As the name suggests, KPC is defined in terms of
kernels on reproducing kernel Hilbert spaces (RKHSs). The population KPC
is a deterministic number between 0 and 1; it is 0 if and only if Y is
conditionally independent of Z given X, and it is 1 if and only if Y is a
measurable function of Z and X. One empirical KPC estimator is based on
geometric graphs, such as K-nearest neighbor graphs and minimum spanning
trees, and is consistent under very weak conditions. The other empirical
estimator, defined using conditional mean embeddings (CMEs) as used in the
RKHS literature, is also consistent under suitable conditions. Using KPC,
a stepwise forward variable selection algorithm KFOCI (using the graph
based estimator of KPC) is provided, as well as a similar stepwise forward
selection algorithm based on the RKHS based estimator. For more details on
KPC, its empirical estimators and its application on variable selection,
see Huang, Z., N. Deb, and B. Sen (2020). “Kernel partial correlation
coefficient – a measure of conditional dependence” <arXiv:2012.14804>.
When X is empty, KPC measures the unconditional dependence between Y and
Z, which has been described in Deb, N., P. Ghosal, and B. Sen (2020),
“Measuring association on topological spaces using kernels and geometric
graphs” <arXiv:2010.01768>, and it is implemented in the functions KMAc()
and Klin() in this package. The latter can be computed in near linear
time.

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
