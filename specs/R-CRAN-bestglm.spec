%global packname  bestglm
%global packver   0.37.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.37.3
Release:          2%{?dist}
Summary:          Best Subset GLM and Regression Utilities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-CRAN-pls 
Requires:         R-CRAN-leaps 
Requires:         R-lattice 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-grpreg 
Requires:         R-CRAN-pls 

%description
Best subset glm using information criteria or cross-validation, carried by
using 'leaps' algorithm (Furnival and Wilson, 1974) <doi:10.2307/1267601>
or complete enumeration (Morgan and Tatar, 1972)
<doi:10.1080/00401706.1972.10488918>. Implements PCR and PLS using
AIC/BIC. Implements one-standard deviation rule for use with the 'caret'
package.

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
%doc %{rlibdir}/%{packname}/bestglm.pdf
%doc %{rlibdir}/%{packname}/SimExperimentBICq.pdf
%{rlibdir}/%{packname}/INDEX
