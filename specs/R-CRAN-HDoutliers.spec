%global packname  HDoutliers
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Leland Wilkinson's Algorithm for Detecting MultidimensionalOutliers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-mclust 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-mclust 

%description
An implementation of an algorithm for outlier detection that can handle a)
data with a mixed categorical and continuous variables, b) many columns of
data, c) many rows of data, d) outliers that mask other outliers, and e)
both unidimensional and multidimensional datasets. Unlike ad hoc methods
found in many machine learning papers, HDoutliers is based on a
distributional model that uses probabilities to determine outliers. See
<https://www.cs.uic.edu/~wilkinson/Publications/outliers.pdf>.

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
