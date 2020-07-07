%global packname  MKpower
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          3%{?dist}
Summary:          Power Analysis and Sample Size Calculation

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MKinfer >= 0.4
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixTests 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MKdescr 
BuildRequires:    R-CRAN-qqplotr 
BuildRequires:    R-CRAN-coin 
Requires:         R-CRAN-MKinfer >= 0.4
Requires:         R-stats 
Requires:         R-CRAN-matrixTests 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MKdescr 
Requires:         R-CRAN-qqplotr 
Requires:         R-CRAN-coin 

%description
Power analysis and sample size calculation for Welch and Hsu (Hedderich
and Sachs (2018), ISBN:978-3-662-56657-2) t-tests including Monte-Carlo
simulations of empirical power and type-I-error. Power and sample size
calculation for Wilcoxon rank sum and signed rank tests via Monte-Carlo
simulations. Power and sample size required for the evaluation of a
diagnostic test(-system) (Flahault et al. (2005),
<doi:10.1016/j.jclinepi.2004.12.009>; Dobbin and Simon (2007),
<doi:10.1093/biostatistics/kxj036>) as well as for a single proportion
(Fleiss et al. (2003), ISBN:978-0-471-52629-2) and comparing two negative
binomial rates (Zhu and Lakkis (2014), <doi:10.1002/sim.5947>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
