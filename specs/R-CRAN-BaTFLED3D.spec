%global packname  BaTFLED3D
%global packver   0.2.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.11
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Tensor Factorization Linked to External Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-RColorBrewer 

%description
BaTFLED is a machine learning algorithm designed to make predictions and
determine interactions in data that varies along three independent modes.
For example BaTFLED was developed to predict the growth of cell lines when
treated with drugs at different doses. The first mode corresponds to cell
lines and incorporates predictors such as cell line genomics and growth
conditions. The second mode corresponds to drugs and incorporates
predictors indicating known targets and structural features. The third
mode corresponds to dose and there are no dose-specific predictors
(although the algorithm is capable of including predictors for the third
mode if present). See 'BaTFLED3D_vignette.rmd' for a simulated example.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
