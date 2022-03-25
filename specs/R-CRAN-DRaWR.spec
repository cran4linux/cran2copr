%global __brp_check_rpaths %{nil}
%global packname  DRaWR
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Discriminative Random Walk with Restart

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ROCR 
Requires:         R-methods 

%description
We present DRaWR, a network-based method for ranking genes or properties
related to a given gene set. Such related genes or properties are
identified from among the nodes of a large, heterogeneous network of
biological information. Our method involves a random walk with restarts,
performed on an initial network with multiple node and edge types,
preserving more of the original, specific property information than
current methods that operate on homogeneous networks. In this first stage
of our algorithm, we find the properties that are the most relevant to the
given gene set and extract a subnetwork of the original network,
comprising only the relevant properties. We then rerank genes by their
similarity to the given gene set, based on a second random walk with
restarts, performed on the above subnetwork.

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
