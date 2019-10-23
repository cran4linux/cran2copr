%global packname  SubgrPlots
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Graphical Displays for Subgroup Analysis in Clinical Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.1.1
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-alluvial 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geoR 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridBase 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-polyclip 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-survRM2 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-UpSetR 
BuildRequires:    R-CRAN-VennDiagram 
Requires:         R-CRAN-ggplot2 >= 2.1.1
Requires:         R-graphics 
Requires:         R-CRAN-alluvial 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geoR 
Requires:         R-grid 
Requires:         R-CRAN-gridBase 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-polyclip 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-survRM2 
Requires:         R-survival 
Requires:         R-CRAN-UpSetR 
Requires:         R-CRAN-VennDiagram 

%description
Provides functions for obtaining a variety of graphical displays that may
be useful in the subgroup analysis setting. An example with a prostate
cancer dataset is provided. The graphical techniques considered include
level plots, mosaic plots, contour plots, bar charts, Venn diagrams, tree
plots, forest plots, Galbraith plots, L'Abbé plots, the subpopulation
treatment effect pattern plot, alluvial plots, circle plots and UpSet
plots.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/paper
%{rlibdir}/%{packname}/INDEX
