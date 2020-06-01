%global packname  RDFTensor
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Different Tensor Factorization (Decomposition) Techniques forRDF Tensors (Three-Mode-Tensors)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 

%description
Different Tensor Factorization techniques suitable for RDF Tensors. RDF
Tensors are three-mode-tensors, binary tensors and usually very sparse.
Currently implemented methods are 'RESCAL' Maximilian Nickel, Volker
Tresp, and Hans-Peter Kriegel (2012) <doi:10.1145/2187836.2187874>, 'NMU'
Daniel D. Lee and H. Sebastian Seung (1999) <doi:10.1038/44565>, 'ALS',
Alternating Least Squares 'parCube' Papalexakis, Evangelos, C. Faloutsos,
and N. Sidiropoulos (2012) <doi:10.1007/978-3-642-33460-3_39>, 'CP_APR' C.
Chi and T. G. Kolda (2012) <doi.org/10.1137/110859063>. The code is mostly
converted from MATLAB and Python implementations of these methods. The
package also contains functions to get Boolean (Binary) transformation of
the real-number-decompositions. These methods also are for general
tensors, so with few modifications they can be applied for other types of
tensor.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/toy_vicePresident.nt
%{rlibdir}/%{packname}/INDEX
