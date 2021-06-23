%global __brp_check_rpaths %{nil}
%global packname  ORdensity
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Identification of Differentially Expressed Genes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-distances 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-cluster 
Requires:         R-CRAN-distances 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-plyr 
Requires:         R-methods 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doRNG 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Automated discovery of differentially expressed genes. The method (called
ORdensity) is composed of two phases: discovering potential differentially
expressed genes and recognizing differentially expressed genes. It makes
use of a permutation resampling procedure to build outlying and density
indexes. References: a) Irigoien, I. and Arenas, C. (2018).
"Identification of differentially expressed genes by means of outlier
detection". <doi:10.1186/s12859-018-2318-8>. b) Martínez-Otzeta, J. M.,
Irigoien, I., Sierra, B., and Arenas, C. (2020). "ORdensity: user-friendly
R package to identify differentially expressed genes".
<doi:10.1186/s12859-020-3463-4>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
