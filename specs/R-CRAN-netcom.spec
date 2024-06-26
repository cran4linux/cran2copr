%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  netcom
%global packver   2.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          NETwork COMparison Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggfortify 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggfortify 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-reshape2 

%description
Infer system functioning with empirical NETwork COMparisons. These methods
are part of a growing paradigm in network science that uses relative
comparisons of networks to infer mechanistic classifications and predict
systemic interventions. They have been developed and applied in Langendorf
and Burgess (2021) <doi:10.1038/s41598-021-99251-7>, Langendorf (2020)
<doi:10.1201/9781351190831-6>, and Langendorf and Goldberg (2019)
<doi:10.48550/arXiv.1912.12551>.

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
