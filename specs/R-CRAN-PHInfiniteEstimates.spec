%global packname  PHInfiniteEstimates
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Tools for Inference in the Presence of a Monotone Likelihood

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-mlogit 
BuildRequires:    R-CRAN-coxphf 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-survival 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-mlogit 
Requires:         R-CRAN-coxphf 

%description
Proportional hazards estimation in the presence of a partially monotone
likelihood has difficulties, in that finite estimators do not exist.
These difficulties are related to those arising from logistic and
multinomial regression.  References for methods are given in the separate
function documents.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
