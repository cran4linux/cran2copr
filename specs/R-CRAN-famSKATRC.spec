%global packname  famSKATRC
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Family Sequence Kernel Association Test for Rare and CommonVariants

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.1
Requires:         R-core >= 3.4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-CRAN-coxme 
BuildRequires:    R-CRAN-bdsmatrix 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-kinship2 
Requires:         R-CRAN-coxme 
Requires:         R-CRAN-bdsmatrix 

%description
FamSKAT-RC is a family-based association kernel test for both rare and
common variants. This test is general and several special cases are known
as other methods: famSKAT, which only focuses on rare variants in
family-based data, SKAT, which focuses on rare variants in
population-based data (unrelated individuals), and SKAT-RC, which focuses
on both rare and common variants in population-based data. When one
applies famSKAT-RC and sets the value of phi to 1, famSKAT-RC becomes
famSKAT. When one applies famSKAT-RC and set the value of phi to 1 and the
kinship matrix to the identity matrix, famSKAT-RC becomes SKAT. When one
applies famSKAT-RC and set the kinship matrix (fullkins) to the identity
matrix (and phi is not equal to 1), famSKAT-RC becomes SKAT-RC. We also
include a small sample synthetic pedigree to demonstrate the method with.
For more details see Saad M and Wijsman EM (2014)
<doi:10.1002/gepi.21844>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
