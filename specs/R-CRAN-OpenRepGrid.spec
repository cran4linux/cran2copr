%global __brp_check_rpaths %{nil}
%global packname  OpenRepGrid
%global packver   0.1.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.12
Release:          2%{?dist}%{?buildtag}
Summary:          Tools to Analyze Repertory Grid Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-pvclust 
BuildRequires:    R-CRAN-openxlsx 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-XML 
Requires:         R-tcltk 
Requires:         R-CRAN-pvclust 
Requires:         R-CRAN-openxlsx 

%description
Analyze repertory grids, a qualitative-quantitative data collection
technique devised by George A. Kelly in the 1950s. Today, grids are used
across various domains ranging from clinical psychology to marketing. The
package contains functions to quantitatively analyze and visualize
repertory grid data (see e.g. Bell, 2005, <doi:10.1002/0470013370.ch9>;
Fransella, Bell, & Bannister, 2004, ISBN: 978-0-470-09080-0).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
