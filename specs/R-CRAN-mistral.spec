%global packname  mistral
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          3%{?dist}
Summary:          Methods in Structural Reliability Analysis

License:          CeCILL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-emoa 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-CRAN-e1071 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-emoa 
Requires:         R-CRAN-quadprog 

%description
Various reliability analysis methods for rare event inference: 1)
computing failure probability (probability that the output of a numerical
model exceeds a threshold), 2) computing quantiles of low or high-order,
3) Wilks formula to compute quantile(s) from a sample or the size of the
required i.i.d. sample.

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
%doc %{rlibdir}/%{packname}/COPYRIGHT
%{rlibdir}/%{packname}/INDEX
