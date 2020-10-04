%global packname  nodiv
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Compares the Distribution of Sister Clades Through a Phylogeny

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-utils 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-vegan 
Requires:         R-utils 

%description
An implementation of the nodiv algorithm, see Borregaard, M.K., Rahbek,
C., Fjeldsaa, J., Parra, J.L., Whittaker, R.J. & Graham, C.H. 2014.
Node-based analysis of species distributions. Methods in Ecology and
Evolution 5(11): 1225-1235. <DOI:10.1111/2041-210X.12283>. Package for
phylogenetic analysis of species distributions. The main function goes
through each node in the phylogeny, compares the distributions of the two
descendant nodes, and compares the result to a null model. This highlights
nodes where major distributional divergence have occurred. The
distributional divergence for these nodes is mapped using the SOS
statistic.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
