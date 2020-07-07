%global packname  forestr
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          3%{?dist}
Summary:          Ecosystem and Canopy Structural Complexity Metrics from LiDAR

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-tibble 

%description
Provides a toolkit for calculating forest and canopy structural complexity
metrics from terrestrial LiDAR (light detection and ranging). References:
Atkins et al. 2018 <doi:10.1111/2041-210X.13061>; Hardiman et al. 2013
<doi:10.3390/f4030537>; Parker et al. 2004
<doi:10.1111/j.0021-8901.2004.00925.x>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/pcl-vignette_files
%doc %{rlibdir}/%{packname}/pcl-vignette.html
%doc %{rlibdir}/%{packname}/pcl-vignette.pdf
%{rlibdir}/%{packname}/INDEX
