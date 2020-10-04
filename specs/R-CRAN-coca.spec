%global packname  coca
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Cluster-of-Clusters Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-Matrix 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-sparcl 
BuildRequires:    R-stats 
Requires:         R-CRAN-caret 
Requires:         R-cluster 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-glmnet 
Requires:         R-Matrix 
Requires:         R-nnet 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-sparcl 
Requires:         R-stats 

%description
Contains the R functions needed to perform Cluster-Of-Clusters Analysis
(COCA) and Consensus Clustering (CC). For further details please see
Cabassi and Kirk (2020) <doi:10.1093/bioinformatics/btaa593>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
