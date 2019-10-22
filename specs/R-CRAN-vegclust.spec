%global packname  vegclust
%global packver   1.7.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.7
Release:          1%{?dist}
Summary:          Fuzzy Clustering of Vegetation Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-MASS 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-sp 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-Kendall 
Requires:         R-CRAN-circular 
Requires:         R-MASS 

%description
A set of functions to: (1) perform fuzzy clustering of vegetation data [De
Caceres et al. (2010) <doi:10.1111/j.1654-1103.2010.01211.x>]; (2) to
assess ecological community ressemblance on the basis of structure and
composition [De Caceres et al. (2013): <doi:10.1111/2041-210X.12116>]; and
(3) to perform community trajectory analysis [De Caceres et al. (2019):
<doi:10.1002/ecm.1350>].

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
