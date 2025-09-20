%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  networkABC
%global packver   0.9-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Network Reverse Engineering with Approximate Bayesian Computation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-sna 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-network 
Requires:         R-CRAN-sna 

%description
We developed an inference tool based on approximate Bayesian computation
to decipher network data and assess the strength of the inferred links
between network's actors. It is a new multi-level approximate Bayesian
computation (ABC) approach. At the first level, the method captures the
global properties of the network, such as a scale-free structure and
clustering coefficients, whereas the second level is targeted to capture
local properties, including the probability of each couple of genes being
linked. Up to now, Approximate Bayesian Computation (ABC) algorithms have
been scarcely used in that setting and, due to the computational overhead,
their application was limited to a small number of genes. On the contrary,
our algorithm was made to cope with that issue and has low computational
cost. It can be used, for instance, for elucidating gene regulatory
network, which is an important step towards understanding the normal cell
physiology and complex pathological phenotype. Reverse-engineering
consists in using gene expressions over time or over different
experimental conditions to discover the structure of the gene network in a
targeted cellular process. The fact that gene expression data are usually
noisy, highly correlated, and have high dimensionality explains the need
for specific statistical methods to reverse engineer the underlying
network.

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
