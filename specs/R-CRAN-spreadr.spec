%global __brp_check_rpaths %{nil}
%global packname  spreadr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulating Spreading Activation in a Network

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-ggplot2 

%description
The notion of spreading activation is a prevalent metaphor in the
cognitive sciences. This package provides the tools for cognitive
scientists and psychologists to conduct computer simulations that
implement spreading activation in a network representation. The
algorithmic method implemented in 'spreadr' subroutines follows the
approach described in Vitevitch, Ercal, and Adagarla (2011, Frontiers),
who viewed activation as a fixed cognitive resource that could spread
among nodes that were connected to each other via edges or connections
(i.e., a network). See Vitevitch, M. S., Ercal, G., & Adagarla, B. (2011).
Simulating retrieval from a highly clustered network: Implications for
spoken word recognition. Frontiers in Psychology, 2, 369.
<doi:10.3389/fpsyg.2011.00369> and Siew, C. S. Q. (2019). spreadr: A R
package to simulate spreading activation in a network. Behavior Research
Methods, 51, 910-929. <doi: 10.3758/s13428-018-1186-5>.

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
