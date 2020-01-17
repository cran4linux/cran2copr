%global packname  aqp
%global packver   1.18.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.18.1
Release:          1%{?dist}
Summary:          Algorithms for Quantitative Pedology

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-grid 
BuildRequires:    R-lattice 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-digest 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape 
Requires:         R-grid 
Requires:         R-lattice 
Requires:         R-cluster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-MASS 
Requires:         R-CRAN-digest 

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
<https://casoilresource.lawr.ucdavis.edu/soilweb-apps/>. Components of the
AQP project (aqp, soilDB, sharpshootR, soilReports packages) serve an
important role in routine data analysis within the USDA-NRCS Soil Science
Division. The AQP suite of R packages offer a convenient platform for
bridging the gap between pedometric theory and practice.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/_pkgdown.yml
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/example-data
%{rlibdir}/%{packname}/INDEX
