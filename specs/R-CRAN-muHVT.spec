%global packname  muHVT
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Constructing Hierarchical Voronoi Tessellations and OverlayHeatmap for Data Analysis

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-conf.design 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-polyclip 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-CRAN-deldir 
Requires:         R-grDevices 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-conf.design 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-polyclip 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-ggplot2 

%description
Constructing hierarchical voronoi tessellations for a given data set and
overlay heatmap for variables at various levels of the tessellations for
in-depth data analysis. See
<https://en.wikipedia.org/wiki/Voronoi_diagram> for more information.
Credits to Mu Sigma for their continuous support throughout the
development of the package.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
