%global packname  aPCoA
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Covariate Adjusted PCoA Plot

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-randomcoloR 
BuildRequires:    R-CRAN-mvabund 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-cluster 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-randomcoloR 
Requires:         R-CRAN-mvabund 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-car 
Requires:         R-cluster 

%description
In fields such as ecology, microbiology, and genomics, non-Euclidean
distances are widely applied to describe pairwise dissimilarity between
samples. Given these pairwise distances, principal coordinates analysis
(PCoA) is commonly used to construct a visualization of the data. However,
confounding covariates can make patterns related to the scientific
question of interest difficult to observe. We provide 'aPCoA' as an
easy-to-use tool to improve data visualization in this context, enabling
enhanced presentation of the effects of interest. Details are described in
Yushu Shi, Liangliang Zhang, Kim-Anh Do, Christine Peterson and Robert
Jenq (2020) <arXiv:2003.09544>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
