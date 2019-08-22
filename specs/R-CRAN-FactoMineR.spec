%global packname  FactoMineR
%global packver   1.42
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.42
Release:          1%{?dist}
Summary:          Multivariate Exploratory Data Analysis and Data Mining

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-flashClust 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-car 
Requires:         R-cluster 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-flashClust 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-lattice 
Requires:         R-CRAN-leaps 
Requires:         R-MASS 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-stats 
Requires:         R-utils 

%description
Exploratory data analysis methods to summarize, visualize and describe
datasets. The main principal component methods are available, those with
the largest potential in terms of applications: principal component
analysis (PCA) when variables are quantitative, correspondence analysis
(CA) and multiple correspondence analysis (MCA) when variables are
categorical, Multiple Factor Analysis when variables are structured in
groups, etc. and hierarchical cluster analysis. F. Husson, S. Le and J.
Pages (2017).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
