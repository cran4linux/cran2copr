%global packname  nnTensor
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Non-Negative Tensor Decomposition

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-tagcloud 
Requires:         R-methods 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-tagcloud 

%description
Some functions for performing non-negative matrix factorization,
non-negative CANDECOMP/PARAFAC (CP) decomposition, non-negative Tucker
decomposition, and generating toy model data. See Andrzej Cichock et al
(2009) <doi:10.1002/9780470747278> and the reference section of GitHub
README.md <https://github.com/rikenbit/nnTensor>, for details of the
methods.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
