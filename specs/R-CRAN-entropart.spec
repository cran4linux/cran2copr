%global packname  entropart
%global packver   1.6-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.7
Release:          1%{?dist}%{?buildtag}
Summary:          Entropy Partitioning to Measure Diversity

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-EntropyEstimation 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-SPECIES 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-EntropyEstimation 
Requires:         R-CRAN-ggpubr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-SPECIES 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-vegan 

%description
Measurement and partitioning of diversity, based on Tsallis entropy,
following Marcon and Herault (2015) <doi:10.18637/jss.v067.i08>.
'entropart' provides functions to calculate alpha, beta and gamma
diversity of communities, including phylogenetic and functional diversity.
Estimation-bias corrections are available.

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
