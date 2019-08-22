%global packname  bigdatadist
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Distances for Machine Learning and Statistics in the Context ofBig Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-pdist 
Requires:         R-MASS 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-pdist 

%description
Functions to compute distances between probability measures or any other
data object than can be posed in this way, entropy measures for samples of
curves, distances and depth measures for functional data, and the
Generalized Mahalanobis Kernel distance for high dimensional data. For
further details about the metrics please refer to Martos et al (2014)
<doi:10.3233/IDA-140706>; Martos et al (2018) <doi:10.3390/e20010033>;
Hernandez et al (2018, submitted); Martos et al (2018, submitted).

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
