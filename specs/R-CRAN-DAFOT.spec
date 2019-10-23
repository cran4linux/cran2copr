%global packname  DAFOT
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Detector of Active Flow on a Tree

License:          MIT+file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tidytree 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-tidytree 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ape 

%description
Quantitative comparison of microbial composition from different
populations is a fundamental task in various microbiome studies. The main
goal of this package is to provide a new method for two-sample testing for
microbial compositional data by leveraging the phylogenetic tree
information. Empirical evidence from real data sets suggests that the
phylogenetic microbial composition difference between two populations is
usually sparse. Motivated by this observation, this package implements a
new maximum type test, Detector of Active Flow on a Tree (DAFOT). It is
shown that DAFOT is particularly powerful against sparse phylogenetic
composition difference and enjoys certain optimality. Chen, J., Bittinger,
K., Charlson, E. S., Hoffmann, C., Lewis, J., Wu, G. D., Collman, R. G.,
Bushman, F. D., Li, H. (2012) <doi:10.1093/bioinformatics/bts342>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
