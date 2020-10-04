%global packname  cobs
%global packver   1.3-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          3%{?dist}%{?buildtag}
Summary:          Constrained B-Splines (Sparse Matrix Based)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-quantreg >= 4.65
BuildRequires:    R-CRAN-SparseM >= 1.6
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-quantreg >= 4.65
Requires:         R-CRAN-SparseM >= 1.6
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-methods 

%description
Qualitatively Constrained (Regression) Smoothing Splines via Linear
Programming and Sparse Matrices.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/util.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
