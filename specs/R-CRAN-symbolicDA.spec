%global packname  symbolicDA
%global packver   0.6-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          Analysis of Symbolic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-clusterSim 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-shapes 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-RSDA 
Requires:         R-CRAN-clusterSim 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-shapes 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ade4 
Requires:         R-cluster 
Requires:         R-CRAN-RSDA 

%description
Symbolic data analysis methods: importing/exporting data from ASSO XML
Files, distance calculation for symbolic data (Ichino-Yaguchi, de Carvalho
measure), zoom star plot, 3d interval plot, multidimensional scaling for
symbolic interval data, dynamic clustering based on distance matrix, HINoV
method for symbolic data, Ichino's feature selection method, principal
component analysis for symbolic interval data, decision trees for symbolic
data based on optimal split with bagging, boosting and random forest
approach (+visualization), kernel discriminant analysis for symbolic data,
Kohonen's self-organizing maps for symbolic data, replication and
profiling, artificial symbolic data generation. (Milligan, G.W., Cooper,
M.C. (1985) <doi:10.1007/BF02294245>, Breiman, L. (1996),
<doi:10.1007/BF00058655>, Hubert, L., Arabie, P. (1985),
<doi:10.1007%2FBF01908075>, Ichino, M., & Yaguchi, H. (1994),
<doi:10.1109/21.286391>, Rand, W.M. (1971)
<doi:10.1080/01621459.1971.10482356>, Calinski, T., Harabasz, J. (1974)
<doi:10.1080/03610927408827101>, Breckenridge, J.N. (2000)
<doi:10.1207/S15327906MBR3502_5>, Groenen, P.J.F, Winsberg, S., Rodriguez,
O., Diday, E. (2006) <doi:10.1016/j.csda.2006.04.003>, Walesiak, M.,
Dudek, A. (2008) <doi:10.1007/978-3-540-78246-9_11>, Dudek, A. (2007),
<doi:10.1007/978-3-540-70981-7_4>).

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
%doc %{rlibdir}/%{packname}/csv
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/pdf
%doc %{rlibdir}/%{packname}/xml
%{rlibdir}/%{packname}/INDEX
