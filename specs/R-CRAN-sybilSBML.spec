%global packname  sybilSBML
%global packver   3.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.2
Release:          1%{?dist}
Summary:          'SBML' Integration in Package 'Sybil'

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.2
Requires:         R-core >= 2.14.2
BuildRequires:    R-CRAN-sybil >= 2.0.0
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-sybil >= 2.0.0
Requires:         R-Matrix 
Requires:         R-methods 

%description
'SBML' (Systems Biology Markup Language) with 'FBC' (Flux Balance
Constraints) integration in 'sybil'. Many constraint based metabolic
models are published in 'SBML' format ('*.xml'). Herewith is the ability
to read, write, and check 'SBML' files in 'sybil' provided.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/INSTALL
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/README
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
