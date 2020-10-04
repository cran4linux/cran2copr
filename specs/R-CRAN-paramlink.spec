%global packname  paramlink
%global packver   1.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Parametric Linkage and Other Pedigree Analysis in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-assertthat 
Requires:         R-graphics 
Requires:         R-CRAN-kinship2 
Requires:         R-CRAN-maxLik 
Requires:         R-stats 
Requires:         R-utils 

%description
A suite of tools for analysing pedigrees with marker data, including
parametric linkage analysis, forensic computations, relatedness analysis
and marker simulations. The core of the package is an implementation of
the Elston-Stewart algorithm for pedigree likelihoods, extended to allow
mutations as well as complex inbreeding. Features for linkage analysis
include singlepoint LOD scores, power analysis, and multipoint analysis
(the latter through a wrapper to the 'MERLIN' software). Forensic
applications include exclusion probabilities, genotype distributions and
conditional simulations. Data from the 'Familias' software can be imported
and analysed in 'paramlink'. Finally, 'paramlink' offers many utility
functions for creating, manipulating and plotting pedigrees with or
without marker data (the actual plotting is done by the 'kinship2'
package).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
