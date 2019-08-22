%global packname  arulesViz
%global packver   1.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          1%{?dist}
Summary:          Visualizing Association Rules and Frequent Itemsets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-arules >= 1.4.1
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-seriation 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-arules >= 1.4.1
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-grid 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-seriation 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-visNetwork 

%description
Extends package 'arules' with various visualization techniques for
association rules and itemsets. The package also includes several
interactive visualizations for rule exploration.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
