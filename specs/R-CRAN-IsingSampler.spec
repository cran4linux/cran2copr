%global packname  IsingSampler
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Sampling Methods and Distribution Functions for the Ising Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.4
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-Rcpp >= 0.10.4
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-magrittr 
Requires:         R-nnet 
Requires:         R-CRAN-dplyr 

%description
Sample states from the Ising model and compute the probability of states.
Sampling can be done for any number of nodes, but due to the
intractibility of the Ising model the distribution can only be computed up
to ~10 nodes.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYING
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
