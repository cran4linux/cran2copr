%global packname  sodavis
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          SODA: Main and Interaction Effects Selection for LogisticRegression, Quadratic Discriminant and General Index Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-nnet 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-nnet 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 

%description
Variable and interaction selection are essential to classification in
high-dimensional setting. In this package, we provide the implementation
of SODA procedure, which is a forward-backward algorithm that selects both
main and interaction effects under logistic regression and quadratic
discriminant analysis. We also provide an extension, S-SODA, for dealing
with the variable selection problem for semi-parametric models with
continuous responses.

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
%{rlibdir}/%{packname}/INDEX
