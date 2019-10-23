%global packname  NHEMOtree
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Non-hierarchical evolutionary multi-objective tree learner toperform cost-sensitive classification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-emoa 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-rpart 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-emoa 
Requires:         R-CRAN-sets 
Requires:         R-rpart 

%description
NHEMOtree performs cost-sensitive classification by solving the
two-objective optimization problem of minimizing misclassification rate
and minimizing total costs for classification. The three methods comprised
in NHEMOtree are based on EMOAs with either tree representation or
bitstring representation with an enclosed classification tree algorithm.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
