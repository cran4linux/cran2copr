%global packname  krm
%global packver   2020.5-20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2020.5.20
Release:          3%{?dist}
Summary:          Kernel Based Regression Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-kyotil 
BuildRequires:    R-methods 
Requires:         R-CRAN-kyotil 
Requires:         R-methods 

%description
Implements several methods for testing the variance component parameter in
regression models that contain kernel-based random effects, including a
maximum of adjusted scores test. Several kernels are supported, including
a profile hidden Markov model mutual information kernel for protein
sequence. This package is described in Fong et al. (2015)
<DOI:10.1093/biostatistics/kxu056>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/misc
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
