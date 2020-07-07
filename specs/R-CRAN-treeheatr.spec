%global packname  treeheatr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Heatmap-Integrated Decision Tree Visualizations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggparty 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-cluster 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-seriation 
Requires:         R-CRAN-ggparty 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-gtable 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-cluster 
Requires:         R-grid 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-seriation 

%description
Creates interpretable decision tree visualizations with the data
represented as a heatmap at the tree's leaf nodes. 'treeheatr' utilizes
the customizable 'ggparty' package for drawing decision trees.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
