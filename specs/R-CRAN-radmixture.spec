%global packname  radmixture
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          Calculate Population Stratification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MCMCpack 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MCMCpack 

%description
Implementation of ADMIXTURE for individual ancestry inference in R.
Specifically, ADMIXTURE is a software tool for maximum likelihood
estimation of individual ancestries from multilocus SNP genotype datasets,
see <https://www.genetics.ucla.edu/software/admixture/>. Users can use
'radmixture' to calculate ancestry components with different public
datasets. It is very convenient and fast for personal genotype data. For
more details, see
<https://github.com/wegene-llc/radmixture/blob/master/README.md>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
