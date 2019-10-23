%global packname  uwIntroStats
%global packver   0.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          1%{?dist}
Summary:          Descriptive Statistics, Inference, Regression, and Plotting inan Introductory Statistics Course

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Exact 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-Exact 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-plyr 
Requires:         R-survival 
Requires:         R-CRAN-sandwich 

%description
A set of tools designed to facilitate easy adoption of R for students in
introductory classes with little programming experience. Compiles output
from existing routines together in an intuitive format, and adds
functionality to existing functions. For instance, the regression function
can perform linear models, generalized linear models, Cox models, or
generalized estimating equations. The user can also specify
multiple-partial F-tests to print out with the model coefficients. We also
give many routines for descriptive statistics and plotting.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
