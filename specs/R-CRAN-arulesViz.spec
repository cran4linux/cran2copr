%global packname  arulesViz
%global packver   1.5-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing Association Rules and Frequent Itemsets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-arules >= 1.6.0
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-seriation 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggnetwork 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-arules >= 1.6.0
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-seriation 
Requires:         R-CRAN-colorspace 
Requires:         R-grid 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggnetwork 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-visNetwork 

%description
Extends package 'arules' with various visualization techniques for
association rules and itemsets. The package also includes several
interactive visualizations for rule exploration. Michael Hahsler (2017)
<doi:10.32614/RJ-2017-047>.

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
