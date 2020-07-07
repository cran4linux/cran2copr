%global packname  palmtree
%global packver   0.9-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          3%{?dist}
Summary:          Partially Additive (Generalized) Linear Model Trees

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula >= 1.2.1
BuildRequires:    R-CRAN-partykit 
Requires:         R-CRAN-Formula >= 1.2.1
Requires:         R-CRAN-partykit 

%description
This is an implementation of model-based trees with global model
parameters (PALM trees). The PALM tree algorithm is an extension to the
MOB algorithm (implemented in the 'partykit' package), where some
parameters are fixed across all groups. Details about the method can be
found in Seibold, Hothorn, Zeileis (2016) <arXiv:1612.07498>. The package
offers coef(), logLik(), plot(), and predict() functions for PALM trees.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
