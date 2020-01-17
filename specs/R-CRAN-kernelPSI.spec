%global packname  kernelPSI
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Post-Selection Inference for Nonlinear Variable Selection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-lmtest 

%description
Different post-selection inference strategies for kernel selection, as
described in "kernelPSI: a Post-Selection Inference Framework for
Nonlinear Variable Selection", Slim et al., Proceedings of Machine
Learning Research, 2019,
<http://proceedings.mlr.press/v97/slim19a/slim19a.pdf>. The strategies
rest upon quadratic kernel association scores to measure the association
between a given kernel and an outcome of interest. The inference step
tests for the joint effect of the selected kernels on the outcome. A fast
constrained sampling algorithm is proposed to derive empirical p-values
for the test statistics.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
