%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DDPNA
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Disease-Drived Differential Proteins Co-Expression Network Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggalt 
BuildRequires:    R-CRAN-MEGENA 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-VennDiagram 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggalt 
Requires:         R-CRAN-MEGENA 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Hmisc 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-scales 
Requires:         R-grid 
Requires:         R-CRAN-VennDiagram 

%description
Functions designed to connect disease-related differential proteins and
co-expression network. It provides the basic statics analysis included t
test, ANOVA analysis. The network construction is not offered by the
package, you can used 'WGCNA' package which you can learn in Peter et al.
(2008) <doi:10.1186/1471-2105-9-559>. It also provides module analysis
included PCA analysis, two enrichment analysis, Planner maximally filtered
graph extraction and hub analysis.

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
