%global packname  seriation
%global packver   1.2-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.8
Release:          2%{?dist}
Summary:          Infrastructure for Ordering Objects Using Seriation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-TSP 
BuildRequires:    R-CRAN-qap 
BuildRequires:    R-grid 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-gclus 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-registry 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-TSP 
Requires:         R-CRAN-qap 
Requires:         R-grid 
Requires:         R-cluster 
Requires:         R-CRAN-gclus 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-colorspace 
Requires:         R-MASS 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-registry 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Infrastructure for ordering objects with an implementation of several
seriation/sequencing/ordination techniques to reorder matrices,
dissimilarity matrices, and dendrograms. Also provides (optimally)
reordered heatmaps, color images and clustering visualizations like
dissimilarity plots, and visual assessment of cluster tendency plots (VAT
and iVAT).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
