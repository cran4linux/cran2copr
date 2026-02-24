%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pkggraph
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Explore the R Package Dependencies on the Comprehensive R Archive Network (CRAN) Like Repositories

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-checkmate >= 2.3.0
BuildRequires:    R-CRAN-ggraph >= 2.2.2
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-BiocManager >= 1.30.27
BuildRequires:    R-CRAN-tidygraph >= 1.3.1
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-tibble >= 1.3.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.1
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-checkmate >= 2.3.0
Requires:         R-CRAN-ggraph >= 2.2.2
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-BiocManager >= 1.30.27
Requires:         R-CRAN-tidygraph >= 1.3.1
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-tibble >= 1.3.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.1
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-tools 
Requires:         R-utils 

%description
Explore various dependencies of a packages (on the Comprehensive R Archive
Network Like repositories). The functions get_neighborhood() and
get_dependencies() provide dependencies of packages and as_graph() can be
used to convert into a 'igraph' object for further analysis and plotting.

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
