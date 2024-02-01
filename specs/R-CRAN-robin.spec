%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robin
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          ROBustness in Network

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-fdatest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-qpdf 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-fdatest 
Requires:         R-methods 
Requires:         R-CRAN-gridExtra 
Requires:         R-parallel 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-qpdf 
Requires:         R-CRAN-Matrix 

%description
Assesses the robustness of the community structure of a network found by
one or more community detection algorithm to give indications about their
reliability. It detects if the community structure found by a set of
algorithms is statistically significant and compares the different
selected detection algorithms on the same network. robin helps to choose
among different community detection algorithms the one that better fits
the network of interest. Reference in Policastro V., Righelli D.,
Carissimo A., Cutillo L., De Feis I. (2021)
<https://journal.r-project.org/archive/2021/RJ-2021-040/index.html>.

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
