%global packname  discourseGT
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Group Patterns using Graph Theory in Educational Settings

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-network 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggrepel 

%description
Analyzes group patterns using discourse analysis data with graph theory
mathematics. Takes the order of which individuals talk and converts it to
a network edge and weight list. Returns the density, centrality,
centralization, and subgroup information for each group. Based on the
analytical framework laid out in Chai et al. (2019)
<doi:10.1187/cbe.18-11-0222>.

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
