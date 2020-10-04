%global packname  clustrd
%global packver   1.3.7-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7.2
Release:          3%{?dist}%{?buildtag}
Summary:          Methods for Joint Dimension Reduction and Clustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ca 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-rARPACK 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-fpc 
Requires:         R-cluster 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ca 
Requires:         R-stats 

%description
A class of methods that combine dimension reduction and clustering of
continuous, categorical or mixed-type data (Markos, Iodice D'Enza and van
de Velden 2019; <DOI:10.18637/jss.v091.i10>). For continuous data, the
package contains implementations of factorial K-means (Vichi and Kiers
2001; <DOI:10.1016/S0167-9473(00)00064-5>) and reduced K-means (De Soete
and Carroll 1994; <DOI:10.1007/978-3-642-51175-2_24>); both methods that
combine principal component analysis with K-means clustering. For
categorical data, the package provides MCA K-means (Hwang, Dillon and
Takane 2006; <DOI:10.1007/s11336-004-1173-x>), i-FCB (Iodice D'Enza and
Palumbo 2013, <DOI:10.1007/s00180-012-0329-x>) and Cluster Correspondence
Analysis (van de Velden, Iodice D'Enza and Palumbo 2017;
<DOI:10.1007/s11336-016-9514-0>), which combine multiple correspondence
analysis with K-means. For mixed-type data, it provides mixed Reduced
K-means and mixed Factorial K-means (van de Velden, Iodice D'Enza and
Markos 2019; <DOI:10.1002/wics.1456>), which combine PCA for mixed-type
data with K-means.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
