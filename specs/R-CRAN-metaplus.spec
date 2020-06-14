%global packname  metaplus
%global packver   0.7-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.11
Release:          2%{?dist}
Summary:          Robust Meta-Analysis and Meta-Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bbmle 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-boot 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-bbmle 
Requires:         R-CRAN-metafor 
Requires:         R-boot 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-MASS 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-CRAN-lme4 

%description
Performs meta-analysis and meta-regression using standard and robust
methods with confidence intervals based on the profile likelihood. Robust
methods are based on alternative distributions for the random effect,
either the t-distribution (Lee and Thompson, 2008 <doi:10.1002/sim.2897>
or Baker and Jackson, 2008 <doi:10.1007/s10729-007-9041-8>) or mixtures of
normals (Beath, 2014 <doi:10.1002/jrsm.1114>).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
