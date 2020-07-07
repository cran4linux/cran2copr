%global packname  qsub
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Running Commands Remotely on 'Gridengine' Clusters

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-random 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-ssh 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-random 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-ssh 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Run lapply() calls in parallel by submitting them to 'gridengine' clusters
using the 'qsub' command.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
