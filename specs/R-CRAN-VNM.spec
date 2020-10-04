%global packname  VNM
%global packver   7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.1
Release:          3%{?dist}%{?buildtag}
Summary:          Finding Multiple-Objective Optimal Designs for the 4-ParameterLogistic Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 

%description
Provide tools for finding multiple-objective optimal designs for
estimating the shape of dose-response, the ED50 (the dose producing an
effect midway between the expected responses at the extreme doses) and the
MED (the minimum effective dose level) for the 2,3,4-parameter logistic
models and for evaluating its efficiencies for the three objectives. The
acronym VNM stands for V-algorithm using Newton Raphson method to search
multiple-objective optimal design.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
