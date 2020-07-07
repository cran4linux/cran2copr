%global packname  multcomp
%global packver   1.4-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.13
Release:          3%{?dist}
Summary:          Simultaneous Inference in General Parametric Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival >= 2.39.4
BuildRequires:    R-CRAN-sandwich >= 2.3.0
BuildRequires:    R-CRAN-TH.data >= 1.0.2
BuildRequires:    R-CRAN-mvtnorm >= 1.0.10
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-codetools 
Requires:         R-survival >= 2.39.4
Requires:         R-CRAN-sandwich >= 2.3.0
Requires:         R-CRAN-TH.data >= 1.0.2
Requires:         R-CRAN-mvtnorm >= 1.0.10
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-codetools 

%description
Simultaneous tests and confidence intervals for general linear hypotheses
in parametric models, including linear, generalized linear, linear mixed
effects, and survival models. The package includes demos reproducing
analyzes presented in the book "Multiple Comparisons Using R" (Bretz,
Hothorn, Westfall, 2010, CRC Press).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/deprecated
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/MCMT
%doc %{rlibdir}/%{packname}/multcomp_coxme.R
%doc %{rlibdir}/%{packname}/multcomp_VA.R
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
