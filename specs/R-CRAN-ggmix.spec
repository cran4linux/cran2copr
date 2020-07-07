%global packname  ggmix
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}
Summary:          Variable Selection in Linear Mixed Models for SNP Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-Matrix 

%description
Fit penalized multivariable linear mixed models with a single random
effect to control for population structure in genetic association studies.
The goal is to simultaneously fit many genetic variants at the same time,
in order to select markers that are independently associated with the
response. Can also handle prior annotation information, for example, rare
variants, in the form of variable weights. For more information, see the
website below and the accompanying paper: Bhatnagar et al., "Simultaneous
SNP selection and adjustment for population structure in high dimensional
prediction models", 2020, <DOI:10.1101/408484>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
