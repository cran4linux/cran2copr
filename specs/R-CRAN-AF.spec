%global packname  AF
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}
Summary:          Model-Based Estimation of Confounder-Adjusted AttributableFractions

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-base 
BuildRequires:    R-graphics 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-drgee 
BuildRequires:    R-CRAN-stdReg 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ivtools 
Requires:         R-stats 
Requires:         R-base 
Requires:         R-graphics 
Requires:         R-survival 
Requires:         R-CRAN-drgee 
Requires:         R-CRAN-stdReg 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ivtools 

%description
Estimates the attributable fraction in different sampling designs adjusted
for measured confounders using logistic regression (cross-sectional and
case-control designs), conditional logistic regression (matched
case-control design), Cox proportional hazard regression (cohort design
with time-to- event outcome), gamma-frailty model with a Weibull baseline
hazard and instrumental variables analysis. An exploration of the AF with
a genetic exposure can be found in the package 'AFheritability' Dahlqwist
E et al. (2019) <doi:10.1007/s00439-019-02006-8>.

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
