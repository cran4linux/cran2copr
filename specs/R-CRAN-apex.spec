%global packname  apex
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Phylogenetic Methods for Multiple Gene Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-adegenet 
Requires:         R-methods 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phangorn 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-adegenet 

%description
Toolkit for the analysis of multiple gene data (Jombart et al. 2017)
<doi:10.1111/1755-0998.12567>. Apex implements the new S4 classes
'multidna', 'multiphyDat' and associated methods to handle aligned DNA
sequences from multiple genes.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/patr_poat43.fasta
%doc %{rlibdir}/%{packname}/patr_poat47.fasta
%doc %{rlibdir}/%{packname}/patr_poat48.fasta
%doc %{rlibdir}/%{packname}/patr_poat49.fasta
%{rlibdir}/%{packname}/INDEX
