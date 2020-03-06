%global packname  EGAnet
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          1%{?dist}
Summary:          Exploratory Graph Analysis - A Framework for Estimating theNumber of Dimensions in Multivariate Data Using NetworkPsychometrics

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-qgraph >= 1.4.1
BuildRequires:    R-Matrix >= 1.2
BuildRequires:    R-CRAN-glasso >= 1.10
BuildRequires:    R-CRAN-NetworkToolbox >= 1.1.2
BuildRequires:    R-CRAN-semPlot >= 1.0.1
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-lavaan >= 0.5.22
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-qgraph >= 1.4.1
Requires:         R-Matrix >= 1.2
Requires:         R-CRAN-glasso >= 1.10
Requires:         R-CRAN-NetworkToolbox >= 1.1.2
Requires:         R-CRAN-semPlot >= 1.0.1
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-lavaan >= 0.5.22
Requires:         R-stats 
Requires:         R-CRAN-plotly 

%description
An implementation of the Exploratory Graph Analysis (EGA) framework for
dimensionality assessment. EGA is part of a new area called network
psychometrics that focuses on the estimation of undirected network models
in psychological datasets. EGA estimates the number of dimensions or
factors using graphical lasso or Triangulated Maximally Filtered Graph
(TMFG) and a weighted network community analysis. A bootstrap method for
verifying the stability of the estimation is also available. The fit of
the structure suggested by EGA can be verified using confirmatory factor
analysis and a direct way to convert the EGA structure to a confirmatory
factor model is also implemented. Documentation and examples are
available. Golino, H. F., & Epskamp, S. (2017)
<doi:10.1371/journal.pone.0174035>. Golino, H. F., & Demetriou, A. (2017)
<doi:10.1016/j.intell.2017.02.007> Golino, H., Shi, D., Garrido, L. E.,
Christensen, A. P., Nieto, M. D., Sadana, R., & Thiyagarajan, J. A. (2018)
<doi:10.31234/osf.io/gzcre>. Christensen, A. P. & Golino, H.F. (2019)
<doi:10.31234/osf.io/9deay>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
