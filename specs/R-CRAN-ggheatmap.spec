%global __brp_check_rpaths %{nil}
%global packname  ggheatmap
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plot Heatmap

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-aplot 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-aplot 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-tidyr 

%description
The flexibility and excellence of 'ggplot2' is unquestionable, so many
drawing tools basically need 'ggplot2' as the operating object. In order
to develop a heatmap drawing system based on ggplot2, we developed this
tool, mainly to solve the heatmap puzzle problem and the flexible
connection between the heatmap and the 'ggplot2' object. The advantages of
this tool are as follows: 1. More flexible label settings; 2. Realize the
linkage of heatmap and 'ggplot2' drawing system, which is helpful for
operations such as puzzles; 3. Simple and easy to operate; 4. Optimization
of clustering tree visualization.

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
