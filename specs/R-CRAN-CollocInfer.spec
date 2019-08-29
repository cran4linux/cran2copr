%global packname  CollocInfer
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Collocation Inference for Dynamic Systems

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-methods 
Requires:         R-CRAN-fda 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-deSolve 
Requires:         R-methods 

%description
These functions implement collocation-inference for continuous-time and
discrete-time stochastic processes. They provide model-based smoothing,
gradient-matching, generalized profiling and forwards prediction error
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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/CollocInferManual.pdf
%doc %{rlibdir}/%{packname}/Devel
%doc %{rlibdir}/%{packname}/Devel.Examples
%doc %{rlibdir}/%{packname}/MatlabCollocInfer
%doc %{rlibdir}/%{packname}/OldCode
%doc %{rlibdir}/%{packname}/OldDemo
%doc %{rlibdir}/%{packname}/todo.txt
%doc %{rlibdir}/%{packname}/trymcmc.r
%doc %{rlibdir}/%{packname}/trymcmc2.r
%{rlibdir}/%{packname}/INDEX
