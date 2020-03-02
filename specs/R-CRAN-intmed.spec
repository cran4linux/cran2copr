%global packname  intmed
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Mediation Analysis using Interventional Effects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-EValue 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyverse 
Requires:         R-MASS 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-EValue 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
Implementing the interventional effects for mediation analysis for up to 3
mediators. The methods used are based on VanderWeele, Vansteelandt and
Robins (2014) <doi:10.1097/ede.0000000000000034>, Vansteelandt and Daniel
(2017) <doi:10.1097/ede.0000000000000596> and Chan and Leung (2020;
unpublished manuscript, available on request from the author of this
package). Linear regression, logistic regression and Poisson regression
are used for continuous, binary and count mediator/outcome variables
respectively.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
