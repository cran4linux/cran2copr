%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mecoturn
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Decipher Microbial Turnover along a Gradient

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-microeco >= 0.20.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-GUniFrac 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-CRAN-glmmTMB 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-microeco >= 0.20.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-GUniFrac 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-betareg 
Requires:         R-CRAN-glmmTMB 

%description
Two pipelines are provided to study microbial turnover along a gradient,
including the beta diversity and microbial abundance change. The
'betaturn' class consists of the steps of community dissimilarity matrix
generation, matrix conversion, differential test and visualization. The
workflow of 'taxaturn' class includes the taxonomic abundance calculation,
abundance transformation, abundance change summary, statistical analysis
and visualization. Multiple statistical approaches can contribute to the
analysis of microbial turnover.

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
