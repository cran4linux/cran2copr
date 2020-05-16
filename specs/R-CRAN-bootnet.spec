%global packname  bootnet
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}
Summary:          Bootstrap Methods for Various Network Estimation Routines

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mgm >= 1.2
BuildRequires:    R-CRAN-NetworkToolbox >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 0.3.0.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-IsingFit 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-IsingSampler 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-huge 
BuildRequires:    R-CRAN-relaimpo 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-graphicalVAR 
BuildRequires:    R-CRAN-BDgraph 
BuildRequires:    R-CRAN-psychTools 
BuildRequires:    R-CRAN-networktools 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-glasso 
Requires:         R-CRAN-mgm >= 1.2
Requires:         R-CRAN-NetworkToolbox >= 1.1.0
Requires:         R-CRAN-dplyr >= 0.3.0.2
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-IsingFit 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-IsingSampler 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-abind 
Requires:         R-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-huge 
Requires:         R-CRAN-relaimpo 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-graphicalVAR 
Requires:         R-CRAN-BDgraph 
Requires:         R-CRAN-psychTools 
Requires:         R-CRAN-networktools 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-glasso 

%description
Bootstrap methods to assess accuracy and stability of estimated network
structures and centrality indices <doi:10.3758/s13428-017-0862-1>. Allows
for flexible specification of any undirected network estimation procedure
in R, and offers default sets for various estimation routines.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
