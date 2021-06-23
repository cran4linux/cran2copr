%global __brp_check_rpaths %{nil}
%global packname  PartCensReg
%global packver   1.39
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.39
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation and Diagnostics for Partially Linear CensoredRegression Models Based on Heavy-Tailed Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ssym 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-ssym 
Requires:         R-CRAN-optimx 
Requires:         R-Matrix 

%description
It estimates the parameters of a partially linear regression censored
model via maximum penalized likelihood through of ECME algorithm. The
model belong to the semiparametric class, that including a parametric and
nonparametric component. The error term considered belongs to the
scale-mixture of normal (SMN) distribution, that includes well-known heavy
tails distributions as the Student-t distribution, among others. To
examine the performance of the fitted model, case-deletion and local
influence techniques are provided to show its robust aspect against
outlying and influential observations. This work is based in Ferreira, C.
S., & Paula, G. A. (2017) <doi:10.1080/02664763.2016.1267124> but
considering the SMN family.

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
%{rlibdir}/%{packname}/INDEX
