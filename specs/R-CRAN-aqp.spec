%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aqp
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Algorithms for Quantitative Pedology

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-farver 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-ape 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-farver 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-ape 

%description
The Algorithms for Quantitative Pedology (AQP) project was started in 2009
to organize a loosely-related set of concepts and source code on the topic
of soil profile visualization, aggregation, and classification into this
package (aqp). Over the past 8 years, the project has grown into a suite
of related R packages that enhance and simplify the quantitative analysis
of soil profile data. Central to the AQP project is a new vocabulary of
specialized functions and data structures that can accommodate the
inherent complexity of soil profile information; freeing the scientist to
focus on ideas rather than boilerplate data processing tasks
<doi:10.1016/j.cageo.2012.10.020>. These functions and data structures
have been extensively tested and documented, applied to projects involving
hundreds of thousands of soil profiles, and deeply integrated into widely
used tools such as SoilWeb
<https://casoilresource.lawr.ucdavis.edu/soilweb-apps>. Components of the
AQP project (aqp, soilDB, sharpshootR, soilReports packages) serve an
important role in routine data analysis within the USDA-NRCS Soil Science
Division. The AQP suite of R packages offer a convenient platform for
bridging the gap between pedometric theory and practice.

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
