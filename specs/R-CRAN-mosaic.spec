%global packname  mosaic
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Project MOSAIC Statistics and Mathematics Teaching Utilities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mosaicCore >= 0.5.0
BuildRequires:    R-lattice >= 0.20.21
BuildRequires:    R-CRAN-lazyeval >= 0.2.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggformula 
BuildRequires:    R-CRAN-mosaicData 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-MASS 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-leaflet 
Requires:         R-CRAN-mosaicCore >= 0.5.0
Requires:         R-lattice >= 0.20.21
Requires:         R-CRAN-lazyeval >= 0.2.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggformula 
Requires:         R-CRAN-mosaicData 
Requires:         R-Matrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-MASS 
Requires:         R-grid 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-splines 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-leaflet 

%description
Data sets and utilities from Project MOSAIC (<http://mosaic-web.org>) used
to teach mathematics, statistics, computation and modeling.  Funded by the
NSF, Project MOSAIC is a community of educators working to tie together
aspects of quantitative work that students in science, technology,
engineering and mathematics will need in their professional lives, but
which are usually taught in isolation, if at all.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/google
%{rlibdir}/%{packname}/otherdata
%doc %{rlibdir}/%{packname}/rmarkdown
%{rlibdir}/%{packname}/INDEX
