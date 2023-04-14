%global __brp_check_rpaths %{nil}
%global packname  foodingraph
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Food Network Inference and Visualization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-minerva 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-grid 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-minerva 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-labeling 
Requires:         R-grid 

%description
Displays a weighted undirected food graph from an adjacency matrix. Can
perform confidence-interval bootstrap inference with mutual information or
maximal information coefficient. Based on my Master 1 internship at the
Bordeaux Population Health center. References : Reshef et al. (2011)
<doi:10.1126/science.1205438>, Meyer et al. (2008)
<doi:10.1186/1471-2105-9-461>, Liu et al. (2016)
<doi:10.1371/journal.pone.0158247>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
