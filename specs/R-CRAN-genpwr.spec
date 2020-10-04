%global packname  genpwr
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Power Calculations Under Genetic Model Misspecification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nleqslv 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-utils 

%description
Power and sample size calculations for genetic association studies
allowing for misspecification of the model of genetic susceptibility.
Power and/or sample size can be calculated for logistic (case/control
study design) and linear (continuous phenotype) regression models, using
additive, dominant, recessive or degree of freedom coding of the genetic
covariate while assuming a true dominant, recessive or additive genetic
effect. In addition, power and sample size calculations can be performed
for gene by environment interactions. These methods are extensions of
Gauderman (2002) <doi:10.1093/aje/155.5.478> and Gauderman (2002)
<doi:10.1002/sim.973> and are described in: Moore CM, Jacobson S,
Fingerlin TE. Power and Sample Size Calculations for Genetic Association
Studies in the Presence of Genetic Model Misspecification. American
Society of Human Genetics. October 2018, San Diego.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
