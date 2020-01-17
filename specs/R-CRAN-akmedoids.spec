%global packname  akmedoids
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Anchored Kmedoids for Longitudinal Data Clustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-kml 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-longitudinalData 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-signal 
Requires:         R-CRAN-kml 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-longitudinalData 
Requires:         R-stats 
Requires:         R-CRAN-signal 

%description
Advances a novel adaptation of longitudinal k-means clustering technique
(Genolini et al. (2015) <doi:10.18637/jss.v065.i04>) for grouping
trajectories based on the similarities of their long-term trends and
determines the optimal solution based on either the average silhouette
width (Rousseeuw P. J. 1987) or the Calinski-Harabatz criterion (Calinski
and Harabatz (1974) <doi:10.1080/03610927408827101>). Includes functions
to extract descriptive statistics and generate a visualisation of the
resulting groups, drawing methods from the 'ggplot2' library (Wickham H.
(2016) <doi:10.1007/978-3-319-24277-4>). The package also includes a
number of other useful functions for exploring and manipulating
longitudinal data prior to the clustering process.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
