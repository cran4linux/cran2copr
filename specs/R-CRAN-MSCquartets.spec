%global packname  MSCquartets
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Analyzing Gene Tree Quartets under the Multi-Species Coalescent

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-RandomFieldsUtils 
BuildRequires:    R-CRAN-zipfR 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-ape >= 5.0
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-RandomFieldsUtils 
Requires:         R-CRAN-zipfR 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 

%description
Methods for analyzing and using quartets displayed on a collection of gene
trees, primarily to make inferences about the species tree or network
under the multi-species coalescent model. These include quartet hypothesis
tests for the model, as developed by Mitchell et al. (2019)
<doi:10.1214/19-EJS1576>, the species tree inference routines based on
quartet distances of Rhodes (2019) <doi:10.1109/TCBB.2019.2917204> and
Yourdkhani and Rhodes (2019), and the NANUQ algorithm for inference of
level-1 species networks of Allman et al. (2019) <arXiv:1905.07050>.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
